from scrapper import scrape_article
from sentiment import classify_sentiment

def run_pipeline(url):
    article = scrape_article(url)

    sentiment = classify_sentiment(article["body"])

    print("\n=== Article Info ===")
    print(f"Title: {article['title']}\n")
    print(f"First 300 chars: {article['body'][:300]}...\n")
    
    print("=== Sentiment Analysis ===")
    print(f"Sentiment: {sentiment['label']} (confidence {sentiment['score']})")

if __name__ == "__main__":
    url = "https://www.bbc.com/news/articles/cwy5dqxd0z1o"  # Example article
    run_pipeline(url)