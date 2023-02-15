import requests
from bs4 import BeautifulSoup
import pandas as pd

def forming (to_edit):
    text = to_edit.replace("km","").replace("€","").replace(" ","").replace("\xa0","")
    integer= int(text)
    return integer

def url(brand_name,page_number): 
    url_to_edit = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&mileageMax={km_max}&mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}yearMax={year_max}&yearMin={year_min}&options=&page={page}"""
    url = url_to_edit.format(energy = "ess", brand = brand_name, km_max = 250000, km_min = 10000, price_max = 60000, price_min = 10000, year_max = 2022, year_min = 2019, page = page_number)
    return url

def request(brand_name, page_number):
    url_main = url(brand_name, page_number)
    request= requests.get(url_main, timeout=5).text
    return request

def parsing(brand_name, page_number):
    request_made = request(brand_name, page_number)
    
    soup = BeautifulSoup(request_made,'html.parser')
    
    cards = soup.find_all('div','Vehiculecard_Vehiculecard_cardBody')
    
    i=1
    scrapped_items = []
    
    for card in cards :
       title = card.find('h3','Text_Text_subtitle2').get_text()
       model_to_edit = title.split(brand_name) 
       model = model_to_edit[-1].strip()

       motor = card.find('div', 'Text_Text_body2').get_text()
       
       characteristics = card.find_all('div', 'Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2')
       elements = []
       for characteristic in characteristics :
           elements.append(characteristic.get_text())

       year = int(elements[0])
       to_edit = elements[1]
       mileage = forming(to_edit)
       gear = elements[2]
       fuel = elements[3]
       
       to_edit = (card.find('span', 'Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2').get_text())
       price = forming(to_edit)

       item = [i, brand_name, model, motor, year, mileage, gear, fuel, price]
       scrapped_items.append(item)
       i += 1

    return scrapped_items

def csv_editing(brand_name, page_number):
    scrapped_items = parsing(brand_name, page_number)
    df_write = pd.DataFrame(scrapped_items)
    df_write.to_csv("data.csv", index=False, header=['Index', 'Brand', 'Model', 'Motor', 'Year', 'Mileage', 'Gear', 'Fuel', 'Price'])

def main() :
    brand_name = "PEUGEOT"
    page_number = 1
    while page_number <= 5 :
        csv_editing(brand_name, page_number)
        page_number += 1

main()