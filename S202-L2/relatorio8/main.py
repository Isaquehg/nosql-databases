from database import Database
from game import Game

# Neo4j Config.
db = Database("bolt://44.212.36.171:7687", "neo4j", "dawn-computers-drillers")
db.drop_all()
game_db = Game(db)

game_db.create_player(0, "Larry")
game_db.create_player(1, "Darry")
game_db.create_player(2, "Garry")
game_db.create_player(3, "Perry")
game_db.create_player(4, "Harry")
game_db.create_player(5, "Merry")


game_db.create_match(0)
game_db.create_match(1)
game_db.create_match(2)

game_db.insert_player_match("Larry", 0)
game_db.insert_player_match("Darry", 0)
game_db.insert_player_match("Garry", 0)

game_db.insert_player_match("Perry", 1)
game_db.insert_player_match("Harry", 1)

game_db.delete_player("Merry")
game_db.delete_match(2)

print()

db.close()