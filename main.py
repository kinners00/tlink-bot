import bs4 as bs
import urllib.request
import pandas as pd

data = pd.read_html('https://apis.opendatani.gov.uk/translink/rendercis.asp?file=3044C2.xml',header=0,)


stuff = data[0].values.tolist()

#train1 = stuff[0]

#train2 = stuff[2]

#train3 = stuff[4]

#train4 = stuff[6]

#train5 = stuff[8]

#train6 = stuff[10]

#alltrains = train1,train2,train3

#destination1 = alltrains[1][1]

#destination2 = alltrains[2][1]

#destination3 = alltrains[3][1]

#destination4 = alltrains[4][1]

#destination5 = alltrains[5][1]

#alldestinations = destination1,destination2


#time = train[0]

#destination = train[1]

#platform = train[2]

#status = train[4]

#print(data[0]) .values

#fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

#fish_list = [fish for fish in fish_tuple if fish != 'octopus']
#print(fish_list)


#locations = [loc for loc in alltrains[0][3] if loc != nan]
#$print(locations)

#trolley = []

#if train2[1] == 'Whitehead':
#        print("BOOM son")
#else:
#    print("shit one")

try:
    train1 = stuff[0]
except IndexError:
    pass

#try:
#    train3 = stuff[4]
#except IndexError:
#    train3 = 'null'

#alltrains = train1,train2,train3

print(train1) #star removements list formatting
#print('The next train departing from Jordanstown is at', time, 'to', destination, 'from platform', platform)

#some other stuff try:
   # newlist.append(dlist[1])
#except IndexError:
 #   pass
#continue