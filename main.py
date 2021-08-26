from nltk.sentiment import SentimentIntensityAnalyzer

with open('input.txt','r') as f:
    lines = f.readlines()

#Using an instance of the VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

#Tracking the amoung of line in file
lineNum = 0
#Calculating the sentiment value for each line
sentimentScore = 0

for x in lines:
    lineNum = lineNum + 1
    print(lineNum, ": ", sia.polarity_scores(x).get('compound')) #Printing each individul score for the line
    sentimentScore += sia.polarity_scores(x).get('compound') #accumulating the scores for the file

#Determining the average score for entire file
sentimentScore /= lineNum 

#Displaying the calculated total score
print("Overall Sentiment Score: ", sentimentScore)


f.close()
