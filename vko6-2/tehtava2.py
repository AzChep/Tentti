import argparse
import os
from azure.storage.blob import BlobClient
import time

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

def lataa_blubi():
      blob = BlobClient.from_connection_string(conn_str=connect_str, container_name="tentti", blob_name="checkpoint.txt")

      with open("checkpoint.txt", "wb") as my_blob:
            blob_data = blob.download_blob()
            blob_data.readinto(my_blob)

def tee_lista():
    try:
        with open("checkpoint.txt") as tiedosto:
    
            sanat1 = []

            for rivi in tiedosto:
                rivi = rivi.replace("\n", "")
                sanat1.append(rivi)
    except:
        print("virhus")

    sanat1.sort(key = len)
    return sanat1

def tulosta_haluttu(luku: int, lista: list):

    for i in range(luku):
        print(lista[i])

lataa_blubi()
time.sleep(5)

parser = argparse.ArgumentParser()
parser.add_argument("luku", help="montako riviä tulostetaan?")
args = parser.parse_args()

luku = args.luku

tulosta_haluttu(int(luku), tee_lista())

