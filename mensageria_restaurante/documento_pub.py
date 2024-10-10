#!/usr/bin/env python
import pika
import json
import time

# Conexão com o RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost',
                                   5672,
                                   '/',
                                   credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declaração da fila para pedidos
channel.queue_declare(queue='pedidos')

# Simulação do garçom enviando pedidos para a cozinha
i = 1
pratos = ["Hambúrguer", "Pizza", "Salada", "Sopa", "Lasanha", "Bife", "Sushi", "Tacos", "Macarrão", "Frango Assado"]

while(True):
    pedido = {"id": i, "prato": pratos[i % len(pratos)]}
    print(f"Garçom: Enviando pedido {pedido}")
    channel.basic_publish(exchange='', routing_key='pedidos', body=json.dumps(pedido).encode())
    print("[x] Pedido enviado para a cozinha")
    time.sleep(5)  # Simula o tempo entre pedidos
    i += 1
    if i == 10:
        break

connection.close()
