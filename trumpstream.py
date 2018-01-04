import tweepy
import json
data_dir = "data/"
auth_data = {}
with open("notebooks/credentials.json", "r") as credentials:
    auth_data = json.load(credentials)
auth = tweepy.OAuthHandler(auth_data["consumer_key"], auth_data["consumer_secret"])
auth.set_access_token(auth_data["access_token"], auth_data["access_token_secret"])
api = tweepy.API(auth)

class WriteStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        with open(data_dir + str(status.id) + ".json", "w") as outfile:
            json.dump(status._json, outfile)
            print "@" + status.user.screen_name + ": " + status.text
            print json.dumps(status._json)

stream_listener = WriteStreamListener()
stream = tweepy.Stream(auth = api.auth, listener=stream_listener)
stream.filter(track=['to:realDonaldTrump,@realDonaldTrump'])
