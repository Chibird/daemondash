import tweepy

# Authentication details. To  obtain these visit dev.twitter.com
access_token = "1849293439-HsCAy8sNftuuZYFG47X0CCmyK9pvfY4dixFUanH"
access_token_secret = "wPrD23Gf5yUyWJvzh0g5UpetAb8FhRlMWcShyrqa7ptDl"
consumer_key = "ybav8hpAJRxlCt3AFXTyzq6CN"
consumer_secret = "ApG56qNb1Y5C4BJF8xOVzBh2dIOCv5eIvLHIyFA5LXTAl8YPbx"

if __name__ == '__main__':
    # Create authentication token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    # Get information about the user    
    user = api.get_user(raw_input('Enter a username: '))
    c = eval(raw_input('Number of tweets?: '))
    timeline = api.user_timeline(user.id, include_rts=True, count=c)
    for tweet in timeline:
        print (tweet.text)
