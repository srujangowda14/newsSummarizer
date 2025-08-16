from transformers import pipeline

sentiment_pipeline =  pipeline("sentiment-analysis")

def classify_sentiment(text):
    result = sentiment_pipeline(text[:512])[0]
    return{
        "label": result["label"],
        "score": round(result["score"], 3)
    }

if __name__ == "__main__":
    sample_text = "The new AI technology is amazing and will change the future of work!"
    sentiment = classify_sentiment(sample_text)
    print(sentiment)
