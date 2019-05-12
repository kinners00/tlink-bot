import bs4 as bs
import urllib.request
import pandas as pd

data = pd.read_html('https://apis.opendatani.gov.uk/translink/rendercis.asp?file=3044C2.xml',header=0,)


stuff = data[0].values.tolist()

train = stuff[0]

time = train[0]

destination = train[1]

platform = train[2]

status = train[4]

#print(data[0]) .values
print('The next train departing from Jordanstown is at', time, 'to', destination, 'from platform', platform)