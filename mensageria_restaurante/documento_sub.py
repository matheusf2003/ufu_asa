#!/usr/bin/env python
import pika
import sys
import os
import time
import json
from fpdf import FPDF

# Função para processar o pedido e gerar o PDF
def preparar_prato(pedido):
    print("Cozinha: Recebido o pedido")
    print(f" [x] Pedido: {pedido}")
    data = pedido.decode('utf-8')

    # Convertendo os dados para JSON
    json_data = json.loads(data)
    print(f"Preparando o prato: {json_data['prato']} (ID do pedido: {json_data['id']})")

    # Simulando o tempo de preparo do prato
    time.sleep(5)
    print(f"Cozinha: O prato '{json_data['prato']}' está pronto!\n")

    # Criando o arquivo PDF com as informações do pedido
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"ID do pedido: {json_data['id']}", ln=1, align="C")
    pdf.cell(200, 20, txt=f"Prato: {json_data['prato']}", ln=2, align="C")
    
    # Salvando o arquivo PDF em uma pasta específica
    caminho_arquivo = os.path.join("/home/mth/Documentos/asa/mensageria_restaurante/src/pedidos.pdf")
    pdf.output(caminho_arquivo)
    print(f"Cozinha: PDF gerado para o pedido {json_data['id']}: {caminho_arquivo}")

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost',
                                           5672,
                                           '/',
                                           credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declaração da fila de pedidos
    channel.queue_declare(queue='pedidos')

    # Callback que processa o pedido
    def callback(ch, method, properties, body):
        preparar_prato(body)

    # Cozinha esperando os pedidos
    channel.basic_consume(queue='pedidos', on_message_callback=callback, auto_ack=True)

    print(' [*] Cozinha aguardando pedidos. Para sair, pressione CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Programa interrompido')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
