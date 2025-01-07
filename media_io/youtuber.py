import os, json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd


yt = build('youtube', 'v3', developerKey=os.environ["YOUTUBE_API_KEY"])

def get_video_ids(channel_id, n_results=50):
    print("Getting video ids")
    video_data = []
    try:
        request = yt.search().list(
            part="id,snippet",
            channelId=channel_id,
            maxResults=n_results,
            order="date"
        )
        response = request.execute()
        print(json.dumps(response, indent=4))
        for item in response['items']:
            if item['id']['kind'] == 'youtube#video':
                print(item)
                video_data.append({
                    'video_id': item['id']['videoId'],
                    'published_at': item['snippet']['publishedAt']
                })
    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
    return video_data

def get_transcripts(video_data, lang="pt"):
    data = []
    not_working = 0
    for video in video_data:
        video_id = video['video_id']
        published_at = video['published_at']
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
            for item in transcript:
                data.append({
                    'video_id': video_id,
                    'published_at': published_at,
                    'text': item['text'],
                    'start': item['start'],
                    'duration': item['duration']
                })
        except Exception as e:
            not_working += 1
            print(f"An error occurred for video {video_id}: {e}")
        
    return data

if __name__ == "__main__":
    # Get All Video IDs by Channel ID with N Results
    channels = [
        ("UCUyeluBRhGPCW4rPe_UvBZQ", "mbl"),
    ]
    # N Videos per channel
    n_videos = 10

    for channel_id, channel_name in channels:
        # Get Ids and Transcripts data
        video_data = get_video_ids(channel_id, n_results=n_videos)
        data = get_transcripts(video_data)

        # Save data to CSV and Join transcripts
        df = pd.DataFrame(data)
        df_grouped = df.groupby('video_id')['text'].apply(' '.join).reset_index()
        df_grouped = df_grouped.merge(df[['video_id', 'published_at']].drop_duplicates(), on='video_id')
        print(df_grouped)
        df.to_csv(f'transcripts_{channel_id}.csv', index=False)
        df_grouped.to_csv(f'grouped_transcripts_{channel_name}.csv', index=False)
