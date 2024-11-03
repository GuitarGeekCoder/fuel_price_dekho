import re
import json
import requests
import time
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from fuels.models import Fuel_price
class Command(BaseCommand):
    help = 'Runs a daily script'

    def handle(self, *args, **options):
        while True:
            # Your script logic here
            self.stdout.write(self.style.SUCCESS('Successfully ran daily script'))
            petrol_dict=self.Petrol_price()
            print("--------diesel price-----------")
            diesel_dict=self.Diesel_price()
            # Convert values to integers and remove trailing spaces
            f_dict = {key: [float(petrol_dict.get(key, 0).strip()), float(diesel_dict.get(key, 0).strip())] for key in set(petrol_dict) | set(diesel_dict)}

            print(f_dict)
            for data in f_dict:
                city=data
                petrol_price=f_dict[city][0]
                diesel_price=f_dict[city][1]
                # Try to get the existing record based on the unique identifier (city)
                obj, created = Fuel_price.objects.get_or_create(city_name=city, defaults={
                    'petrol_price': petrol_price,
                    'diesel_price': diesel_price,
                })
                # If the record was not created, update the prices
                if not created:
                    obj.petrol_price = petrol_price
                    obj.diesel_price = diesel_price
                    obj.save()
            print("successfully inserted record")  

            
            time.sleep(3600*4)    


    def Petrol_price(self):
        city_price={}
        try:
            response = requests.get("https://www.livemint.com/fuel-prices/petrol-city-wise")
            response.raise_for_status()  # Raise an exception for bad responses

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            box_3_element = soup.find('section', {'id': 'box-3'})
            fuel_data = box_3_element.find_all('ul')
            for fuel in fuel_data[1:]:
                fuel_info_string=fuel.text.strip()
                pattern = re.compile(r'\n| ₹/L ')
                info=pattern.split(fuel_info_string)
                print("-------------")
                city, petrol_price, change = info[0], info[1], info[2]
                # print(city,"-",petrol_price,"-",change)  
                petrol_price=petrol_price.split("₹")[0]
                city_price[city]= petrol_price 
        except Exception as e:
            print("Exception during request Petrol:", str(e))
        return city_price

    def Diesel_price(self):
        city_price={}
        try:
            response = requests.get("https://www.livemint.com/fuel-prices/diesel-city-wise")
            response.raise_for_status()  # Raise an exception for bad responses

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            box_3_element = soup.find('section', {'id': 'box-3'})
            fuel_data = box_3_element.find_all('ul')
            for fuel in fuel_data[1:]:
                fuel_info_string=fuel.text.strip()
                pattern = re.compile(r'\n| ₹/L ')
                info=pattern.split(fuel_info_string)
                print("-------------")
                city, diesel_price, change = info[0], info[1], info[2]
                # print(city,"-",diesel_price,"-",change) 
                diesel_price=diesel_price.split("₹")[0]
                city_price[city]= diesel_price

        except Exception as e:
            print("Exception during request Diesel:", str(e))
        
        return city_price
    