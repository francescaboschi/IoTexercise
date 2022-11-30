import random
import json
from MyMQTT import *
import time

class MySubscriber:
	def __init__(self,topic,clientID,broker,port):
		self.clientID=clientID
		self.topic=topic
		self.client=MyMQTT(clientID,broker,port,self)
	def run(self):
		self.client.start()
		print('{} has started'.format(self.clientID))
		self.client.mySubscribe(self.topic)
	def end(self):
		self.client.stop()
		print('{} has stopped'.format(self.clientID))
	
	def notify(self,topic,msg):
		message=json.loads(msg) #? che fa
		value_hr = message['e'][0]['value']
		unit_hr = message['e'][0]['unit']
		time_hr = message['e'][0]['timestamp']
		value_spo2 = message['e'][1]['value']
		unit_spo2 = message['e'][1]['unit']
		time_spo2 = message['e'][1]['timestamp']
		value_snoor = message['e'][2]['value']
		unit_snoor = message['e'][2]['unit']
		time_snoor = message['e'][2]['timestamp']

		
		if topic == "/allSensors":
			print(f'{self.clientID} heart rate : {value_hr} {unit_hr} at time {time_hr}, \n  Sp02 : {value_spo2} {unit_spo2} at time {time_spo2}, \n snooring : {value_snoor} {unit_snoor} at time {time_snoor}')

		elif topic == "/hr":
			print(f'{self.clientID} heart rate : {value_hr} {unit_hr} at time {time_hr}.')

		elif topic == "/spo2":
			print(f'{self.clientID} Sp02 : {value_spo2} {unit_spo2} at time {time_spo2}')

		elif topic== "/snooring ":
			print(f'{self.clientID} snooring : {value_snoor} {unit_snoor} at time {time_snoor}')
		else:
			print('command error')


if __name__ == '__main__':
	conf=json.load(open("settings.json"))
	broker=conf["broker"]
	port=conf["port"]
	
	choice=''
	while choice!='q':
		print("What kind of data you want to retrieve")
		print("\thr: heart rate")
		print("\tspo2: sp02")
		print("\tsnoor: snooring")
		print("\tb: both")
		print("\tq: quit")

		
		choice=input()
		if choice=='q':
			break	
		if choice=='hr':
			topic = "/hr"
			break
		elif choice=='spo2':
			topic = "/spo2"
			break
		elif choice=='snoor':
			topic="/snooring"
			break
		elif choice=='b':
			topic = "/allSensors"
			break

	
	test = MySubscriber(topic,"apnea",broker,port)
	test.run()
	while True:
		time.sleep(1)

	test.end()