import feedparser
from markdownify import markdownify
from datetime import datetime
from pathlib import Path

## handy for local dev
from icecream import ic

d = feedparser.parse("https://steveswift.com.au/feed/")

def jekyll_post_date(args):
    ## TODO the datetime is actually returned as a 'published_parsed' field, but it's not a datetime, so...
    return datetime.strptime(post["published"][0:16], "%a, %d %b %Y")

def jekyll_post_name(post):
    title = post["title"]
    date = jekyll_post_date(post)
    ## a bit gross, but it'll do for now
    return f"{datetime.strftime(date, f'%Y-%m-%d')}-{title.replace(' ', '-')}.md".lower().replace(":", "").replace(",", "")

def post_body_as_md(post):
    if len(post["content"]) > 1:
        ic(post)
        raise ValueError(f"Multiple content fields for {post['title']}")

    markdownify(post["content"][0]["value"])

for post in d["entries"]:

    post_path = Path("../_posts")
    filename = jekyll_post_name(post)
    title = post["title"]
    tags = post["tags"]
    date = jekyll_post_date(post)
    body = post_body_as_md(post)

    with open(post_path / filename, mode='w') as f:
        f.write_text(f"""---
title: "{title}"
tags: {tags}
---

{body}""")
