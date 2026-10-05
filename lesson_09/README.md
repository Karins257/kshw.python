# Lesson 9: database tests

The tests use SQLAlchemy and do not store database credentials in the
repository. Before running them, set the connection string:

```text
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/database
```

By default, the tests work with the `subjects` table and automatically find
its primary key and first editable text column. If the local schema uses other
names, set them explicitly:

```text
DB_TEST_TABLE=subjects
DB_TEST_FIELD=title
```

Install dependencies and run the tests:

```text
pip install -r lesson_09/requirements.txt
pytest lesson_09
```
