import streamlit as st
import pickle as pkl
import nltk

from nltk.corpus import stopwords
import string
from nltk import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []

    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pkl.load(open('Vectorizer.pkl','rb'))
model = pkl.load(open('Model.pkl','rb'))

st.title('SMS SPAM CLASSIFIER')

input_sms = st.text_area('Enter the message')

if st.button('Predict'):

    transformed_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_sms])

    result= model.predict(vector_input)

    if result == 1:
        st.header('SPAM')
    else:
        st.header('NOT SPAM')



