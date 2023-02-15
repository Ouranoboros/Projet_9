from bs4 import BeautifulSoup
#from pprint import pprint
import requests

def User_URL(energie, marque, kms_max, kms_min, prix_max, prix_min, annees_max, annees_min) :
    url_lacentrale = 'https://www.lacentrale.fr/listing?energies={energie_url}&makesModelsCommercialNames={marque_url}&mileageMax={kms_max_url}&mileageMin={kms_min_url}&priceMax={prix_max_url}&priceMin={prix_min_url}&yearMax={annees_max_url}&yearMin={annees_min_url}'
    url = url_lacentrale.format(energie_url = energie, marque_url = marque, kms_max_url = kms_max, kms_min_url = kms_min, prix_max_url = prix_max, prix_min_url = prix_min, annees_max_url = annees_max, annees_min_url = annees_min)
    print(url)
    return url
    


def scrap_listing(url) :
    response = requests.get(url)
    print(response)
    return response.text

URL_request = User_URL('ess', 'PEUGEOT', '250000', '10000', '60000', '10000', '2022', '2019')
html_page = scrap_listing(URL_request)

soup = BeautifulSoup(html_page, 'html.parser')
cards = soup.find_all("div",class_ ='searchCardContainer')
print(cards)

for card in cards:
    title = card.find("h3","Text_Text_text Vehiculecard_Vehiculecard_title Text_Text_subtitle2")
    title2 = title.get_text()
    print(title2)

    object1 = card.find_all("div","Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")
    for test in object1:
        print (test.get_text())

    price = card.find("span","Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2")
    price2 = price.get_text()
    print(price2)
    print("― ― ― ― ― ― ―")