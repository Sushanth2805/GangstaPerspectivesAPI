import requests
import streamlit as st

# Access the API key from Streamlit secrets
YOUTUBE_API_KEY = st.secrets["YOUTUBE_API_KEY"]
CHANNEL_ID = 'UCNTdQYhTtb13-IYKYCW0d1A'

# Streamlit app title
st.title('YouTube Notification Website')

# Fetch the latest videos from the YouTube API
def fetch_latest_videos(channel_id, api_key, max_results=10):
    url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults={max_results}'
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
    return videos

# Display the latest videos in the Streamlit app
videos = fetch_latest_videos(CHANNEL_ID, YOUTUBE_API_KEY)

st.header("Latest Videos")
for video in videos:
    st.subheader(video['title'])
    st.image(video['thumbnail'], width=300)
    st.write(f"Uploaded on: {video['published_at']}")
    st.markdown(f"[Watch on YouTube](https://www.youtube.com/watch?v={video['videoId']})")

st.markdown("[Go back to the top](#youtube-notification-website)")
