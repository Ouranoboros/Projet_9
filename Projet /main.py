import requests

def scrap_listing(brand, year_max, year_min, km_min, km_max, energy, price_min, price_max) :
    """
    scrapper la page de listing de la centrale
    return : page html
    """
    url = """https://www.lacentrale.fr/listing?energies={energy}
    &makesModelsCommercialNames={brand}&mileageMax={km_max}mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}yearMax={year_max}
    &yearMin={year_min}""".format(energy,brand,km_max,km_min,price_max,price_min,year_max,year_min)
    requests.get(url)
    

if __name__ == "__main__" : 
    html_page = scrap_listing("PEUGEOT", 2022, 2000, 0, 100000, "ess", 0, 50000)