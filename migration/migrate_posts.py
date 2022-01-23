import feedparser
from markdownify import markdownify

## handy for local dev
from icecream import ic

d = feedparser.parse("https://steveswift.com.au/feed/")

for post in d["entries"]:
    title = post["title"]
    tags = post["tags"]
    date = post["published"]
    body = markdownify(post["content"][0]["value"])
    ic(title, body)
