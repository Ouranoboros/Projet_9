#Importation des différentes librairies nécessaires 
import requests
from bs4 import BeautifulSoup
import pandas as pd


#Url de base de la centrale
url = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&mileageMax={km_max}&mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}yearMax={year_max}&yearMin={year_min}&options=&page={page}"""

#spécification des différents paramètres
url = url.format(energy="ess",brand="PEUGEOT",km_max=250000,km_min=10000,price_max=60000,price_min=10000,year_max=2022,year_min=2019,page=1)
print (url)

#Requête de l'url
request= requests.get(url, timeout=5).text

#Passage dans BeautifulSoup
soup = BeautifulSoup(request,'html.parser')

#Récupération des blocs de données
cards = soup.find_all('div','Vehiculecard_Vehiculecard_cardBody')

#Récupération des données
i=1
scrapped_items = []
for card in cards :
    print(i)
    #Recupérer le nom de la marque par la variable que l'on renseigne
    title = card.find('h3','Text_Text_subtitle2').get_text()
    test = title
    print(title)
    test = title.split("PEUGEOT")
    test_edit = test[-1].strip()
    print(test_edit)

    
    motor = card.find('div', 'Text_Text_body2').get_text()
    print(motor)
    
    characteristics = card.find_all('div', 'Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2')
    elements = []
    for characteristic in characteristics : 
        #Ajouter les élements dans une liste et les ajouter dans des variables en fonction de leur position 
        elements.append(characteristic.get_text())
    
    year = int(elements[0])
    mileage = elements[1]
    mileage_str = mileage.replace("km","")
    mileage_str = mileage_str.replace(" ","")
    mileage_str = mileage_str.replace("\xa0","")
    mileage_int = int(mileage_str)
    gear = elements[2]
    fuel = elements[3]

    print(year)
    print(mileage_int)
    print(gear)
    print(fuel)

    price = (card.find('span', 'Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2').get_text())
    price_str =price.replace("€","")
    price_int = int(price_str.replace(" ", ""))
    print (price_int)
    print ('\n','--------------', '\n')

    item = [i,title,test_edit,motor,year,mileage_int,gear,fuel,price_int]
    scrapped_items.append(item)
    i += 1
print(scrapped_items)

# Conversion d'un tableau en dataframe puis stockage dans un csv
df_write = pd.DataFrame(scrapped_items)
df_write.to_csv("data.csv", index=False, header=['index', 'brand', 'model', 'motor', 'year', 'mileage', 'gear', 'fuel', 'price'])