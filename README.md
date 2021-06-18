# Machine learning projects 
This repository contains some basic ML projects which I built for learning basics.
# 1. Creditcard fraud detection 
In this project, I used isolation forest algorithm and local outlier factor algorithm for detecting fraud credit cards. This dataset contains numerical values which are a result of PCA transformations. This PCA transformation is done because data is secured and not sharable.
Isolation forest algorithm is the newest techniques to detect anomalities. It isloates observation by randomly selecting features and then randomly selecting a split value.
LOF algorithm is an unsupervised outlier detection method which computes the local density derivation of  agiven data point with respect to its neighbors. It considers as outlier samples that have a substantially lower density than their neighbors.
Isolation forst gave the best accuracy of 99.7% and local outlier factor gave an accuracy of 99.6%

# 2. Movie recommendation system
Recommender systems are one of the most successful and widespread application of machine learning technologies in business. You can find large scale recommender systems in retail, video on demand, or music streaming.
In this project, I used collaborative filtering and feature extraction to get the results.

# 3. Stock price prediction using LSTM
Used an LSTM neural network to predict the closing price of Apple stock using Yahoo stock API. This model can be used to predict the stock of any company just by replacing the company name in the code.

# 4. Automated email bot
This is an automated email bot that sends an unlimited number of emails to unlimited people without typing. It uses smtp library for sending mails and pyttsx3 (python tts engine) for converting the contents of what we say to text.

# 5. Voice assistant named "ALPHA"
This is a personalized voice assistant named ALPHA which is similar to alexa. It helps us to play songs and movies from YouTube, tells us a joke, tells us about a person and gives the information of the current time.
