import random
import json
from MyMQTT import *
import time



class MyPublisher:

    def __init__(self, topic, clientID,sensorID, broker, port):
        self.sensorID = str(sensorID)
        self.clientID = str(clientID)
        self.topic = topic
        self.client = MyMQTT(self.sensorID, broker, port, None)

        self.__message = {
            #'bn': '',
            'e':
            [
                {'n': 'heart rate', 'value': '', 'timestamp': '', 'unit': 'bpm'},
                {'n': 'Sp02', 'value': '','timestamp': '', 'unit': '%' },
                {'n': 'snooring', 'value': '','timestamp': '', 'unit': 'dB' }
            ]
        }
    
   

    
    def publish(self):
        hr = random.randint(73,93)
        spo2 = random.randint(93,99)
        snooring=random.randint(35,60)
        msn=[]

        

        for t in self.topic:
            message = self.__message
            if t=="/allSensors":
                #message['bn'] = '/'.join((self.clientID,self.sensorID,t))
                message['e'][0]['timestamp'] = str(time.time())
                message['e'][0]['value'] = hr
                message['e'][1]['timestamp'] = str(time.time())
                message['e'][1]['value'] = spo2
                message['e'][2]['timestamp'] = str(time.time())
                message['e'][2]['value'] = snooring


                self.client.myPublish(t,message)
                print("published")
            elif t== "/hr":
                #message['bn']= '/'.join((self.clientID,self.sensorID,t))
                message['e'][0]['timestamp'] = str(time.time())
                message['e'][0]['value'] = hr
                self.client.myPublish(t,message)
                print("published")

            elif t== "/spo2":
                message['e'][1]['timestamp'] = str(time.time())
                message['e'][1]['value'] = spo2
                self.client.myPublish(t,message)
                print("published")
            
            elif t== "/snooring ":
                message['e'][2]['timestamp'] = str(time.time())
                message['e'][2]['value'] = snooring
                self.client.myPublish(t,message)
                print("published")

    def start(self):
        self.client.start()

    def stop(self):
        self.client.stop()

if __name__ == "__main__":
    conf = json.load(open("settings.json"))
    broker = conf["broker"]
    port = conf["port"]
    sensor = MyPublisher(["/allSensors", "/hr",
                          "/spo2","/snooring"], "apnea", "sensor1",broker, port)
    sensor.start()
    while True:

        sensor.publish()
        time.sleep(59)
    sensor.stop()
    