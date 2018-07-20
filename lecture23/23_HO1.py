import pprint
import sys
from apiclient.discovery import build

api_key = 'AIzaSyD98gfsIrWUvyuVjmuuEOLKrle-SLHZ1bU'

youtube = build('youtube', 'v3', developerKey = api_key)

search_response = youtube.search().list( q = 'Karelin', part = 'id,snippet', maxResults = 10).execute()

videos = []
channels = []
playlists = []
comments = []

for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
        videos.append('%s (%s)' %
                      (search_result['snippet']['title'], search_result['id']['videoId']))
        
    elif search_result['id']['kind'] == 'youtube#channel':
        channels.append('%s (%s)' %
                        (search_result['snippet']['title'], search_result['id']['channelId']))
        
    elif search_result['id']['kind'] == 'youtube#playlist':
        playlists.append('%s (%s)' %
                        (search_result['snippet']['title'], search_result['id']['playlistId']))
        
    elif search_result['id']['kind'] == 'youtube#comment':
        channels.append('%s (%s)' %
                        (search_result['snippet']['title'], search_result['id']['playlistId']))
        
print 'Videos:\n', '\n'.join(videos).encode('UTF-8'), '\n'
print 'Channels:\n', '\n'.join(channels).encode('UTF-8'), '\n'
print 'Playlists:\n', '\n'.join(playlists).encode('UTF-8'), '\n'

results = youtube.commentThreads().list(
        part = 'snippet',
        videoId = 'LLU7uH45p1I',
        textFormat = 'plainText'
        ).execute()

for item in results['items']:
    comment = item['snippet']['topLevelComment']
    author = comment['snippet']['authorDisplayName']
    text = comment['snippet']['textDisplay']
    likes = comment['snippet']['likeCount']
    
    print 'Comment by %s: %s, %i' % (author.encode('UTF-8'), text.encode('UTF-8'), likes)