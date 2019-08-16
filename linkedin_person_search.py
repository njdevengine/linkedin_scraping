#https://github.com/tomquirk/linkedin-api/blob/master/DOCS.md
#https://github.com/tomquirk/linkedin-api/blob/master/linkedin_api/linkedin.py
#https://github.com/tomquirk/linkedin-api/
from linkedin_api import Linkedin
api = Linkedin('login email','Password123$$')

search = api.search_people(
  keywords='company name,sales manager,account executive',
  industries=['43']
)

array = []
for i in range(len(search)):
    try:
        if search[i]['distance'] == "DISTANCE_3":
            pass
        else:
            print(search[i]['public_id'])
            array.append((search[i]['public_id']))
    except:
        pass
        
array2 = []
for i in array[:10]:
    data = api.get_profile(i)
    array2.append(data)
    
for i in array2:
    print(i["firstName"],i["lastName"],i["experience"][0]["companyName"])#i["headline"])
