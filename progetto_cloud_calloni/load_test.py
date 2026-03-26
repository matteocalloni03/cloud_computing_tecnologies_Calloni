import boto3
import uuid
import time
from concurrent.futures import ThreadPoolExecutor

BUCKET_NAME = 'progetto-cloud-calloni-input'  
NUM_FILES = 50

s3_client = boto3.client('s3')

def upload_dummy_file(file_number):
    file_content = f"Questo è il file di test numero {file_number} per l'esame di Cloud Computing."
    file_name = f"test_esame_{uuid.uuid4().hex[:8]}.txt"
    
    try:
        s3_client.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)
        print(f"Caricato: {file_name}")
    except Exception as e:
        print(f"Errore caricamento {file_name}: {e}")

print(f"Inizio caricamento di {NUM_FILES} file in parallelo su S3...")
start_time = time.time()

# Usa 10 thread in parallelo per stressare il sistema e generare eventi simultanei
with ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(NUM_FILES):
        executor.submit(upload_dummy_file, i)

print(f"Caricamento completato in {time.time() - start_time:.2f} secondi!")