from flask import Flask, render_template
import requests
import streamlit as st

app = Flask(__name__)

# Load the API key from the Streamlit secrets
YOUTUBE_API_KEY = st.secrets["YOUTUBE_API_KEY"]
CHANNEL_ID = 'UCNTdQYhTtb13-IYKYCW0d1A'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/latest_videos')
def latest_videos():
    url = f'https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=10'
    response = requests.get(url)
    data = response.json()
    videos = []
    for item in data['items']:
        video_info = {
            'title': item['snippet']['title'],
            'videoId': item['id']['videoId'],
            'thumbnail': item['snippet']['thumbnails']['medium']['url'],
            'published_at': item['snippet']['publishedAt']
        }
        videos.append(video_info)
    return render_template('latest_videos.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
