'''
Importation des différentes bibliothèques :
- requests : pour faire des requêtes html 
- bs4 : pour faire le "parsing", extraire les différentes informations pertinentes 
- pandas : pour la création et l'édition du fichier csv
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

def forming (to_edit):
    '''
    Fonction chargée de l'édition du format d'une variable en int (ne garde que les nombres).
    '''
    text = to_edit.replace("km","").replace("€","").replace(" ","").replace("\xa0","")
    integer= int(text)
    return integer

def url(brand_name,page_number): 
    '''
    Fonction chargée de la construction de l'Url du site de la centrale.
    '''
    url_to_edit = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&mileageMax={km_max}&mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}yearMax={year_max}&yearMin={year_min}&options=&page={page}"""
    url = url_to_edit.format(energy = "ess", brand = brand_name, km_max = 250000, km_min = 10000, price_max = 60000, price_min = 10000, year_max = 2022, year_min = 2019, page = page_number)
    return url

def request(brand_name, page_number):
    '''
    Fonction chargée d'effectuer les requêtes au site de la centrale.
    '''
    url_main = url(brand_name, page_number)
    request= requests.get(url_main, timeout=5).text
    return request

def parsing(brand_name, page_number, scrapped_items, i):
    '''
    Fonction chargée de récupérer les informations qui nous sont utiles dans la page.
    '''

    request_made = request(brand_name, page_number) #Récupère la requête effectuée par la fonction 'request'.
    
    soup = BeautifulSoup(request_made,'html.parser') #Passage dans BeautifulSoup.
    
    cards = soup.find_all('div','Vehiculecard_Vehiculecard_cardBody') #Récupération de toutes les cartes de voiture d'une page.
    
    for card in cards : #Exécution pour chaque carte :
       title = card.find('h3','Text_Text_subtitle2').get_text() #Récupération du "Titre" de la carte.
       model_to_edit = title.split(brand_name) #Suppression du nom de la marque, afin de récupérer uniquement le modèle.
       model = model_to_edit[-1].strip() #Suppréssion des espaces. 

       motor = card.find('div', 'Text_Text_body2').get_text() #Récupération de la référence moteur.
       
       characteristics = card.find_all('div', 'Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2') #Récupération du "bloc" de charactéristiques.
       elements = [] # Création de la liste des éléments de se "bloc".
       for characteristic in characteristics : #Itération de chaque caractéristique.
           elements.append(characteristic.get_text()) #Ajout de chaque caractéristique à la liste des éléments.

       year = int(elements[0]) #Association de chaque caractéristique à une variable.
       to_edit = elements[1] #Association de chaque caractéristique à une variable.
       mileage = forming(to_edit) #Récupération du résultat après mise en forme.
       gear = elements[2] #Association de chaque caractéristique à une variable.
       fuel = elements[3] #Association de chaque caractéristique à une variable.
       
       to_edit = (card.find('span', 'Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2').get_text()) #Récupération du prix.
       price = forming(to_edit) #Récupération du résultat après mise en forme.

       item = [i, brand_name, model, motor, year, mileage, gear, fuel, price] #Enregistrement de toutes les carastéristiques dans une liste corréspondant à une référence.
       scrapped_items.append(item) #Ajout de cette référence à la liste global.
       i += 1

    return scrapped_items, i #Renvoie les variables modifiées.

def csv_editing(scrapped_items):
    '''
    Fonction chargée de la création et de l'édition du fichier csv.
    '''
    df_write = pd.DataFrame(scrapped_items)
    df_write.to_csv("data.csv", index=False, header=['Index', 'Brand', 'Model', 'Motor', 'Year', 'Mileage', 'Gear', 'Fuel', 'Price'])

def main() :
    '''
    Fonction permettat l'activation du programme
    Contient les variables nécessaires dans plusieurs fonctions.
    '''
    brand_name = "PEUGEOT"
    page_number = 1
    scrapped_items = []
    i = 1

    while page_number <= 8 :
        scrapped_items, i = parsing(brand_name, page_number, scrapped_items, i)
        page_number += 1
    
    csv_editing(scrapped_items)

main()