import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}
&mileageMax={km_max}&mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}yearMax={year_max}&yearMin={year_min}"""
parameters = url.format(energy="ess",brand="PEUGEOT",km_max=150000,km_min=10000,price_max=100000,price_min=3000,year_max=2023,year_min=2010)
print (parameters)


request= requests.get(url).text
#pprint(request)

soup = BeautifulSoup(request)
pprint (soup)

