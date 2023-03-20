from database import Database
from save import writeAJson
from productAnalyzer import ProductAnalyzer

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

product_analyzer = ProductAnalyzer(db)

print(product_analyzer.gastoClienteB())
print(product_analyzer.maisQDois())
print(product_analyzer.menosVendido())
print(product_analyzer.muquirana())