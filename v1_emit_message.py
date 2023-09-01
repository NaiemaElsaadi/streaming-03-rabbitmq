"""
    This program sends a message to a queue on the RabbitMQ server.

    Naiema Elsaadi
    Date: August 30, 2023

"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# use the connection to create a communication channel
channel = connection.channel()
# use the channel to declare a queue
channel.queue_declare(queue="hello")
#Define the message you want to send
message = 'Hi! My name is Naiema!'
# use the channel to publish a message to the queue
channel.basic_publish(exchange='', routing_key='hello', body=message)
# print a message to the console for the user
print(" [x] Sent " + message)
# close the connection to the server
connection.close()