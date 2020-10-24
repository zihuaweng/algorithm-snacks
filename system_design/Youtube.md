# Designing Youtube

## Requirements
1. Upload video
2. Share and view video
3. Search based on video title
4. Record like/dislike/num of view of the video
5. Add and view comments

## Estimation

### Considerations and Assumption

### Estimation

## API
```python
Response(data, status=None, template_name=None, headers=None, content_type=None)

upload_video(api_dev_key: str, video_title: str, video_description: str, tags: List[str], category_id: str, default_language: str, recording_details: str, video_contents: str) -> Response

upload_video(api_dev_key: str, search_query: str, maximum_videos_to_return: str, page_token: str) -> Response

stream_video(api_dev_key: str, video_id: str, offset: int, codec: str, resolution: str)
```

## Database Design
### Database Schema
1. Photos
    - table name: Photo
    - pk: photo_id (UUID, varchar16)
    - user_id (int), photo_path (varchar), photo_latitude (int), photo_longtitude (int), user_latitude (int), user_longtitude (int), create_date (datetime)
2. User data
    - table name: User
    - pk: user_id (UUID, varchar)
    - name (varchar), email (varchar), date_of_birth (datetime), creation_date (datetime), last_login (datetime)
3. User follow
    - table name: user_follow
    - pk: user_id_1, user_id_2

### what database to use
1. Photos: store in distributed file storage like HDFS or S3
2. User data and user follow: wide-column datastore like Cassandra, 


## High Level System Design
1. Processing queue: push uploaded video to the queue
2. Encoder: encode video
3. Thumbnails generator: To generate a few thumbnails for each video.
4. Video and Thumbnail storage: To store video and thumbnail files in some distributed file storage.
5. User Database: To store user’s information, e.g., name, email, address, etc.
6. Video metadata storage: A metadata database to store all the information about videos like title, file path in the system, uploading user, total views, likes, dislikes, etc. It will also be used to store all the video comments.


## Reliability and Redundancy
If we want to have high availability of the system, we need to have multiple replicas of services running in the system so that even if a few services die down, the system remains available and running. Redundancy removes the single point of failure in the system.


## Data Sharding
1. Partitioning based on user_id, 1 shards is 1 TB, keep 10 shards. Each DB shard can have its own auto-increment sequence for PhotoIDs.
    - non-uniform distribution of storage
    - might nore store all pictures of a user
    - unavailability of all the user's data if one shard is down
2. Partitioning based on picture_id, 

## Ranking and News Feed Generation
1. Fetch 100 photos from all user following
2. Rank the top 100 photos
3. Have dedicated servers continuously generating users' News Feeds and store them to the table
4. First fetch data from the table and generate new feeds that time onwards

### Approaches for Sending News Feed contents to the users
1. Pull. Get as needed. Might result in empty response if now new data.
2. Push. Server pushes data as soon as it is available. Huge wordload if the user has a lot followers.
3. Hybrid. We can move all the users who have a high number of follows to a pull-based model and only push data to those users who have a few hundred (or thousand) follows.

## Cache and Load balancing
1. Add cache for metadata server, cache data before hitting the database. 
2. Use LRU as eviction policy
3. Store 20% of the daily read volumn of photos


