import requests
from dotenv import load_dotenv
import os


class connection:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv('BACK_URL')

    def make_post_call(self, endpoint, payload, headers=None): # payload es el cuerpo de la petición
        if headers is None:
            headers = {'Content-Type': 'application/json'}
        response = requests.post(f"{self.url}/{endpoint}", json=payload, headers=headers)
        return response.json().get("id")

    def make_put_call(self, endpoint, payload, headers=None): # payload es el cuerpo de la petición
        if headers is None:
            headers = {'Content-Type': 'application/json'}
        response = requests.put(f"{self.url}/{endpoint}", json=payload, headers=headers)
        return response.json().get('respuesta')
