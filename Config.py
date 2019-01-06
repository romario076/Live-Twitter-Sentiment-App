
class RunConfig:
    ckey="7Q26tbTPi6W0HhNT93t1yBZI4"
    csecret="rHzSrzXiVKvTBeYxmcQv8b5fUHvW0SGvbHgJKlIHXwvKNdgjdM"
    atoken="181176256-tTWjmvyVkeOdX5UpsE5xvQAsq98au2gDWNXn9VHK"
    asecret="HgFNRhrL4jCGzoMN5JOyGaMry9T5nn1ity5HAN0mcPfg9"
    dbNameInit = 'twitter.db'
    tableName = 'Tweets'
    positiveNegativeThreshold = 0.001
    keyWords= ["Ukraine", "ukraine", "Poroshenko", "poroshenko"]
    #keyWords= ["Trump", "usa"]
    dbName = dbNameInit.split('.')[0]+"_".join(keyWords)+".db"

