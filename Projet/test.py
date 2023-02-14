#Importation des différentes librairies nécessaire
import requests
from bs4 import BeautifulSoup
#import pandas as pd

#Url de base de la centrale
url = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&mileageMax={km_max}&mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}yearMax={year_max}&yearMin={year_min}"""

#spécification des différents paramètres
parameters = url.format(energy="ess",brand="PEUGEOT",km_max=150000,km_min=10000,price_max=100000,price_min=3000,year_max=2023,year_min=2010)
print (parameters)

#Requête de l'url
request= requests.get(url).text
#pprint(request)

#Passage dans BeautifulSoup
soup = BeautifulSoup(request,'html.parser')
#pprint (soup)

#Recupération de toutes les cartes
cards = soup.find_all('div',{'class':'searchCardContainer'})
print(1)
#Pour chaque carte
for card in cards :
    print(card)
    print(2)
    title = card.find("h3",{'class':"Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2"}).get_text()
    #title2 = title
    print(title)

    object1 = card.find_all("div",{'class':"Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2"})
    for test in object1:
        print (test.get_text())

    price = card.find("span",{'class':"Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2"})
    price2 = price.get_text()
    print(price2)
    print("― ― ― ― ― ― ―")