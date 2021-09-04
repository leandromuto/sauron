import scrapy
from running.items import Triathlon

class TriathlonBRSpider(scrapy.Spider):
    name = "triathlonbr"
    base_url = "https://triathlonbr.com.br/Blog"

    def start_requests(self):
        yield scrapy.Request(
            url=f"{self.base_url}/calendario",
            callback=self.parse_races_list
        )

    def parse_races_list(self, response):
        races_selector = "//tbody/tr[2 <= position() and position() < 500]"

        for race in response.xpath(races_selector):
            data = race.css("td span::text")

            if len(data.getall()) > 1 and not data[0].get() == "Data":
                print(data.getall())
                # import pdb; pdb.set_trace()
                fwd_data = {"modality" : data[2].get().strip()}

                more_info_url = race.css("a::attr(href)").get()

                yield scrapy.Request(
                    url=more_info_url,
                    cb_kwargs=dict(fwd_data=fwd_data),
                    callback=self.parse_race
                )

    def parse_race(self, response, fwd_data):
        table_content = response.xpath("(//table)[2]/tbody")

        for content in table_content:
            print(content)
            tri_race = Triathlon()

            tri_race["modality"] = fwd_data["modality"]
            tri_race["name"] = content.css("span.titulogrande::text").get().strip()
            tri_race["date"] = content.css("tr:nth-child(3) td:nth-child(2) span::text").get().strip()
            tri_race["city"] = content.css("tr:nth-child(4) td:nth-child(2) span::text").get().strip()
            tri_race["distances"] = content.css("tr:nth-child(5) td:nth-child(2) span::text").get().strip()
            tri_race["organizer"] = content.css("tr:nth-child(6) td:nth-child(2) span::text").get().strip()
            tri_race["website"] = content.css('tr:nth-child(7) td:nth-child(2) a::attr(href)').get().strip()

            yield tri_race

