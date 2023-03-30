from database import Database
import threading
import time
import random

db = Database(database="bancoiot", collection="sensores")
db.resetDatabase()

def gerTemp1():
    while True:
        alarmado1 = False
        temp1 = random.randint(30, 40)

        if temp1 > 38:
            alarmado1 = True
            db.collection.insert_one({
                                      "nomeSensor": "Temp1",
                                      "valorSensor": temp1,
                                      "unidadeMedida": "C",
                                      "sensorAlarmado": alarmado1
                                    })
            break

        print(f"Temperatura do sensor 1 = {temp1}")
        db.collection.insert_one({
                                  "nomeSensor": "Temp1",
                                  "valorSensor": temp1,
                                  "unidadeMedida": "C",
                                  "sensorAlarmado": alarmado1
                                })
        time.sleep(2)
        
def gerTemp2():
    while True:
        alarmado2 = False
        temp2 = random.randint(30, 40)

        if temp2 > 38:
            alarmado2 = True
            db.collection.insert_one({
                                        "nomeSensor": "Temp1",
                                        "valorSensor": temp2,
                                        "unidadeMedida": "C",
                                        "sensorAlarmado": alarmado2
                                    })
            break

        print(f"Temperatura do sensor 2 = {temp2}")
        db.collection.insert_one({
                                  "nomeSensor": "Temp1",
                                  "valorSensor": temp2,
                                  "unidadeMedida": "C",
                                  "sensorAlarmado": alarmado2
                                })
        time.sleep(3)

def gerTemp3():
    while True:
        alarmado3 = False
        temp3 = random.randint(30, 40)

        if temp3 > 38:
            alarmado3 = True
            db.collection.insert_one({
                                  "nomeSensor": "Temp1",
                                  "valorSensor": temp3,
                                  "unidadeMedida": "C",
                                  "sensorAlarmado": alarmado3
                                })
            break

        print(f"Temperatura do sensor 3 = {temp3}")
        db.collection.insert_one({
                                  "nomeSensor": "Temp1",
                                  "valorSensor": temp3,
                                  "unidadeMedida": "C",
                                  "sensorAlarmado": alarmado3
                                })
        time.sleep(4)

#attaching threads to the functions
threadTemp1 = threading.Thread(target = gerTemp1)
threadTemp2 = threading.Thread(target = gerTemp2)
threadTemp3 = threading.Thread(target = gerTemp3)

#initializing threads
threadTemp1.start()
threadTemp2.start()
threadTemp3.start()
