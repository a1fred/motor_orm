import pytest
from bson import ObjectId  # type: ignore
from motor_orm import model, model_service


class Book(model.Model):
    name: str


class BookService(model_service.ModelService):
    model = Book


@pytest.mark.asyncio
async def test_modelservice_base_methods(db):
    book_service = BookService(db)

    # insert_one
    inserted_id = await book_service.insert_one(Book(name="test"))
    assert isinstance(inserted_id, ObjectId)

    # get_by_id
    created_entry = await book_service.get_by_id(inserted_id)
    assert created_entry.name == "test"

    # find_one
    assert created_entry == await book_service.find_one({"name": "test"})
