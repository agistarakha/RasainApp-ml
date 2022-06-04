import requests
import json
import re

food = 'onde-onde'
search_keyword = 'onde+onde+mini+kering'
page = '0'
region = '&gl=id'
# region = ''
api_key = ''


def download_pic(pic_url, name):
    with open(food+'/'+name+'.png', 'wb') as handle:
        response = requests.get(pic_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

# api_url = 'https://masak-apa-tomorisakura.vercel.app/api/search/?q='+keyword


api_url = 'https://serpapi.com/search.json?q={}&tbm=isch&ijn={}&api_key={}{}'.format(
    search_keyword, page, api_key, region)
res = requests.get(api_url)
res_json = res.json()
counter = 0
links = []
with open(food+'.txt', 'r') as link_file:
    links = link_file.readlines()

counter = len(links)
for resep in res_json['images_results']:
    # if(re.search(keyword,resep['key'])):
    # counter += 1
    with open(food+'.txt', 'a') as link_file:
        if(resep['original']+'\n' not in links):
            link_file.write(resep['original']+'\n')
            download_pic(resep['thumbnail'], str(counter))
            counter += 1

# print(links)
# print(counter)

# for link in links:
#     download_pic(link.strip(),str(counter))
#     counter += 1
