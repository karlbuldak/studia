import json

film={'title':'muminki',
      'long':True,
      'fun':True,
      'for kids':True,
      'actors':['muminek','mama muminek']
    }

file=open('fav.json','w')
content=json.dumps(film,indent=4)
file.write(content)
file.close()
