import scrapy
import json

class CarsItemSpider(scrapy.Spider):
    name = 'cars_item'
    allowed_domains = ['khodro45.com']
    start_urls = ['https://khodro45.com/used-car']
    cars = []
    # cars_crawled_count = 0
    def parse(self, response):
        for page_index in range(1,6):
            link = f"https://khodro45.com/api/v2/car_listing/?page={page_index}&ordering=-created_time"
            # link = 'https://khodro45.com/api/v2/car_listing/?page=1&ordering=-created_time'
            yield scrapy.Request(url=link,callback=self.get_details,meta={"page_index": page_index})


    def get_details(self, response):
        res = json.loads(response.text)
        # self.cars_crawled_count += int(res["count"])
        cars_details = res["results"] 

        for car in cars_details:
            # for car in car_item['cars_details']:
            car_dict = {
                'id' : car['identifier'],
                'slug' : car['slug'],
                'guaranteed' :  car['guaranteed'],
                'immediate_delivery' :  car['immediate_delivery'],
                'price' :  car['price'],
                'discounted_price' : car['discounted_price'],
                'views' : car['views'],

                # car properties
                'brand_fa' : car['car_properties']['brand']['title'],
                'brand_en' : car['car_properties']['brand']['title_en'],
                "model_fa" : car['car_properties']['model']['title'],
                "model_en" : car['car_properties']['model']['title_en'],
                'year' : car['car_properties']['year'],

                # car city
                'city_fa' : car['city']['title'],
                'city_en' : car['city']['title_en'],

                # car specifications
                'document' : car['car_specifications']['document'],
                'klm' : car['car_specifications']['klm'],

                # car image
                'image_id'  : car['image']['id'],
                'image_file' : car['image']['file'],
                'image_file_high' : car['image']['file_high']
            }
            # add car to the list of car dictionaries
            yield { "res" : car_dict }