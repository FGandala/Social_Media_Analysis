from googleapiclient.discovery import build

# Substitua 'YOUR_API_KEY' pela sua chave de API
api_key = 'AIzaSyDBArxwCnLhK4YsmholYUvYl88K1tqVMsI'

# Crie o serviço YouTube
youtube = build('youtube', 'v3', developerKey=api_key)

# ID do canal que você deseja obter os dados
channel_id = 'UCAayZDDj3uom0QpSJiwLoUw'  # Exemplo: Canal do Google Developers

# Faça a solicitação para obter os dados do canal
request = youtube.channels().list(
    part='snippet,contentDetails,statistics',
    id=channel_id
)

response = request.execute()

# Exiba os dados do canal
for item in response['items']:
    channel_id = item['id']
    username = item['snippet'].get('customUrl', 'N/A')
    name = item['snippet']['title']
    creation_date = item['snippet']['publishedAt']
    description = item['snippet']['description']
    view_count = item['statistics']['viewCount']
    image_url = item['snippet']['thumbnails']['default']['url']
    subscriber_count = item['statistics'].get('subscriberCount', 'N/A')
    country = item['snippet'].get('country', 'N/A')
    video_count = item['statistics']['videoCount']
    uploads_playlist_id = item['contentDetails']['relatedPlaylists']['uploads']

    # Obtenha as playlists do canal
    playlists_request = youtube.playlists().list(
        part='snippet',
        channelId=channel_id,
        maxResults=50
    )
    playlists_response = playlists_request.execute()

    playlists = []
    for playlist in playlists_response['items']:
        playlists.append({
            'title': playlist['snippet']['title'],
            'id': playlist['id']
        })

    # Obtenha os uploads recentes
    uploads_request = youtube.playlistItems().list(
        part='snippet',
        playlistId=uploads_playlist_id,
        maxResults=5  # Número de uploads recentes a serem exibidos
    )
    uploads_response = uploads_request.execute()

    recent_uploads = []
    for video in uploads_response['items']:
        recent_uploads.append({
            'title': video['snippet']['title'],
            'videoId': video['snippet']['resourceId']['videoId']
        })

    # Exiba os dados do canal
    print(f"ID: {channel_id}")
    print(f"Username: {username}")
    print(f"Name: {name}")
    print(f"Creation Date: {creation_date}")
    print(f"Description: {description}")
    print(f"View Count: {view_count}")
    print(f"Image URL: {image_url}")
    print(f"Subscriber Count: {subscriber_count}")
    print(f"Country: {country}")
    print(f"Video Count: {video_count}")
    print("Playlists:")
    for playlist in playlists:
        print(f"  - {playlist['title']} (ID: {playlist['id']})")
    print("Recent Uploads:")
    for upload in recent_uploads:
        print(f"  - {upload['title']} (Video ID: {upload['videoId']})")

