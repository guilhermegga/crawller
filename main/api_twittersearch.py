from TwitterSearch import *

def buscaTweets():
    try:
        tso = TwitterSearchOrder()
        tso.set_keywords(['lula']) #palavras pra serem buscadas
        tso.set_language('pt') #linguagem de twites
        tso.set_include_entities(False)

        #chaves de acesso
        ts = TwitterSearch(
            consumer_key = '3OKAOOEoPlJ5aQKR3ZII5OQGY',
            consumer_secret = 'IdfwEWchz8Mv468pklbb06px08lpDKHYHMEGSKpuLWYjtD1pMa',
            access_token = '296608449-ngjTc7kHu4hZpw5GD4KSwZvLd5mZ1VRecYNkEr9m',
            access_token_secret = 'Rn7NeeCWTcL4Ux0dHx4diRGt0o7pHwCsS2Q4gnyz1GOyG'
         )
        resultEncontrado = ts.search_tweets_iterable(tso)
        #percorrendo o que foi encontrado
        for tweet in resultEncontrado:
            # print('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text']))
            print(tweet)

    #exceção caso algo de errado aconteça
    except TwitterSearchException as e:
        print(e)


buscaTweets()