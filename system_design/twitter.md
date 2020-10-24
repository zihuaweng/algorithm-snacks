# Designing Twitter

## Requirements
1. Post new tweets
2. Follw users
3. Mark tweets favorite
4. Create and display a timeline consisting of top tweets from all the people the user follows
4. Tweets can contain photos and videos

## Estimation

### Considerations and Assumption
    1. Read heavy
    2. Assume we have 1B users, 200M daily active users, 100M new tweets/day, each user follows 200 users

### Estimation
    2. storage estimates: for 10 years
        Tweets + users
    3. bandwidth estimates: 
        read / write QPS * size(text: 280 bytes, image: 200KB, video: 2M)
    4. memory estimates: 
        If we follow the 80-20 rule, meaning 20% of URLs generate 80% of traffic, we would like to cache these 20% hot URLs. So we cache 20% of urls pre day

## API
```python
Response(data, status=None, template_name=None, headers=None, content_type=None)

tweet(api_dev_key: str, tweet_data: str, tweet_location: str, user_location: str, media_ids: List[str]) -> Response

```

## Database Design
### Database Schema
1. Tweet
    - table name: Tweet
    - pk: tweet_id (UUID, varchar16)
    - user_id (verchar), content (text), tweet_latitude (int), tweet_longtitude (int), user_latitude (int), user_longtitude (int), creation_date (datetime), num_favorites (int)
2. User data
    - table name: User
    - pk: user_id (UUID, varchar)
    - name (varchar), email (varchar), date_of_birth (datetime), creation_date (datetime), last_login (datetime)
3. User follow
    - table name: UserFollow
    - pk: user_id_1, user_id_2
4. Favorite
    - table name: Favrite
    - pk: tweet_id, user_id
    - creation_date (datetime)

### what database to use
1. Tweet: store in distributed file storage like HDFS or S3
2. User data, user follow, Favorite: wide-column datastore like Cassandra, 


## High Level System Design
1. Client, application servers, load balancer, file storage, database


## Data Sharding
1. Sharding based on UserID
2. Sharding based on TweetID

