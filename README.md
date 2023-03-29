# SMSspamClassifier
Built a SMS spam detection model using a Multinomial Naive Bayes model. Also built a supporting web page to deploy the model using the streamlit library.
Tested out both Bernaulli Naive Bayes and Multinomial Naive bayes and found out MultiNB has a precision score of 100%(which means it did not raise any false positive while testing)
Used the NLTK(Natural Language ToolKit) library to preprocess the data and remove all the stop words and punctutations so that the model can be trained on much cleaner and well Labeled data


This is a histrogram showing the most frequently used words in Spam Texts



![Frequent_Words](https://user-images.githubusercontent.com/96071514/228517324-d11e4f0c-40f6-4b14-b42c-6dfe69d05953.png)



By this we can infer that Call, Free, claim these are the top most used words in a spam sms. This data can be used to specificaly target these words and train our model depending on that


Also made a website using Streamlit library, Very basis website which includes just a text area for the user to enter the input and our model and vectorizer integrated into that website which predicts and outputs the result onto the screen




![spamWebsite](https://user-images.githubusercontent.com/96071514/228518394-db9fad03-afb6-4f40-87b9-f5b7d3b49c68.PNG)
