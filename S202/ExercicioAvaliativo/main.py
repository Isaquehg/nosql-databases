from database import Database
import threading
import time
import random

db = Database(database="bancoiot", collection="sensores")
db.resetDatabase()

def gerTemp1():
    alarmado1 = False

    #executar thread enquanto temperatura for ate 38
    while not(alarmado1):
        temp1 = random.randint(30, 40)

        #desativar caso a temperatura for > 38
        if temp1 > 38:
            alarmado1 = True
            print("Atenção! Temperatura  muito  alta! Verificar Sensor 1!")
            print("Sensor 1 desativado")
            db.collection.insert_one({
                                      "nomeSensor": "Temp1",
                                      "valorSensor": temp1,
                                      "unidadeMedida": "C",
                                      "sensorAlarmado": alarmado1
                                    })

        print(f"Temperatura do sensor 1 = {temp1}")
        db.collection.insert_one({
                                  "nomeSensor": "Temp1",
                                  "valorSensor": temp1,
                                  "unidadeMedida": "C",
                                  "sensorAlarmado": alarmado1
                                })
        time.sleep(2)
        
def gerTemp2():
    alarmado2 = False
    while not(alarmado2):
        temp2 = random.randint(30, 40)

        if temp2 > 38:
            alarmado2 = True
            print("Atenção! Temperatura  muito  alta! Verificar Sensor 2!")
            print("Sensor 2 desativado")
            db.collection.insert_one({
                                        "nomeSensor": "Temp2",
                                        "valorSensor": temp2,
                                        "unidadeMedida": "C",
                                        "sensorAlarmado": alarmado2
                                    })

        print(f"Temperatura do sensor 2 = {temp2}")
        db.collection.insert_one({
                                  "nomeSensor": "Temp2",
                                  "valorSensor": temp2,
                                  "unidadeMedida": "C",
                                  "sensorAlarmado": alarmado2
                                })
        time.sleep(3)

def gerTemp3():
    alarmado3 = False
    while not(alarmado3):
        temp3 = random.randint(30, 40)

        if temp3 > 38:
            alarmado3 = True
            print("Atenção! Temperatura  muito  alta! Verificar Sensor 3!")
            print("Sensor 3 desativado")
            db.collection.insert_one({
                                  "nomeSensor": "Temp3",
                                  "valorSensor": temp3,
                                  "unidadeMedida": "C",
                                  "sensorAlarmado": alarmado3
                                })

        print(f"Temperatura do sensor 3 = {temp3}")
        db.collection.insert_one({
                                  "nomeSensor": "Temp3",
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
