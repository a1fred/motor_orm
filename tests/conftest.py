import asyncio
import os

import pytest


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def mongodb_database_name():
    return os.getenv("MOTOR_ORM_TEST_DB_NAME", "motor_orm_tests")


@pytest.fixture(scope="session")
def mongodb_connectionstring():
    return os.getenv("MOTOR_ORM_TEST_DB_CS", "mongodb://127.0.0.1:27017")


@pytest.mark.asyncio
@pytest.fixture(scope="session")
async def db(mongodb_database_name, mongodb_connectionstring):
    from motor_orm.db import get_db

    return await get_db(
        mongodb_database_name=mongodb_database_name,
        mongodb_connectionstring=mongodb_connectionstring,
    )
