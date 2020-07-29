import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
desired_width = 400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',None)

URL = 'https://www.freshoffthegrid.com/backpacking-food-ideas-trader-joes/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

heads = soup.find_all("h2")
df = pd.DataFrame(columns = ['Section','Item','Calories/oz','Fat/oz','Carbs/oz','Protein/oz'])
for section in soup.find_all("h2")[:-4]:
    if section.get_text(strip=True) != '' and section.get_text(strip=True) != '35 Comments':
        text = []
        #print(section.get_text())
        for sib in section.next_siblings:
            if sib.name == 'p':
                text.append(sib.get_text())
            elif sib.name == 'h2':
                break
        #print(text[1:3])
        for item in text[1:]:
            list = []
            list.append(section.get_text())
            #print(item.split('\n'),'\n')
            list.append(item.split('\n')[0])
            #print(item.split('\n')[1].split(' | '))
            for x in item.split('\n')[1].split('|'):
                list.append(x.strip())
            #print(list,'\n')
            df = df.append(pd.Series(list, index = df.columns), ignore_index=True)

pattern = '|'.join(['Calories per oz:','Aprox.','Fat per oz:','Carb per oz:','Protein per oz', ':'])

df['Calories/oz'] = df['Calories/oz'].str.replace(pattern,'').astype('float')
df['Fat/oz'] = df['Fat/oz'].str.replace(pattern,'').astypdf['Carbs/oz'] = df['Carbs/oz'].str.replace(pattern,'').astype('float')
df['Protein/oz'] = df['Protein/oz'].str.replace(pattern,'').astype('float')e('float')


print(df)
df.to_csv(r'X:\AC\Documents\Datasets\Nutritional Facts\Fresh_OTG_TJs_Backpacking_Foods.csv')