import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://mt-news.ru/news/"

html = requests.get(URL).text
soup = BeautifulSoup(html, "html.parser")

items_xml = ""

for a in soup.select("a.border.border-radius.padding"):
    link = a.get("href")

    title = a.select_one("h3.padding-top")
    date = a.select_one("span")

    style = a.get("style", "")
    img = ""
    if "url(" in style:
        img = style.split("url(")[1].split(")")[0]

    if title:
        title = title.text.strip()
    if date:
        date = date.text.strip()

    items_xml += f"""
    <item>
      <title><![CDATA[{title}]]></title>
      <link>{link}</link>
      <description><![CDATA[
        <img}
        {date}
      ]]></description>
      <pubDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate>
      <guid>{link}</guid>
    </item>
    """

xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>MT News</title>
    <link>{URL}</link>
    <description>Moto news</description>
    <language>ru</language>
    <ttl>60</ttl>

    {items_xml}

  </channel>
</rss>
"""

with open("motogp.xml", "w", encoding="utf-8") as f:
    f.write(xml)
