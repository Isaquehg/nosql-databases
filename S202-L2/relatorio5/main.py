from database import Database
from save import writeAJson

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

