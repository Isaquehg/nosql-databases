from pokedex import Database
from save import writeAJson

db = Database(database="dex", collection="pokemons")
db.resetDatabase()

# encontrar todos elementos
def findAll():
    pokemons = db.collection.find()
    return pokemons

# encontrar elemento pelo ID
def getByID(number: int):
    return db.collection.find({"id": number})

# encontrar elementos do tipo água
def getWaterType():
    return db.collection.find({"type": "Water"})

# encontrar speed > 70
def getHighSpeed():
    return db.collection.find({"base.Speed": {"$gt": 70}})

# nomes com 5 letras ou mais
def getFiveOrMore():
    #wants to return only "name" (name: 1) in second find parameter and NOT ID
    names = db.collection.find({}, {"_id": 0, "name.english": 1})
    five_letters_or_more = []
    #print(names)
    #print(type(names))
    for name in names:
        name = list(name['name'].values())
        print(name[0])
        if len(name[0]) > 4:
            #if all(len(word) > 4 for word in name['name'].values()):
            five_letters_or_more.append(name[0])
    return five_letters_or_more

# consulta 1
pokemons = findAll()
writeAJson(pokemons, "pokemons")

# consulta 2
pokemon_x = getByID(5)
writeAJson(pokemon_x, "pokemon_x")

# consulta 3
water_poke = getWaterType()
writeAJson(water_poke, "water_poke")

# consulta 4
high_speed = getHighSpeed()
writeAJson(high_speed, "high_speed")

# consulta 5
five_or_more_letters = getFiveOrMore()
writeAJson(five_or_more_letters, "five_or_more_letters")

