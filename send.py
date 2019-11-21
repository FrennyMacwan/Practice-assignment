# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:39:00 2019

@author: frenny
"""

import pika
import random
import time


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='meter_power')

while (True):
    a = random.randint(0, 9000)
    channel.basic_publish(exchange='',
                      routing_key='meter_power',
                      body= str(a))
    print(a)
    time.sleep(2)


connection.close()