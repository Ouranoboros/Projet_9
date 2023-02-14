#Importation des différentes librairies nécessaires 
import requests
from bs4 import BeautifulSoup
import pandas as pd


#Url de base de la centrale
url = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&mileageMax={km_max}&mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}yearMax={year_max}&yearMin={year_min}"""

#spécification des différents paramètres
url = url.format(energy="ess",brand="PEUGEOT",km_max=250000,km_min=10000,price_max=60000,price_min=10000,year_max=2022,year_min=2019)
print (url)

#Requête de l'url
request= requests.get(url, timeout=5).text

#Passage dans BeautifulSoup
soup = BeautifulSoup(request,'html.parser')

#Récupération des blocs de données
cards = soup.find_all('div','Vehiculecard_Vehiculecard_cardBody')

#Récupération des données
for card in cards :
    title = card.find('h3','Text_Text_subtitle2').get_text()
    test = title.split('PEUGEOT',1)
    print(test)
    
    motor = card.find('div', 'Text_Text_body2').get_text()
    print(motor)
    
    characteristics = card.find_all('div', 'Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2')
    for characteristic in characteristics : 
        print(characteristic.get_text())
    
    price = (card.find('span', 'Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2').get_text())
    price_str =price.replace("€","")
    price_int = int(price_str.replace(" ",""))
    print (price_int)
    
    print ('\n','--------------', '\n')