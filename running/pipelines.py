import logging
# from scrapy.exceptions import DropItem
from database.connection import get_database, get_collection

class MongoDBPipeline:
    def __init__(self):
        self.db_collection = get_collection("races")

    def process_item(self, item, spider):
        try:
            self.db_collection.insert_one(dict(item))
            logging.info("Race added to database.")
        except Exception as ex:
            logging.info(f"Error: {ex.args}")
