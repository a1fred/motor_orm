import pytest
from motor_orm.db import Database, get_db


@pytest.mark.asyncio
async def test_get_db(mongodb_database_name, mongodb_connectionstring):
    db: Database = await get_db(
        mongodb_database_name=mongodb_database_name,
        mongodb_connectionstring=mongodb_connectionstring,
    )
    assert isinstance(db, Database)


@pytest.mark.asyncio
async def test_get_db_dropdb(mongodb_database_name, mongodb_connectionstring):
    db: Database = await get_db(
        mongodb_database_name=mongodb_database_name,
        mongodb_connectionstring=mongodb_connectionstring,
        dropdb=True,
    )
    assert isinstance(db, Database)
