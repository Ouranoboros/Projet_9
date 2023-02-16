import pandas as pd #pip install pandas

#Lecture d'un fichier csv et conversion en dataframe.
df = pd.read_csv("file.csv")
# print(df)

# Conversion d'un dictionnaire en dataframe puis stockage dans un csv
dict_df = {
    "brand" : ['ford', 'bmw'],
    "model" : ['focus', 'serie 3'],
    "year" : [2012, 2020]
}
df_write = pd.DataFrame(dict_df)
df_write.to_csv("pandas.csv", index=False)
# Syntaxe courte
pd.DataFrame(dict_df).to_csv("pandas.csv", index=False)


# Conversion d'un tableau en dataframe puis stockage dans un csv

array_df = [
    ['ford', 'focus', 2012],
    ['bmw', 'serie 3', 2020]
]

df_write = pd.DataFrame(array_df)
print(df_write)
df_write.to_csv("pandas2.csv", index=False, header=['brand', 'model', 'version'])
# Syntaxe courte
pd.DataFrame(array_df).to_csv("pandas2.csv", index=False, header=['brand', 'model', 'version'])

'''
2 ième méthode 
'''

import csv

#Ouverture et instanciation d'un objet "csv.writer"
fd = open("file.csv", "w")
csv_writer = csv.writer(fd)
fd.close()

# Deuxième méthode d'ouverture d'un fichier, et écriture grâce à writerrow
with open("file.csv", "w") as fd :
    csv_writer = csv.writer(fd)
    csv_writer.writerow(['brand', 'model', 'year'])
    csv_writer.writerow(['ford', 'focus', 2012])

with open("file2.csv", "w") as fd :
    csv_writer = csv.writer(fd)
    csv_writer.writerows([['brand', 'model', 'year'],
                          ['ford', 'focus', 2012],
                          ['bmw', 'serie 3', 2020]])
    
# Ouverture du fichier et lecture grâce à l'object csv.reader
with open("file.csv", "r") as fd :
    csv_reader = csv.reader(fd)
    for row in csv_reader :
        brand = row[0]
        model = row[1]
        year = row[2]