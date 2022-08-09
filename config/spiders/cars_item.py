import scrapy
import json

class CarsItemSpider(scrapy.Spider):
    name = 'cars_item'
    allowed_domains = ['khodro45.com']
    start_urls = ['https://khodro45.com/used-car']
    # cars_crawled_count = 0
    def parse(self, response):
        for page_index in range(1,6):
            link = f"https://khodro45.com/api/v2/car_listing/?page={page_index}&ordering=-created_time"
            # link = 'https://khodro45.com/api/v2/car_listing/?page=1&ordering=-created_time'
            yield scrapy.Request(url=link,callback=self.get_details,meta={"page_index": page_index})


    def get_details(self, response):
        res = json.loads(response.text)
        # self.cars_crawled_count += int(res["count"])
        yield { 
                f"cars_details" : res["results"],
        }