import streamlit as st

from scrapper import scrape_article
from sentiment import classify_sentiment
from summarizer import summarize_text

st.title("Sentiment bases news summarizer")

url = st.text_input("Enter the news url")

if url:
    with st.spinner("Processing..."):

       article = scrape_article(url)

       sentiment = classify_sentiment(article["body"])

       summary = summarize_text(article["body"])

    st.subheader("Article Title")
    st.write(article["title"])

    st.subheader("Sentiment")
    st.write(f"{sentiment['label']} (confidence {sentiment['score']})")

    st.subheader("Summary")
    st.write(summary)

    st.subheader("Original Text (first 500 chars)")
    st.write(article["body"][:500] + "...")







