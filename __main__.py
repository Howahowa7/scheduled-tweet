import tweepy

def main(dict):
    consumer_key = dict['CONSUMER_KEY']
    consumer_secret = dict['CONSUMER_SECRET']
    access_token = dict['ACCESS_TOKEN']
    access_token_secret = dict['ACCESS_TOKEN_SECRET']
    tweet_text = dict['TWEET_TEXT']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    result = api.update_status(tweet_text)

    return result._json
