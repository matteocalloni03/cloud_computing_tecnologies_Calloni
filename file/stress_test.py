import sys
import boto3
import json
import random
import time
import uuid
from concurrent.futures import ThreadPoolExecutor

BUCKET_NAME = 'matteo-iot-stress-test-2024'
REGION = 'eu-south-1'
VALID_FILES = 300
CORRUPTED_FILES = 10
THREADS = 20 

s3_client = boto3.client('s3', region_name=REGION)

def upload_file(is_corrupted):
    file_name = f"telemetry/sensor_data_{uuid.uuid4()}.json"
    
    if is_corrupted:
        content = "ERRORE_SENSORE: Rilevazione fallita. Questo non è un JSON formattato!"
        print(f"[!] Invio file CORROTTO: {file_name}")
    else:
        content = json.dumps({
            "device_id": f"sensor_{random.randint(100, 999)}",
            "temperature": round(random.uniform(15.0, 65.0), 1)
        })
        print(f"[+] Invio file valido: {file_name}")

    try:
        s3_client.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=content)
    except Exception as e:
        print(f"Errore durante l'upload: {e}")

if __name__ == "__main__":
    print(f"--- INIZIO STRESS TEST ---")
    print(f"Target: s3://{BUCKET_NAME}")
    print(f"Preparazione di {VALID_FILES} file validi e {CORRUPTED_FILES} file corrotti...")
    
    tasks = [False] * VALID_FILES + [True] * CORRUPTED_FILES
    random.shuffle(tasks)
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(upload_file, tasks)
        
    end_time = time.time()
    print(f"\n--- TEST COMPLETATO ---")
    print(f"Inviati {len(tasks)} file in {round(end_time - start_time, 2)} secondi.")

input("\nPremi INVIO per chiudere la finestra...")
