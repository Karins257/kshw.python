import os

import pytest

from db_table import DatabaseTable


@pytest.fixture(scope="session")
def db_table():
    if not os.getenv("DATABASE_URL"):
        pytest.skip("DATABASE_URL is not set")
    return DatabaseTable.from_environment()
