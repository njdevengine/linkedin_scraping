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

