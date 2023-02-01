"""
Methode format string"""

brand="RENAULT"
year_min=2010
year_max=2019
url = """https://www.lacentrale.fr/listing?makesModelsCommercialNames={brand}&yearMax={year_max}&yearMin={year_min}""".format(brand=brand, year_min=year_min, year_max=year_max)

print(url)
var_first, var_second = 0, 1
"""Autre syntaxes possibles"""
# str_test = "abc{}def{}".format(var_first, var_second)
# str_test = "abc{1}def{0}".format(var_first, var_second)

while var_first < 10 :
    str_test = "abc{first}def{second}".format(first=var_first, second=var_second)
    print(str_test)
    var_first += 1
    var_second += 2