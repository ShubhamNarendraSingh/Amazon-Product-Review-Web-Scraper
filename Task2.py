import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
import ssl
import pandas as pd

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.amazon.in/DABUR-Organic-Honey-300-g/dp/B088DWCBZW?th=1'
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

names = soup.find_all('span',class_='a-profile-name')

print(len(names))

cust_name = []
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())

title = soup.find_all('a',class_='review-title-content')

review_title = []
for i in range(0,len(title)):
    review_title.append(title[i].get_text())

review_title[:] = [titles.lstrip('\n') for titles in review_title]

review_title[:] = [titles.rstrip('\n') for titles in review_title]

print(len(review_title))

rating = soup.find_all('i',class_="review-rating")

rate = []
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())

print(len(rate))

review = soup.find_all("span",{"data-hook":"review-body"})

rbody = []
for i in range(0,len(review)):
    rbody.append(review[i].get_text())

rbody[:] = [review.lstrip('\n\n') for review in rbody]

rbody[:] = [review.rstrip('\n\n') for review in rbody]

print(len(rbody))

print(cust_name,review_title,rate,rbody)

# csv- comma seperated value
df = pd.DataFrame()

df['Customer Name']=cust_name
print(df)

df['Review Title']=review_title
df['Ratings']=rate
df['Reviews']=rbody
print(df)

df.to_csv(r'D:\Web_Internship_Tasks\reviews.csv',index=True)