import json
import boto3
import uuid
import time
from datetime import datetime

# Inizializza i client per i servizi AWS
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ProcessedFiles') 

def lambda_handler(event, context):
    # Log dell'evento ricevuto 
    print("Evento ricevuto:", json.dumps(event))

    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']
        file_size = record['s3']['object']['size']

        print(f"Elaborazione file: {file_key} dal bucket: {bucket_name}")

        # Simulazione di elaborazione
        # Creo un oggetto da salvare nel DB
        item = {
            'id': str(uuid.uuid4()),
            'filename': file_key,
            'size_bytes': file_size,
            'upload_time': datetime.now().isoformat(),
            'status': 'PROCESSED',
            'processed_by_lambda': context.function_name
        }

        # Scrittura su DynamoDB
        try:
            table.put_item(Item=item)
            print(f"Item salvato in DynamoDB: {item['id']}")
        except Exception as e:
            print(f"Errore scrittura DB: {str(e)}")
            raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Elaborazione completata con successo!')
    }
