from pymongo import MongoClient
from bson.objectid import ObjectId

class BookModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.livros

    def create_book(self, id: int, title: str, author: str, year: int, price: float) -> str:
        try:
            result = self.collection.insert_one({"_id": id, "titulo": title, "autor": author, "ano": year, "preco": price})
            book_id = str(result.inserted_id)
            print(f"Book {title} created with id: {book_id}")
            return book_id
        except Exception as error:
            print(f"An error occurred while creating book: {error}")
            return None

    def read_book_by_id(self, book_id: str) -> dict:
        try:
            book = self.collection.find_one({"_id": book_id})
            if book:
                print(f"Book found: {book}")
                return book
            else:
                print(f"No book found with id {book_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading book: {error}")
            return None

    def update_book(self, book_id: str, title: str, author: str, year: int, price: float) -> int:
        try:
            result = self.collection.update_one({"_id": book_id}, {"$set": {"titulo": title, "autor": author, "ano": author, "ano": year, "preco": price}})
            if result.modified_count:
                print(f"Book {book_id} updated with title {title} and year {year}")
            else:
                print(f"No book found with id {book_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating book: {error}")
            return None

    def delete_book(self, book_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": book_id})
            if result.deleted_count:
                print(f"Book {book_id} deleted")
            else:
                print(f"No book found with id {book_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting book: {error}")
            return None