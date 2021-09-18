import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
import ssl
import csv

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://nclt.gov.in/all-couse-list?field_nclt_benches_list_target_id=All&field_cause_date_value=09%2F09%2F2021&field_cause_date_value_1=09%2F16%2F2021'
html = urllib.request.urlopen(url, context=ctx).read()
# r = requests.get(url)
soup = BeautifulSoup(html, 'html.parser')

filename = 'test.csv'

csv_writer = csv.writer(open(filename,'w'))

#run a for loop to extract the table data and store it in csv file

for tr in soup.find_all('tr'):
    data = []

    #for extracting the table heading this will execute only once

    for th in tr.find_all('th'):
        data.append(th.text)

    if(data):
        print("Inserting headers: {}".format('  '.join(data)))
        csv_writer.writerow(data)
        continue

    #for scrapping the actual table data values

    for td in tr.find_all('td'):
        data.append(td.text.strip())

    if(data):
        print("Inserting Table Data:{}".format('\n  '.join(data)))
        csv_writer.writerow(data)



# nclt_table = soup.find('table', class_ ="views-table views-view-table cols-6")
# for Title in nclt_table.find_all('tbody'):
#     rows = Title.find_all('tr')
#     for row in rows:
#         Court = row.find('td', class_ = 'views-field views-field-field-nclt-benches-list').text.strip()
#         print(Court)