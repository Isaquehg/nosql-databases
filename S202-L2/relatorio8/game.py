class Game:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Jogador {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_aluno(self, name):
        query = "CREATE (:Aluno {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_aula(self, name, professor_name):
        query = "MATCH (p:Professor {name: $professor_name}) CREATE (:Aula {name: $name})<-[:MINISTRA]-(p)"
        parameters = {"name": name, "professor_name": professor_name}
        self.db.execute_query(query, parameters)

    def get_professores(self):
        query = "MATCH (p:Professor) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_alunos(self):
        query = "MATCH (a:Aluno) RETURN a.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_aulas(self):
        query = "MATCH (a:Aula)<-[:MINISTRA]-(p:Professor) RETURN a.name AS name, p.name AS professor_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["professor_name"]) for result in results]

    def update_professor(self, old_name, new_name):
        query = "MATCH (p:Professor {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def insert_aluno_aula(self, aluno_name, aula_name):
        query = "MATCH (a:Aluno {name: $aluno_name}) MATCH (b:Aula {name: $aula_name}) CREATE (a)-[:ASSISTE]->(b)"
        parameters = {"aluno_name": aluno_name, "aula_name": aula_name}
        self.db.execute_query(query, parameters)
    
    def insert_professor_aula(self, professor_name, aula_name):
        query = "MATCH (a:Professor {name: $professor_name}) MATCH (b:Aula {name: $aula_name}) CREATE (a)-[:MINISTRA]->(b)"
        parameters = {"professor_name": professor_name, "aula_name": aula_name}
        self.db.execute_query(query, parameters)

    def delete_professor(self, name):
        query = "MATCH (p:Professor {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_aluno(self, name):
        query = "MATCH (a:Aluno {name: $name}) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_aula(self, name):
        query = "MATCH (a:Aula {name: $name})<-[:MINISTRA]-(p:Professor) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)