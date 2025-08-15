from newspaper import Article

def scrape_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return {
       "title" : article.title,
       "body" : article.text
    }
    
if __name__ == "__main__":
    url = 'https://www.bbc.com/news/articles/cwy5dqxd0z1o'
    result = scrape_article(url)
    print(result["title"])
    print(result["body"][:500])