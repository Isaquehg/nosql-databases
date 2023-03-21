from save import writeAJson

class ProductAnalyzer():
    def __init__(self, db):
        self.db = db

    # gasto total cliente B
    def gastoClienteB(self):
        result1 = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        ])
        result1 = list(result1)
        result1 = result1[1]

        writeAJson(result1, "gasto-cliente-b")
        return result1

    # produto menos vendido
    def menosVendido(self):
        result2 = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": 1}},
            {"$limit": 1}
        ])

        writeAJson(result2, "prod-menos-vendido")
        return result2

    # cliente que menos gastou
    def muquirana(self):
        result3 = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": 1}},
            {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
        ])

        writeAJson(result3, "muquirana")
        return result3
    
    # produtos com mais de duas unidades vendidas
    def maisQDois(self):
        result4 = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$group": {"total": {"$gt": 2}}},
            {"$sort": {"total": 1}}
        ])

        writeAJson(result4, "mais-q-dois")
        return result4
