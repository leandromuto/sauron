import scrapy

class CorridasBRSpider(scrapy.Spider):
	name = "corridasbr"

	def start_requests(self):
    	start_urls = ["http://www.corridasbr.com.br/"]
    
    	for url in start_urls:
  			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
  		page = response.url.
