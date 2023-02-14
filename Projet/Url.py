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