import twitter
import json
from prettytable import PrettyTable
from collections import Counter
CONSUMER_KEY = '6DDkehPkroU1IYwB2DJIeOYuE'
CONSUMER_SECRET = '56sC9z6R4dmUtDbyBOsKolGLrPeyQHooj7TcDI3udJbzzvHYrK'
OAUTH_TOKEN = '117137313-3OqzlliamkfF1DrCF9gDfmnRbmhFGvSGsLqKiwXe'
OAUTH_TOKEN_SECRET = '8S8RRWfkSjcDk03ucCvFpvug7L7KUR9QczWQTtI4XFLGV'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)
q = '#India' 

count = 100

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

status_texts = [ status['text'] 
                 for status in statuses ]

screen_names = [ user_mention['screen_name'] 
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text'] 
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]
# Compute a collection of all words from all tweets
words = [ w 
          for t in status_texts 
              for w in t.split() ]

for label, data in (('Word', words), 
                    ('Screen Name', screen_names), 
                    ('Hashtag', hashtags)):
    pt = PrettyTable(field_names=[label, 'Count']) 
    c = Counter(data)
    [ pt.add_row(kv) for kv in c.most_common()[:10] ]
    pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
    print pt
