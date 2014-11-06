#My simple scrapy
========

This is a simple scrapy to crawl  Aaron Swartz's blog, just for fun.The function fetch will alway fetch all the url of blogs and
read_file will read all the passages which  will be stored.

1. Find all the url from the [Archive page] (http://www.aaronsw.com/weblog/archive).
2. Just crawl all passages from the page. Mostly are text paragraphs between the <p></p>. Use regex extract the text and filter   some odd characters.


