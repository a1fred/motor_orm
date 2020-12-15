# Motor orm
![CI](https://github.com/a1fred/motor_orm/workflows/CI/badge.svg?branch=master)
Simple motor and pydantic based orm created not to underfoot.

```python
from typing import List
import asyncio
from motor_orm import get_db, ModelService, Model


# Define model
class Book(Model):
    name: str
    book_collections: List[str] = []


# Define model service
class BookService(ModelService):
    model = Book

    async def create_collection(self):
        """
        Hook called when db connection created
        """
        await self.collection.create_index('name', unique=True)

    async def get_book_collection(self, collection_name: str):
        """
        Find all books in book_collections
        """
        res = []
        async for doc in self.collection.find({'collections': collection_name).sort(name, -1):
            res.append(self._db_to_model(doc))
        return res


async def main():
    db = await get_db(
        mongodb_database_name='test_db',
        mongodb_connectionstring="mongodb://127.0.0.1:27017",
    )
    book_service = BookService(db)
    book_id = await book_service.insert_one(Book(name='test'))

asyncio.run(main())
```