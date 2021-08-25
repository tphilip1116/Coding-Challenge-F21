from nltk.sentiment import SentimentIntensityAnalyzer

with open('input.txt','r') as f:
    lines = f.readlines()

sia = SentimentIntensityAnalyzer()

lineNum = 0
sentimentScore = 0
for x in lines:
    lineNum = lineNum + 1
    print(lineNum, ": ", sia.polarity_scores(x).get('compound'))
    sentimentScore += sia.polarity_scores(x).get('compound')

sentimentScore /= lineNum
print("Overall Sentiment Score: ", sentimentScore)


f.close()
