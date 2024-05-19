# Importer pandas til læse og tilføje data til vores datasæt
import pandas as pd

# Opretter en liste med navne på de mærker vi arbejder med
brand = ["audi", "bmw", "ford", "hyundai", "mercedes", "skoda", "toyota", "vauxhall", "vw"]

# liste til at holde dataframesne med en tilføjet kolonne
brands_df = []
# Opretter en funktion til tilføje mærket til de tilsvarende .csv filer
def kollonne_tilføjer(brand):
    # Indslæser filen med et specifikt "brand" af biler ind i et dataframe 
    df = pd.read_csv(f"data/{brand}.csv", sep = ";", engine = "python")
    df["brand"] = brand # Tilføjer en kolone til .csv filen med titlen "brand" og indholdet funktions argumentet "brand"

    # gemmer den nye dataframe i listen
    brands_df.append(df)

# Køre funktionen "brandtilfil" for alle elemnter i listen "brand" så vi får en ny .csv fil for alle mærker    
for x in brand:
    kollonne_tilføjer(x)

dfsaml = pd.DataFrame() # Opretter et pandas dataframe 

# Opretter en funktion til at samle datasætten til et datasæt
def datasaml(dfmerge):
    global dfsaml 
    # Samler begge dataframes til et samlet dataframe 
    dfsaml = pd.concat([dfsaml, dfmerge])

# Kører funktionen "datasaml" for alle elementer i "brands"
for df in brands_df:
    datasaml(df)
# Definere de koloner vi vil gemme i et samlet datasæt
columns = ["model", "year", "price", "transmission", "mileage", "fuelType", "tax", "mpg", "engineSize", "brand"]
# Udvælger de koloner med det data vi vil have i vores samlede datasæt
dfsaml=dfsaml[columns]
# Gemmer det samlede dataframe som en .csv fil
dfsaml.to_csv("samletdata.csv", sep = ";", )
