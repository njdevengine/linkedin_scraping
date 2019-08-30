#using linkedin-api grabs profile info, takes in public profile id. this is like www.linkedin.com/in/***your_profile_name_11101***
from linkedin_api import Linkedin
api = Linkedin('your@email','your_pass!')

#get profiles from public ids, private ids will be included in results
import pandas as pd
df = pd.read_csv('linkedin_input.csv')

ids = list(df['id'])
profile_data = []

from random import randint
from time import sleep
        
for i in ids:
    profile_info = api.get_profile(i)
    print('getting',i)
    profile_data.append(profile_info)
    sleep(randint(2,6))
    
#keys returned: ['summary', 'industryName', 'lastName', 'locationName',
#'student', 'elt', 'industryUrn', 'firstName', 'entityUrn',
#'location', 'headline', 'displayPictureUrl', 'profile_id',
#'experience', 'skills', 'education']

ids = []
summaries = []
locations = []
headlines = []
current_company = []
industry = []
desc = []
title = []
first = []
last = []
for i in profile_data:
    ids.append(i["profile_id"])
    locations.append(i["locationName"])
    headlines.append(i["headline"])
    first.append(i["firstName"])
    last.append(i["lastName"])
    try:
        summaries.append(i["summary"])
        current_company.append(i['experience'][0]['companyName'])
        industry.append(i['industryName'])
        desc.append(i["experience"][0]['description'])
        title.append(i['experience'][0]['title'])
    except:
        summaries.append('')
        current_company.append('')
        industry.append('')
        desc.append('')
        title.append('')
        
dataframe = pd.DataFrame({'id':ids2,'first':first,'last':last,'location':locations,
                          'headline':headlines,'desc':desc,'title':title})
dataframe.to_csv('linkedin_profile_scrape.csv')

