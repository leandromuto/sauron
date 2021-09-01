import re
import logging
# from scrapy.exceptions import DropItem
from database.connection import get_database, get_collection

class RacePipeline:
    def __init__(self):
        pass

    def process_item(self, item, spider):
        spider_name = spider.name
        if spider_name == 'corridasbr':
            item["modality"] = "run"

        distances = re.findall(r"([0-9,]+)", str(item["distances"]))
        item["distances"] = distances

        return item

class MongoDBPipeline:
    def __init__(self):
        self.db_collection = get_collection("races")

    def process_item(self, item, spider):
        try:
            doc_exist = self.db_collection.find(item)
            if not any(doc_exist):
                document = self.db_collection.insert_one(dict(item))
                logging.info(f"Race added to database. Document id: {document.inserted_id}")
        except Exception as ex:
            logging.info(f"Error: {ex.args}")
