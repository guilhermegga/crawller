from TwitterSearch import *
from textblob import TextBlob
import nltk

def buscaTweets():
    try:
        tso = TwitterSearchOrder()
        tso.set_keywords(['lula']) #palavras pra serem buscadas
        tso.set_language('pt') #linguagem de twites
        tso.set_include_entities(False)

        #chaves de acesso
        ts = TwitterSearch(
            consumer_key = 'xxxxxx',
            consumer_secret = 'xxxxxx',
            access_token = 'xxxxxx',
            access_token_secret = 'xxxxxxxx'
         )
        resultEncontrado = ts.search_tweets_iterable(tso)
        #percorrendo o que foi encontrado
        for tweet in resultEncontrado:
            # print('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text']))
            analisarFrase(tweet['text'])
    #exceção caso algo de errado aconteça
    except TwitterSearchException as e:
        print(e)
def analisarFrase(tweetOriginal):
    blob = TextBlob(tweetOriginal)
    traducao = blob.translate(to='en')
    tweetMod = TextBlob(str(traducao))
    print('Tweet original:{0}'.format(tweetOriginal))
    print('Tweet traduzido:{0} \nSentimento: {1}\n\n----\n'.format(str(traducao),tweetMod.sentiment_assessments))




buscaTweets()
