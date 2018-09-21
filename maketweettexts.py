import json

'''
     Twitter object - Holds data we actually want
    (Used mainly to clean our data and reformat for future analysis)
'''
class twitter_entry:

    def __init__(self, _raw_text, _truncated, _fav_count, _source, _retweeted, _created_at, _lang, _retweets, _hashtags):
        self.raw_text = _raw_text
        self.truncated = _truncated
        self.fav_count = _fav_count
        self.source = _source
        self.retweeted = _retweeted
        self.created_at = _created_at
        self.lang = _lang
        self.retweets = _retweets
        self.hashtags = _hashtags

    ### Define the setter functions ###
    def set_raw_text(self,text):
        self.raw_text = text
    def set_truncated(self,trunc):
        self.truncated = trunc
    def set_fav_count(self,fav):
        self.fav_count = fav
    def set_source(self,sourc):
        self.source = sourc
    def set_retweeted(self,retweet):
        self.retweeted = retweet
    def set_created_at(self,at):
        self.created_at = at
    def set_lang(self,language):
        self.lang = language
    def set_retweets(self,retweet):
        if(retweet != 0):
            self.retweeted = True
        self.retweets = retweet
    # For setting the hashtags it will be initalizing a list
    def set_hashtags(self,current_tweet):
        hash_tag_list =[]
        hash_list = current_tweet['entities']['hashtags']
        for tag in hash_list:
            hold_value = tag['text']
            hash_tag_list.append(hold_value)
            #print (hold_value)
        self.hashtags = hash_tag_list
    ### END OF SETTER FUNCTIONS ###

    ### Defining the getter functions ###
    def get_raw_text(self):
        return self.raw_text
    def get_truncated(self):
        return self.truncated
    def get_fav_count(self):
        return self.fav_count
    def get_source(self):
        return self.source
    def get_retweeted(self):
        return self.retweeted
    def get_created_at(self):
        return self.created_at
    def get_lang(self):
        return self.lang
    def get_retweets(self):
        return self.retweets
    # For setting the hashtags it will be initalizing a list
    def get_hashtags(self):
        return self.hashtags
    ### END OF GETTER FUNCTIONS ###

    def print_tweet_data(self):
        ### Used for testing purposes
        print('------------------------------------------------------------------------')
        #Prints the text of the tweet
        print(self.get_raw_text())
        #Prints if the tweet was truncated
        #print(self.get_truncated())
        #Prints the number of favorites the tweet had
        print(self.get_fav_count())
        #Prints the source of the tweet
        #print(self.get_source())
        #Prints if the tweet was retweeted
        print(self.get_retweeted())
        #Prints when the tweet was created
        #print(self.get_created_at())
        #Prints the language of the tweet
        #print(self.get_lang())
        #Prints the number of retweets
        print(self.get_retweets())
        #Prints a list of the hashtags associated with the tweets
        #print(self.get_hashtags())
        print('------------------------------------------------------------------------')
'''
raw_text= models.CharField(max_length=350)
truncated = models.CharField(max_length=300)
fav_count = models.IntegerField(default=0)
source = models.CharField(max_length=50)
retweets = models.IntegerField(default=0)
created_at = models.DateTimeField('created at')
lang = models.CharField(max_length=10)
retweeted = models.BooleanField('retweeted')
hashtags = models.CharField(max_length=200)
'''

### END OF Twitter Entry Class ###

class TwitterJSONParser:

    def parse_data(self):
        data = []
        with open(self.file) as j:
            for tweet in j:
                tweeter = twitter_entry('test',0,0,0,0,0,0,0,0)
                current_tweet = json.loads(tweet)

                #Using Setter Functions to create an object for each tweet
                tweeter.set_raw_text(current_tweet['text'])
                #tweeter.set_truncated(current_tweet['truncated'])
                tweeter.set_fav_count(current_tweet['favorite_count'])
                tweeter.set_source(current_tweet['source'])
                tweeter.set_retweeted(current_tweet['retweeted'])
                #tweeter.set_created_at(current_tweet['created_at'])
                #tweeter.set_lang(current_tweet['lang'])
                tweeter.set_retweets(current_tweet['retweet_count'])
                #tweeter.set_hashtags(current_tweet)
                data.append(tweeter)

        return data

    def __init__(self, _JSON_file_name):
        self.file = _JSON_file_name
        self.tweets = self.parse_data()

    def get_data(self):
        return self.tweets

    def print_tweets(self):
        for tweet in self.tweets:
            tweet.print_tweet_data()
