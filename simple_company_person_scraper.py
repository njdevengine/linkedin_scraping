from random import randint
from time import sleep
frames = []
for i in companies:
    print('getting',i)
    search = api.search_people(
      keywords=str(i),
      industries=['43'],
        limit=100)
    ab = pd.DataFrame([search])
    ab = ab.transpose()
    ab["company"] = str(i)
    frames.append(ab)
    ab.to_csv(r'linkedin_companies\\'+i+'.csv')
    sleep(randint(2,10))
