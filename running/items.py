
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Race(scrapy.Item):
    name = scrapy.Field()
    date = scrapy.Field()
    city = scrapy.Field()
    organizer = scrapy.Field()
    website = scrapy.Field()
    modality = scrapy.Field()

class Running(Race):
    distances = scrapy.Field()

class Triathlon(Race):
    swim = scrapy.Field()
    bike = scrapy.Field()
    run = scrapy.Field()
