from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['opendata']) # let's define all words we would like to have a look for
    tso.set_language('es') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = "pILHVEWLnRfXlWSqkeX3UgVkB",
        consumer_secret = "LxqCrw6xA0EHtRiZyooDJVLSZlSdy5J9PjflUun6qQyELJqrfw",
        access_token = "268051002-DTkRXkesXuguiVkdrn8dNJ81gHK9RWzPpcujEqCe",
        access_token_secret = "vFlaphycI9CMUnkd6nTove98qP2TRpfWHIvVHKgA2FSEI"
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
