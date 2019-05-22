def trainvars():
    import slack
    import os
    import urllib.request
    import pandas as pd
    

    jtown = pd.read_html('https://apis.opendatani.gov.uk/translink/rendercis.asp?file=3044C2.xml',header=0,)

    stuff = jtown[0].values.tolist()

    try:
     train1 = stuff[0]
    except IndexError:
     train1 = ''

    try:
     train2 = stuff[2]
    except IndexError:
     train2 = ''

    try:
     train3 = stuff[4]
    except IndexError:
     train3 = ''

    dest = input("Where do you want to go? ")
    bfstrain = 0
    bfstrain1 = 0
    bfstrain2 = 0
    larne = 0
    larne1 = 0
    larne2 = 0
    whitehead = 0
    whitehead1 = 0
    whitehead2 = 0

    for x in stuff[0][1]:
     x
     if dest in ["Belfast","belfast"] and stuff[0][1] == "Great Victoria St":
       bfstrain = 1
     elif dest in ["Belfast","belfast"] and stuff[2][1] == "Great Victoria St":
       bfstrain1 = 1
     elif dest in ["Belfast","belfast"] and stuff[4][1] == "Great Victoria St":
       bfstrain2 = 1
     if bfstrain == 1:
       print("The next train from Jordanstown is the", train1[0], "Train to", train1[1], "on platform", train1[2])
       break
     elif bfstrain1 == 1:
         print("The next train from Jordanstown is the", train2[0], "Train to", train2[1], "on platform", train2[2])
         break
     elif bfstrain2 == 1:
         print("The next train from Jordanstown is the", train3[0], "Train to", train3[1], "on platform", train3[2])
         break
     if dest in ["larne","larne"] and x == "Larne Harbour":
       larne = 1
     elif dest in ["larne","Larne"] and stuff[2][1] == "Larne Harbour":
       larne1 = 1
     elif dest in ["larne","Larne"] and stuff[4][1] == "Larne Harbour":
       larne2 = 1
     if larne == 1:
       print("The next train from Jordanstown is the", train1[0], "Train to", train1[1], "on platform", train1[2])
       break
     elif larne1 == 1:
         print("The next train from Jordanstown is the", train2[0], "Train to", train2[1], "on platform", train2[2])
         break
     elif larne2 == 1:
         print("The next train from Jordanstown is the", train3[0], "Train to", train3[1], "on platform", train3[2])
         break
     if dest in ["whitehead","Whitehead"] and x == "Whitehead":
       whitehead = 1
     elif dest in ["whitehead","Whitehead"] and stuff[2][1] == "Whitehead":
       whitehead1 = 1
     elif dest in ["whitehead","Whitehead"] and stuff[4][1] == "Whitehead":
       whitehead2 = 1
     if whitehead == 1:
       print("The next train from Jordanstown is the", train1[0], "Train to", train1[1], "on platform", train1[2])
       break
     elif whitehead1 == 1:
         print("The next train from Jordanstown is the", train2[0], "Train to", train2[1], "on platform", train2[2])
         break
     elif whitehead2 == 1:
         print("The next train from Jordanstown is the", train3[0], "Train to", train3[1], "on platform", train3[2])
         break
    else: print(larne1)

trainvars()
#train4 = stuff[6]

#train5 = stuff[8]

#train6 = stuff[10]

#alltrains = train1,train2,train3

#destination1 = alltrains[0][1]

#destination2 = alltrains[1][1]

#destination3 = alltrains[2][1]

#destination4 = alltrains[4][1]

#destination5 = alltrains[5][1]

#alldestinations = destination1,destination2,destination3


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


#try:
#    trainbfs = stuff[0]
#except IndexError:
#    pass

#try:
#    train3 = stuff[4]
#except IndexError:
#    train3 = 'null'

#alltrains = train1,train2,train3

#print(trainbfs) #star removements list formatting
#print('The next train departing from Jordanstown is at', time, 'to', destination, 'from platform', platform)

#some other stuff try:
   # newlist.append(dlist[1])
#except IndexError:
 #   pass
#continue