import os
import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

# Substitua 'YOUR_API_KEY' pela sua chave de API do YouTube
API_KEY = 'AIzaSyDBArxwCnLhK4YsmholYUvYl88K1tqVMsI'
VIDEO_ID = 'lir3dzYIhz0'

def get_video_details(api_key, video_id):
    # Cria o cliente da API do YouTube
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Faz a requisição à API para obter detalhes do vídeo
    request = youtube.videos().list(
        part='snippet,contentDetails,statistics',
        id=video_id
    )
    response = request.execute()
    
    return response

def pretty_print_json(json_data):
    # Formata a saída JSON com espaçamento e quebra de linha
    formatted_json = json.dumps(json_data, indent=4)
    
    # Substitui \n por quebras de linha reais
    formatted_json = formatted_json.replace('\\n', '\n')
    
    print(formatted_json)

if __name__ == '__main__':
    video_details = get_video_details(API_KEY, VIDEO_ID)
    pretty_print_json(video_details)
