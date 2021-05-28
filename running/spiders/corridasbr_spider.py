import scrapy

class CorridasBRSpider(scrapy.Spider):
	name = "corridasbr"

	def start_requests(self):
		states = [
			'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
			'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN',
			'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'
		]

		for state in states:
			yield scrapy.Request(
				url=f'http://www.corridasbr.com.br/{state}/calendario.asp',
				callback=self.parse
			)

	def parse(self, response):
		print(response)

