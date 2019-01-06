
class RunConfig:
    ckey="your-ckey"
    csecret="your-csecret"
    atoken="your-atoken"
    asecret="your-asecret"
    dbNameInit = 'twitter.db'
    tableName = 'Tweets'
    positiveNegativeThreshold = 0.001
    keyWords= ["Ukraine", "ukraine", "Poroshenko", "poroshenko"]
    #keyWords= ["Trump", "usa"]
    dbName = dbNameInit.split('.')[0]+"_".join(keyWords)+".db"

