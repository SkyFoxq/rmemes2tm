import scrapy

class RedditSpider(scrapy.Spider):
	name = "rmemes"
	start_urls = [
	'https://old.reddit.com/r/memes/top/'

	]
	pages = 3
	def is_pic(self,s):
		if s[-3:] == 'jpg' or s[-3:] == 'png' or s[-4:] == 'jpeg':# or s[-3:] == 'gif':
			return True
		else:
			return False

	def parse(self, response):
		titles = response.selector.xpath('//div[@class="top-matter"]/p[@class="title"]/a/text()').extract()
		authors = response.selector.xpath('//div[@id="siteTable"]/div/@data-author').extract()
		urls = response.selector.xpath('//div[@id="siteTable"]/div/@data-permalink').extract()
		content_links = response.selector.xpath('//div[@id="siteTable"]/div/@data-url').extract()
		ratings = response.selector.xpath('//div[@id="siteTable"]/div/@data-score').extract()
		#print(len(content_links))
		#print(type(content_links))
		for i in range(25):
			#print('#############'+str(i))
			if not self.is_pic(content_links[i]):
				#print ('#########'+content_links[i])
				continue 
			yield  {
			'title': titles[i],
			'author': authors[i],
			'url' : 'https://old.reddit.com' + urls[i],
			'content' : content_links[i],
			'rating' : ratings[i],
			'current' : False,
			}
		next_page = response.selector.xpath('//span[@class="next-button"]/a/@href')[0]
		self.pages -= 1
		if next_page is not None and self.pages > 0:
			#print ('#############\t' + str(self.pages))
			yield response.follow(next_page, callback=self.parse)	
