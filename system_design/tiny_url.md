# Designing a URL Shortening service like TinyURL

## Requirements
1. Given an url -> unique alias, easy to remember
2. Redirect user to the original link
3. Users are allowed to customize the tiny link
4. link will expire after a timespan, users are allowed to specify the expiration time

## Estimation

### Considerations and Assumption
    1. read heavy
    1. read heavy
    2. assume read: write = 100:1
    3. 500 M new URL per month

### Estimation
    1. traffic estimates: 
        Queries Per Second (QPS) for view / upload : 2M new photos every day, 23 new photos every second.
    2. storage estimates: 
        storage for 1 dya, 10 years
    3. bandwidth estimates: 
        read / write QPS * size(photo) [200KB] 
    4. memory estimates

## API
```python
# log in to get user_token

create_url(user_token: str, original_url: str, custom_alias: str = '', user_name: str = '', expire_date: str = '') -> str

# user_token (string): The API developer key of a registered account. This will be used to, among other things, throttle users based on their allocated quota.
get_url(user_token: str, short_url: str) -> long_url
delete_url(user_token: str, url_key: str) -> bool

```

To prevent abuse, we can limit users via their api_dev_key. Each api_dev_key can be limited to a certain number of URL creations and redirections per some time period (which may be set to a different duration per developer key). 


## Database Design
### Database Schema
1. url mapping
    - table name: Url
    - pk: url_id (UUID, varchar16)
    - original_url (varchar512), creation_date (datetime), expiration_date (datetime), user_id(varcchar) 
2. user data
    - table name: User
    - pk: user_id (UUID, varchar)
    - name (varchar), email (varchar), creation_date (datetime), last_login (datetime)

### what database to use
We don’t need to use relationships between objects – a NoSQL store like DynamoDB, Cassandra or Riak is a better choice. A NoSQL choice would also be easier to scale. Please see SQL vs NoSQL for more details.


## Basic system design & algorithm
### encoding url
    1. unique hashing code (MD5 128bit 21 char / SHA256)
    2. Base64 encoding  ('A-Z', 'a-z', '0-9', '_', '-')
    3. Would generate same url for diff people. solution: add an incresing number or hash with user id

### generate url offline

1. Key Generation Service (KGS), take already generated key and use it
2. A used key table, a new key table, and add some keys to cache/ memory
3. get key from memory and move it to the used key table

## Data Partitioning and Replication
1. Stored url to diff table based on the prefix -> lead to unbalance db server
2. Data sharding & consistent hashing

## Cache
1. Starts with storing 20% of the urls
2. Eviction policies: LRU
3. update cache

## Load Balancer
1. Clients - Application server
2. Application server - database server
3. Application server - cache server


## Purging and db cleanup