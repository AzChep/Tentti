import os
from azure.storage.blob import BlobServiceClient, __version__, BlobClient
import requests
import time

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

def suorita():
    haeJson()
    luo_blob("tentti")
    time.sleep(15)
    uppaa_blubi()

def haeJson():

    haku = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')

    file = haku.json()

    with open("checkpoint.txt", "w") as tiedosto:
        for arvo in file['items']:
            tiedosto.write(arvo['parameter']+"\n")


def luo_blob(nimi: str):
    
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = str(nimi)
    container_client = blob_service_client.create_container(container_name)

def uppaa_blubi():
      
    blob = BlobClient.from_connection_string(conn_str=connect_str, container_name="tentti", blob_name="checkpoint.txt")
    with open("checkpoint.txt", "rb") as data:
            blob.upload_blob(data)


if __name__ == "__main__":
    suorita()