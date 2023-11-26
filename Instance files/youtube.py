import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd
import s3fs
import api_key

def youtube_comments():
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key.DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId="cbVUIbeVfhQ",
        maxResults=200
    )
    response = request.execute()

    data =[]
    for item in response['items']:
        get  = item['snippet']['topLevelComment']['snippet']
        data.append([get['authorDisplayName'], get['textOriginal'], get['likeCount'], get['publishedAt'], get['updatedAt']])
        
    columns = ['Username','Comment','Likes','Commented_on','Updated_on']

    df = pd.DataFrame(data,columns=columns)

    #writes the file in S3 bucket
    df.to_csv("s3://testing414/youtube_comments.csv", index=False)
    