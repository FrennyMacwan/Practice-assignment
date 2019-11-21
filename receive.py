# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:46:33 2019

@author: frenny
"""

#!/usr/bin/env python
import pika
from datetime import datetime


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='meter_power')

PV= 100

def callback(ch, method, properties, body):
    print(" Received %d" % int(body))
    with open("output.txt", "a") as f:
        f.write("Time:%s Meter Power:%d PV Power:%d total Power(meter+PV): %d \n" % (str(datetime.now()),  int(body), PV,int(body)+PV))
    
channel.basic_consume(
    queue='meter_power', on_message_callback=callback, auto_ack=True)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()