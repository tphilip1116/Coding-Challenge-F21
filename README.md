# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted.

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Explanation:

The Natural Language Toolkit for python is used in the Solution. The VADER sentiment Analyzer was used to score each line of the text file. The overall sentiment score of the file is the average score of all the lines in the file. The score is calculated from the compound result of the sentiment analyzer. I used the average score of each line because I didn't want the length of the file to affect the sentiment score and the fixed range from -1 to 1 will be more consistent with larger groups files.

Compound Results are float numbers that express the magnitude of the sentiment.

Scores Range from -1 to 1:
- Negative Sentiment will be closer to -1
- Neutral Sentiment will be closer to 0
- Positive Sentiment will be closer to 1

## Expectations:
When I first read the file I notices some negative words towards the beginning but then as I began reading further I recognized a shift with a lot more positive words at the latter half of the text. The text file started with an excerpt from the book **Fahrenheit 451** which had some fairly negative sentiment specifically in this portion but then it switched to the **The Autobiography of Benjamin Franklin** which was mostly neutral and had somewhat of a positive sentiment. This is why it was no surprise to me when the program evaluated the sentiment with a positive response **(0.15277)** because the Vader Sentiment Analyzer uses the bag of words approach score the sentiment. The bag of words approach is when there is a database of pre-determined values assigned to a immense amount of keys. The database is then used to evaluate a sentence based on the composed words.

## Resources

The research on how to use the VADER Sentiment Analyzer was found in this website:
https://realpython.com/python-nltk-sentiment-analysis/

The research on comparing different sentiment analysis:
https://medium.com/@b.terryjack/nlp-pre-trained-sentiment-analysis-1eb52a9d742c

The research on the Bag of Words concept:
https://machinelearningmastery.com/gentle-introduction-bag-words-model/
