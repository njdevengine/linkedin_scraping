from linkedin_api import Linkedin
api = Linkedin('email','pass')

#get 10 people from a search. keywords comma separated.
search = api.search_people(
  keywords='company,sales manager,account executive',
    current_company ='company name',
  industries=['43'],
    limit=10
)

#fuzzy match company name

from fuzzywuzzy import fuzz
for i in array2:
#     print(i["firstName"],i["lastName"],i["experience"][0]["companyName"])#i["headline"])
    if fuzz.token_sort_ratio(i["experience"][0]["companyName"],"the company name") >=84:
        print(i["experience"][0]["companyName"])
        print(i["headline"])
        
#get a profile       
profile_info = api.get_profile_contact_info('profile-public-name-64962376')
