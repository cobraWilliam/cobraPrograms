'''find the distance from the CINC'''
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

cincDefault = '1777 Exposition Drive, Boulder, CO 80301'
subjectAddr = input('Please enter a subject address: ')
df = [[cincDefault, subjectAddr]]

df = pd.DataFrame(df, columns=['Address 1', 'Address 2'])
df.to_string(index=False)
emailAdd   = input("Please enter a valid lab email address:")
geolocator = Nominatim(user_agent=emailAdd)

df["Cor1"] = df["Address 1"].apply(geolocator.geocode)
df["Cor2"] = df["Address 2"].apply(geolocator.geocode)

df["lat1"] = df["Cor1"].apply(lambda x: x.latitude if x != None else None)
df["lon1"] = df["Cor1"].apply(lambda x: x.longitude if x != None else None)
df["lat2"] = df["Cor2"].apply(lambda x: x.latitude if x != None else None)
df["lon2"] = df["Cor2"].apply(lambda x: x.longitude if x != None else None)

def distance(row):
    address1 = (row["lat1"], row["lon1"])
    address2 = (row["lat2"], row["lon2"])
    return (geodesic(address1, address2).miles)

df["dist"] = df.apply(lambda row: distance(row), axis=1)

distanceMiles = (df["dist"].to_string(index=False))
prettyMiles   = (round(float(distanceMiles), 2))

print('\n')
print('The subject lives', prettyMiles, 'geodesic miles from CINC.')
 
    
        
        


