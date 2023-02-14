#Importation des différentes librairies nécessaires 
import requests
from bs4 import BeautifulSoup
#import pandas as pd


#Url de base de la centrale
url = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&mileageMax={km_max}&mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}yearMax={year_max}&yearMin={year_min}"""
#spécification des différents paramètres
parameters = url.format(energy="ess",brand="PEUGEOT",km_max=250000,km_min=10000,price_max=60000,price_min=10000,year_max=2022,year_min=2019)
print (parameters)

#Requête de l'url
request= requests.get(url)
print(request)
request = request.text

#Passage dans BeautifulSoup
soup = BeautifulSoup(request,'html.parser')
cards = soup.find_all("div",class_ ='searchCardContainer')
print(cards)

def forming(var):
    var_tab = []
    for e in var : 
        e = e.text
        var_tab.append(e) 

    return var_tab


soup = (soup.find_all('h3', {'class': 'Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2'}))
