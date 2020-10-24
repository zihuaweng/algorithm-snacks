# Designing Instagram

## Requirements
1. Upload / download / view photos
2. Search based on the photo / video titles
3. Follow other users
4. Generate news feed consisting of top photos from all the people the user follows

## Estimation

### Considerations and Assumption
    1. Read heavy
    2. Low latency is expected while viewing photos
    3. Data should be 100% reliable
    2. Assume we have 500M total users, with 1M daily active users
    3. 2M new photos every day, 23 new photos every second.
    4. Average photo file size => 200KB

### Estimation
    1. traffic estimates: 
        Queries Per Second (QPS) for read and write
    2. storage estimates: for 10 years
        - User storage
        - Photo storage
        - Follow storage
    3. bandwidth estimates: 
        read / write QPS * size(image) [200KB] 
    4. memory estimates: 
        If we follow the 80-20 rule, meaning 20% of URLs generate 80% of traffic, we would like to cache these 20% hot URLs. So we cache 20% of urls pre day

## API


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
1. Client, image hosting system, image storage, image metadata
2. Upload images is slow but read is fast. We could seperate photo upload and photo view/search to diff servers.


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


