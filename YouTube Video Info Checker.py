import time
from googleapiclient.discovery import build

# Build the service object
youtube = build('youtube', 'v3', developerKey='YOUR API KEY')

# Define the video ID and the channel ID
video_id = 'VIDEO ID'
channel_id = 'CHANNEL ID'

while True:
    # Make the API request to retrieve the video's statistics
    video_statistics = youtube.videos().list(id=video_id, part='statistics').execute()
    # Make the API request to retrieve the channel's statistics
    channel_statistics = youtube.channels().list(id=channel_id, part='statistics').execute()
    
    # Retrieve the view count, likes, and subscribers
    views = video_statistics['items'][0]['statistics']['viewCount']
    likes = video_statistics['items'][0]['statistics']['likeCount']
    subscribers = channel_statistics['items'][0]['statistics']['subscriberCount']
    
    # Print the view count, likes and subscribers
    print(f'Views: {views}, Likes: {likes}, Subscribers: {subscribers}')
    
    # Sleep for 60 seconds
    time.sleep(60)
