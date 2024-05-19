# Importer pandas til læse og tilføje data til vores datasæt
import pandas as pd

# Opretter en liste med navne på de mærker vi arbejder med
brand = ["audi", "bmw", "ford", "hyundai", "mercedes", "skoda", "toyota", "vauxhall", "vw"]

# Opretter en funktion til tilføje mærket til de tilsvarende .csv filer
def brandtilfil(brand):
    # Indslæser filen med et specifikt "brand" af biler ind i et dataframe 
    df = pd.read_csv(f"data/{brand}.csv", sep = ";", engine = "python")
    word_to_add = brand # Definere det ord der skal tilføjes til filen som "brand"
    df["brand"] = word_to_add # Tilføjer en kolone til .csv filen med titlen "brand" og indholdet "word_to_add"

    # Gemmer den nye .csv fil med det tilføjede brand
    df.to_csv(f"datany/{brand}ny.csv", sep = ";", )

# Køre funktionen "brandtilfil" for alle elemnter i listen "brand" så vi får en ny .csv fil for alle mærker    
for x in brand:
    brandtilfil(x)

# Definere de koloner vi vil gemme i et samlet datasæt
columns = ["model", "year", "price", "transmission", "mileage", "fuelType", "tax", "mpg", "engineSize", "brand"]
dfsaml = pd.DataFrame() # Opretter et pandas dataframe 

# Opretter en funktion til at samle datasætten til et datasæt
def datasaml(brand):
    global dfsaml 
    # Indlæser et datasæt ind i et pandas dataframe
    dfmerge = pd.read_csv(f"datany/{brand}ny.csv", sep = ";", engine = "python")
    # Samler begge dataframes til et samlet dataframe 
    dfsaml = pd.concat([dfsaml, dfmerge])

# Kører funktionen "datasaml" for alle elementer i "brands"
for x in brand:
    datasaml(x)
# Udvælger de koloner med det data vi vil have i vores samlede datasæt
dfsaml=dfsaml[columns]
# Gemmer det samlede dataframe som en .csv fil
dfsaml.to_csv("samletdata.csv", sep = ";", )
