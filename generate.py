from datetime import datetime

xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>MotoGP</title>
    <link>https://www.motogp.com</link>
    <description>Latest MotoGP news</description>
    <language>en-us</language>
    <ttl>60</ttl>
    <lastBuildDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}</lastBuildDate>

    <item>
      <title><![CDATA[MotoGP race results]]></title>
      <link>https://www.motogp.com/en/news/</link>
      <description><![CDATA[
        Auto generated RSS feed
      ]]></description>
      <pubDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate>
      <guid>https://www.motogp.com/en/news/</guid>
    </item>

  </channel>
</rss>
"""

with open("motogp.xml", "w", encoding="utf-8") as f:
    f.write(xml)
