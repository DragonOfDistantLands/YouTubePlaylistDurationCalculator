#!/usr/bin/env python
# coding: utf-8

# In[4]:


from googleapiclient.discovery import build
import isodate

def get_playlist_total_duration(api_key, playlist_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get all video ids in the playlist
    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=50,
        playlistId=playlist_id
    )
    response = request.execute()
    video_ids = [item['contentDetails']['videoId'] for item in response['items']]

    # Get details of videos
    request = youtube.videos().list(
        part="contentDetails",
        id=",".join(video_ids)
    )
    response = request.execute()
    total_duration = 0
    for item in response['items']:
        duration = isodate.parse_duration(item['contentDetails']['duration'])
        total_duration += duration.total_seconds()

    return total_duration

api_key = 'YOUR_API_KEY'  # Replace with your API key
playlist_id = input("Please enter the playlist ID: ")
total_duration = get_playlist_total_duration(api_key, playlist_id)
hours, remainder = divmod(total_duration, 3600)
minutes, seconds = divmod(remainder, 60)

# Print only the total duration
print(f"Total time = {int(hours)} Hours {int(minutes)} Minutes {int(seconds)} Seconds")


# In[ ]:




