from itemadapter import ItemAdapter
import logging
# from scrapy.exceptions import DropItem
from database.connection import get_database, get_collection

class MongoDBPipeline:
    def __init__(self):
        self.db_collection = get_collection("races")

    def process_item(self, item, spider):
        self.db_collection.insert_one(item)
        logging.info("Race added to database.")
