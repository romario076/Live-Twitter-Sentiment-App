from Config import RunConfig

class TweetsSideCounter(object):
    def __init__(self):
        self.positiveCount = 0
        self.negativeCount = 0
        self.neutralCount = 0
        self.positiveNegativeThreshold = RunConfig.positiveNegativeThreshold

    def update(self, polarity):
        if polarity>0:
            if polarity>=self.positiveNegativeThreshold:
                self.positiveCount = self.positiveCount + 1
            else:
                self.neutralCount = self.neutralCount + 1
        elif polarity<0:
            if polarity<=-self.positiveNegativeThreshold:
                self.negativeCount = self.negativeCount + 1
            else:
                self.neutralCount = self.neutralCount + 1
        else:
            self.neutralCount = self.neutralCount + 1