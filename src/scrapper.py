from newspaper import Article

url = 'https://www.bbc.com/news/articles/cwy5dqxd0z1o'
article = Article(url)
article.download()
article.parse()
print(article.title)
print(article.text[:500])