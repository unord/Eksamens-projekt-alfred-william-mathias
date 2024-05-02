import pandas as pd
brand = ["audi","bmw","ford","hyundai","mercedes","skoda","toyota","vauxhall","vw"]
def brandtilfil(brand):
    df = pd.read_csv(f"data\{brand}.csv", 
                    sep = ';', 
                    engine = 'python')
    word_to_add = brand
    df['brand'] = word_to_add

    df.to_csv(f"datany\{brand}ny.csv", 
                    sep = ';', )
    
for x in brand:
    brandtilfil(x)

columns = ['model', 'year', 'price', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize', 'brand']
dfsaml = pd.DataFrame()

def datasaml(brand):
    global dfsaml
    dfmerge = pd.read_csv(f"datany\{brand}ny.csv", 
                    sep = ';', 
                    engine = 'python')
    
    dfsaml = pd.concat([dfsaml, dfmerge])

for x in brand:
    datasaml(x)
dfsaml=dfsaml[columns]
dfsaml.to_csv("samletdata.csv", 
                    sep = ';', )