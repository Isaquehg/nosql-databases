from pymongo import MongoClient
from database import Database
from book_model import BookModel

#CLIENT EXERCICIO 1
#db = Database(database="livraria", collection="livros")
#db.resetDatabase()

#CLIENT EXERCICIO 2
client = MongoClient("localhost:27017")
db = client["livraria"]
book_model = BookModel(db)

#create
book_id = book_model.create_book(3, "Elon Musk", "Ashlee Vance", 2015, 25.12)

#read
book = book_model.read_book_by_id(book_id)

#update
book_model.update_book(book_id, "Elon Reeve Musk", "Ashlee Vance", 2015, 25.12)

#delete
book_model.delete_book(book_id)