from database import Database

class TeacherCRUD():
    def __init__(self) -> None:
        self.db = Database("bolt://44.208.24.26:7687", "neo4j", "elbows-operands-velocities")

    def create(self, name: str, ano_nasc: int, cpf: str) -> None:
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def retrieve(self, name: str):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.name as name"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["name"] for result in results]

    def update(self, name: str, newCpf: str) -> None:
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $new_cpf"
        parameters = {"name": name, "new_cpf": newCpf}
        self.db.execute_query(query, parameters)

    def delete(self, name: str) -> None:
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)