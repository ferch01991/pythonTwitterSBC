import twitter, csv, json
from twitter import *
apiTwitter = twitter.Api(consumer_key="Qo46To2vlET5P5PS3KU69LDI1", 
						 consumer_secret="jaTghzMO8RUGvB8hdmfUxJZ5zrebmTnTcKyfxGEOUdnqjgyxGX", 
						 access_token_key="220199635-602fbt5TMjfJOx08hHcRnTkGIhOGowAC89nzE11R", 
						 access_token_secret="MefFBekMOTJGvJ6W2a64XI0znSR8tiVx1iUeVXaJw6Se2")


query = apiTwitter.GetSearch("#LOJA", count=200)
csvDatos = csv.writer(open("twees.csv", "wb"))
csvDatos.writerow(["Texto","Fecha","NumeroFavoritos","Idioma","Retweets","Cuenta", "Entidades"])
i = 0
for result in query:
	i = i+1
	print i
	print result.user.screen_name
	print result.created_at
	#csvDatos.writerow([(result.text).encode('utf-8').strip(), 
	#					result.created_at,result.favorite_count,
	#					result.lang,result.retweet_count,result.user.screen_name])

