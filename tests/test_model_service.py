import pytest
from bson import ObjectId  # type: ignore
from motor_orm import model, model_service


def test_tofromdb():
    assert BookService._model_to_db(
        Book(name="test")
    ) == {'name': 'test', '_id': None}

    assert BookService._db_to_model(
        {'name': 'test', '_id': None}
    ) == Book(name="test")


class Book(model.Model):
    name: str


class BookService(model_service.ModelService):
    model = Book


@pytest.fixture
def book_service(db):
    return BookService(db)


@pytest.mark.asyncio
async def test_insert_one(book_service):
    inserted_id = await book_service.insert_one(Book(name="test_insert_one"))
    assert isinstance(inserted_id, ObjectId)


@pytest.mark.asyncio
async def test_get_by_id(book_service):
    inserted_id = await book_service.insert_one(Book(name="test_get_by_id"))
    created_entry = await book_service.get_by_id(inserted_id)
    assert created_entry.name == "test_get_by_id"


@pytest.mark.asyncio
async def test_find_one(book_service):
    inserted_id = await book_service.insert_one(Book(name="test_find_one"))
    found = await book_service.find_one({"name": "test_find_one"})

    assert found.id == inserted_id
    assert found.name == 'test_find_one'


@pytest.mark.asyncio
async def test_insert_many(book_service):
    inserted_ids = await book_service.insert_many([
        Book(name="test_insert_many_0"),
        Book(name="test_insert_many_1"),
        Book(name="test_insert_many_2"),
    ])

    assert len(inserted_ids) == 3

    assert (
        await book_service.get_by_id(inserted_ids[0])
    ).name == 'test_insert_many_0'
    assert (
        await book_service.get_by_id(inserted_ids[1])
    ).name == 'test_insert_many_1'
    assert (
        await book_service.get_by_id(inserted_ids[2])
    ).name == 'test_insert_many_2'
