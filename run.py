rota = [
    {
        'source':'JPN',
        'destination':'PHL'
    },
     {
        'source':'BRA',
        'destination':'UAE'
    },
     {
        'source':'USA',
        'destination':'BRA'
    },
     {
        'source':'UAE',
        'destination':'JPN'
    }]

begin = rota[0]['source']
v = 0

for i in range(0, len(rota)):
    if(rota[i]['destination'] == begin):
        begin = rota[i]['source']
        while(v<len(rota)):
            if(begin == rota[v]['destination']):
                begin = rota[v]['source']
                v=0
            else:
                v +=1
v=0
for i in range(0, len(rota)):
    if(rota[i]['source'] == begin):
        print("Begin:" + begin)
        begin = rota[i]['destination']
        print("Destination: "+ begin)
        while(v<len(rota)):
            if(begin == rota[v]['source']):
                print('Source: '+ begin)
                begin = rota[v]['destination']
                print('Destination: '+ begin)
                v=0
            else:
                v +=1