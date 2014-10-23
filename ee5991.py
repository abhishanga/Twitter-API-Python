import twitter
import json
CONSUMER_KEY = '6DDkehPkroU1IYwB2DJIeOYuE'
CONSUMER_SECRET = '56sC9z6R4dmUtDbyBOsKolGLrPeyQHooj7TcDI3udJbzzvHYrK'
OAUTH_TOKEN = '117137313-3OqzlliamkfF1DrCF9gDfmnRbmhFGvSGsLqKiwXe'
OAUTH_TOKEN_SECRET = '8S8RRWfkSjcDk03ucCvFpvug7L7KUR9QczWQTtI4XFLGV'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print json.dumps(world_trends, indent=1)
print
print json.dumps(us_trends, indent=1)
