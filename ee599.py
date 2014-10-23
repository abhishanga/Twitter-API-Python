from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = '6DDkehPkroU1IYwB2DJIeOYuE'
csecret = '56sC9z6R4dmUtDbyBOsKolGLrPeyQHooj7TcDI3udJbzzvHYrK'
atoken = '117137313-3OqzlliamkfF1DrCF9gDfmnRbmhFGvSGsLqKiwXe'
asecret = '8S8RRWfkSjcDk03ucCvFpvug7L7KUR9QczWQTtI4XFLGV'

class listener(StreamListener):

    def on_data(self, data):
        try:
            #print data
            tweet = data.split(',"text":"')[1].split('","source')[0]
            print tweet
            saveThis  = str(time.time())+'::'+tweet
            saveFile = open('twitDB2.csv','a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed ondata,',str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
