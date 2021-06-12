import scrapy

class CorridasBRSpider(scrapy.Spider):
	name = "corridasbr"
	base_url = "http://www.corridasbr.com.br"

	def start_requests(self):
		states = [
			'AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
			'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN',
			'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'
		]

		for state in states:
			yield scrapy.Request(
				url=f'{self.base_url}/{state}/calendario.asp',
				callback=self.parse_states,
				cb_kwargs=dict(state=state)
			)

	def parse_states(self, response, state):
		next_pages = response.css('td:nth-child(3) span.tipo3 a::attr(href)').getall()

		if next_pages is not None:
			for page in next_pages:
				yield scrapy.Request(
					url=f"{self.base_url}/{state}/{page}",
					callback=self.parse_state_running
				)

	def parse_state_running(self, response):
		table_selector = "(//table)[9]"

		for info in response.xpath(table_selector):
			yield {
				"name": info.css('tr span strong::text').get(),
				"date": info.css('tr:nth-child(2) td:nth-child(2) span::text').get(),
				"city": info.css('tr:nth-child(3) td:nth-child(2) span::text').get(),
				"distances": info.css('tr:nth-child(4) td:nth-child(2) span::text').get(),
				"organizer": info.css('tr:nth-child(6) td:nth-child(2) span::text').get(),
				"website": info.css('tr:nth-child(7) td:nth-child(2) a::attr(href)').get()
			}
