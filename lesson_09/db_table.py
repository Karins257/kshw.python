import os
from datetime import date, datetime
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update


class DatabaseTable:
    def __init__(self, database_url, table_name="subjects"):
        self.engine = create_engine(database_url)
        self.metadata = MetaData()
        self.table = Table(
            table_name,
            self.metadata,
            autoload_with=self.engine,
        )
        primary_keys = list(self.table.primary_key.columns)
        if len(primary_keys) != 1:
            raise ValueError("The test table must have one primary key")
        self.primary_key = primary_keys[0]
        self.editable_column = self._find_editable_column()

    @classmethod
    def from_environment(cls):
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("Set the DATABASE_URL environment variable")
        table_name = os.getenv("DB_TEST_TABLE", "subjects")
        return cls(database_url, table_name)

    def _find_editable_column(self):
        preferred_name = os.getenv("DB_TEST_FIELD")
        if preferred_name:
            return self.table.c[preferred_name]

        for column in self.table.columns:
            if not column.primary_key and isinstance(column.type, String):
                return column
        raise ValueError(
            "Set DB_TEST_FIELD to an editable text column name"
        )

    def _foreign_key_value(self, connection, column):
        foreign_key = next(iter(column.foreign_keys))
        target_table = Table(
            foreign_key.column.table.name,
            MetaData(),
            autoload_with=self.engine,
        )
        target_column = target_table.c[foreign_key.column.name]
        return connection.execute(select(target_column).limit(1)).scalar_one()

    def _value_for_column(self, connection, column, label):
        if column.foreign_keys:
            return self._foreign_key_value(connection, column)
        if isinstance(column.type, String):
            return label[: column.type.length] if column.type.length else label
        if isinstance(column.type, Boolean):
            return False
        if isinstance(column.type, Integer):
            return int(uuid4().int % 1_000_000_000)
        if isinstance(column.type, (Float, Numeric)):
            return Decimal("1.0")
        if isinstance(column.type, DateTime):
            return datetime.now()
        if isinstance(column.type, Date):
            return date.today()
        raise ValueError(f"Cannot create a value for column {column.name}")

    def build_row(self, label):
        row = {}
        with self.engine.connect() as connection:
            for column in self.table.columns:
                has_generated_value = (
                    column.primary_key
                    and (column.autoincrement is True or column.identity)
                )
                has_default = column.default is not None
                has_server_default = column.server_default is not None
                if has_generated_value or has_default or has_server_default:
                    continue
                if column.nullable and column is not self.editable_column:
                    continue
                row[column.name] = self._value_for_column(
                    connection,
                    column,
                    label,
                )
        return row

    def add(self, values):
        with self.engine.begin() as connection:
            result = connection.execute(insert(self.table).values(**values))
            return result.inserted_primary_key[0]

    def get(self, row_id):
        statement = select(self.table).where(
            self.primary_key == row_id
        )
        with self.engine.connect() as connection:
            return connection.execute(statement).mappings().one_or_none()

    def change_label(self, row_id, new_label):
        statement = (
            update(self.table)
            .where(self.primary_key == row_id)
            .values({self.editable_column.name: new_label})
        )
        with self.engine.begin() as connection:
            connection.execute(statement)

    def remove(self, row_id):
        statement = delete(self.table).where(
            self.primary_key == row_id
        )
        with self.engine.begin() as connection:
            connection.execute(statement)
