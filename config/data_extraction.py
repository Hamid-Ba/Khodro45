import json

cars = []

# open result.json file
with open('result.json', 'r') as json_file:
    items = json.loads(json_file.read())
    
    for car_item in items:
        for car in car_item[f'cars_details']:
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
            cars.append(car_dict)

# convert cars to json and save it to final_result.json file
with open('final_result.json', 'w',encoding='utf8') as final_result:
    json.dump(cars, final_result,ensure_ascii=False)
    final_result.close()