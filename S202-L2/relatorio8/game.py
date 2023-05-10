class Game:
    def __init__(self, database):
        self.db = database

    def create_player(self, id: int, name: str):
        query = "CREATE (:Player {id: $id, name: $name})"
        parameters = {"id": id, "name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, id: int):
        query = "CREATE (:Match {id: $id})"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_matches(self):
        query = "MATCH (m:Match)<-[:JOGA]-(p:Player) RETURN m.id AS id, p.name AS player_name"
        results = self.db.execute_query(query)
        return [(result["id"], result["player_name"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def insert_player_match(self, player_name, match_id):
        query = "MATCH (p:Player {name: $player_name}) MATCH (m:Match {id: $match_id}) CREATE (p)-[:JOGA]->(m)"
        parameters = {"player_name": player_name, "match_id": match_id}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_match(self, id):
        query = "MATCH (m:Match {id: $id})<-[:JOGA]-(p:Player) DETACH DELETE m"
        parameters = {"id": id}
        self.db.execute_query(query, parameters)