from flask import Flask, render_template
import requests

app = Flask(__name__)

YOUTUBE_API_KEY = 'AIzaSyD3YtxM00R8LeGC0YXmrRyh4TEw2qc9EeQ'  # Replace with your actual API key
CHANNEL_ID = 'UCNTdQYhTtb13-IYKYCW0d1A'  # Your provided channel ID

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/latest_videos')
def latest_videos():
    url = f'https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=20'
    response = requests.get(url)
    data = response.json()
    videos = []
    for item in data['items']:
        video_info = {
            'title': item['snippet']['title'],
            'videoId': item['id']['videoId'],
            'thumbnail': item['snippet']['thumbnails']['medium']['url'],  # Get the medium size thumbnail
            'published_at': item['snippet']['publishedAt']
        }
        videos.append(video_info)
    return render_template('latest_videos.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
