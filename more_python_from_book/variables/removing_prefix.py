url = "http://facebook.com"
news_url = url.removeprefix("http://")
print(news_url)

# Output: facebook.com

news_url = news_url.removesuffix(".com")
print(news_url)

# Output: facebook
