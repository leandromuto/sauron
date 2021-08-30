
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Race(scrapy.Item):
    name = scrapy.Field()
    date = scrapy.Field()
    city = scrapy.Field()
    distances = scrapy.Field()
    organizer = scrapy.Field()
    website = scrapy.Field()
    modality = scrapy.Field()
