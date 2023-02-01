energies = ["dies","ess", "elec", "hyb","plug_hyb", "not_plug_hyb", "gpl", "eth", "alt"]
#dies = diesel / ess = essence / elec = electrique / hyb = hybride / plub_hyb = hybride rechargeabable / not_plug_hyb = hybride non rechargeabable / gpl = biocarburation essence / eth = biocarburation essence bioéthanol / alt = autres énergies alternatives 
print (energies)

def_energy = ""
def_brand =""
def_km_max = ""
def_km_min = ""
def_price_max = ""
def_price_min = ""
def_year_max = ""
def_year_min = ""

url = """https://www.lacentrale.fr/listing?energies={energy}
&makesModelsCommercialNames={brand}&mileageMax={km_max}mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}yearMax={year_max}
&yearMin={year_min}""".format(energy = def_energy,brand = def_brand,km_max=def_km_max,km_min=def_km_min,price_max=def_price_max,price_min=def_price_min,year_max=def_year_max,year_min=def_year_min)

print (url)

class Parameters_choice ():
    def __init__(self) :
        self.energies = ["dies","ess", "elec", "hyb","plug_hyb", "not_plug_hyb", "gpl", "eth", "alt"]
        self.def_energy = input("Vous recherchez un véhicule de quelle type d'énergie ?")
        self.def_brand = input("Vous recherchez un véhicule de quelle marque ?")
        self.def_km_max = int(input("Vous recherchez un véhicule avec un kilométrage maximum de ?"))
        self.def_km_min = int(input("Vous recherchez un véhicule avec un kilométrage minimum de ?"))
        self.def_price_max = int(input("Vous recherchez un véhicule avec un prix maximum de ?"))
        self.def_price_min = int(input("Vous recherchez un véhicule avec un prix minimum de ?"))
        self.def_year_max = int(input("Vous recherchez un véhicule datant au maximum de ?"))
        self.def_year_min = int(input("Vous recherchez un véhicule datant au minimum de ?"))
        self.url = url_search()

    def url_search(self):
        url = """https://www.lacentrale.fr/listing?energies={energy}
        &makesModelsCommercialNames={brand}&mileageMax={km_max}mileageMin={km_min}&priceMax={price_max}&priceMin={price_min}yearMax={year_max}
        &yearMin={year_min}""".format(energy = def_energy,brand = def_brand,km_max=def_km_max,km_min=def_km_min,price_max=def_price_max,price_min=def_price_min,year_max=def_year_max,year_min=def_year_min)