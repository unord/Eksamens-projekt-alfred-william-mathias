# Importer pandas til læse og tilføje data til vores datasæt
import pandas as pd

# Opretter en liste med navne på de mærker vi arbejder med
brand = ["audi", "bmw", "ford", "hyundai", "mercedes", "skoda", "toyota", "vauxhall", "vw"]

# liste til at holde dataframes med en tilføjet kolonne
brands_df = []
# Opretter en funktion til tilføje mærket til de tilsvarende dataframes
def kollonne_tilføjer(brand):
    # Indslæser filen med et specifikt "brand" af biler ind i et dataframe 
    df = pd.read_csv(f"data/{brand}.csv", sep = ";", engine = "python")
    df["brand"] = brand # Tilføjer en kolone til dataframet med titlen "brand" og indholdet funktions argumentet "brand"

    # gemmer den nye dataframe i listen
    brands_df.append(df)

# Køre funktionen "kollonne_tilføjer" for alle elementer i listen "brand" sådan at vi gemmer brandet med i dataframet    
for x in brand:
    kollonne_tilføjer(x)

# samler dataframesne i et
dfsaml = pd.concat(brands_df) # Opretter et pandas dataframe 

# Definere de koloner vi vil gemme i et samlet datasæt
columns = ["model", "year", "price", "transmission", "mileage", "fuelType", "tax", "mpg", "engineSize", "brand"]
# Udvælger de koloner med det data vi vil have i vores samlede datasæt
dfsaml=dfsaml[columns]
# Gemmer det samlede dataframe som en .csv fil
dfsaml.to_csv("samletdata.csv", sep = ";", )