import requests

def scrap_listing() :
    """
    scrapper la page de listing de la centrale
    return : page html
    """
    url = """https://www.lacentrale.fr/listing"""
    result = requests.get(url)
    print(result.text)
    

if __name__ == "__main__" : 
    html_page = scrap_listing()