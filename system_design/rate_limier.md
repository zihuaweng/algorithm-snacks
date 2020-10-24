# Designing Rate Limiter

## Requirements
1. Limit the number of request to API within a time window, eg: 15 request/sec
2. Access throught cluseter. Support distributed system

## Different Type of Rate Limiter
1. Hard Throttling
2. Soft Throttling
3. Elastic or Dynamic Throttling

## Different Type of ALgorithms
1. Fixed Window Algorithm
2. Rolling Window Algorithm

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
1. request -> web server -> rate limiter -> web server


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


