

import requests
from pprint import pprint 
import json

class API_VK:
  def __init__(self,file):
    with open('file.txt', 'r') as f:
      token = f.read().strip()
    self.token = token

  def get_photos(self):
    URL = 'https://api.vk.com/method/photos.get'
    params = {
      'owner_id': '552934290',
      'album_id': 'profile',
      'extended': '1', 
      'photo_sizes': '1', 
      'v':'5.131', 
      'access_token': self.token}
    res = requests.get(URL, params=params)
    global res_json
    res_json = res.json()
    pprint(res_json)

    data_list =[]
    for item in res_json['response']['items']:
        pprint(item)
        data_dict = {}
        size_list = []
        
        # print(len(size_list))
        data_dict['file_name'] = str(item['likes']['count']) + '.jpg'
        
        if len(item['sizes']) == len(size_list):
          max_size = max(size_list)
          # print(max_size)
          index = int(size_list.index(max_size))
          data_dict['file_name'] = str(item['likes']['count']) + '.jpg'
          data_dict['path'] = item['sizes'][index]['url']
          data_dict['size'] = item['sizes'][index]['type']
          data_list.append(data_dict)

        else:
            # size in item['sizes']  
          p = int(item['sizes']['height'])*int(item['sizes']['width'])
          print(int(p))
          size_list.append(int(p)) 
            
            


        if size['type'] == 'w': 
                # or size['type'] == 'z' or size['type'] == 'y' or size['type'] == 'q' or size['type'] == 'p' or size['type'] == 'o' or size['type'] == 'x' or size['type'] == 'm' or size['type'] == 's':    
                data_dict['path'] = size['url']
                data_dict['size'] = size['type']
                data_list.append(data_dict)
                break
            elif size['type'] == 'z':
                data_dict['path'] = size['url']
                data_dict['size'] = size['type']
                data_list.append(data_dict)
                break
            elif size['type'] == 'y':
                data_dict['path'] = size['url']
                data_dict['size'] = size['type']
                data_list.append(data_dict)
                break
            elif size['type'] == 'q':
                data_dict['path'] = size['url']
                data_dict['size'] = size['type']
                data_list.append(data_dict)
                break

            elif size['type'] == 'p':
                data_dict['path'] = size['url']
                data_dict['size'] = size['type']
                data_list.append(data_dict)
                break
            elif size['type'] == 'o':
                data_dict['path'] = size['url']
                data_dict['size'] = size['type']
                data_list.append(data_dict)
                break
            elif size['type'] == 'x':
                data_dict['path'] = size['url']
                data_dict['size'] = size['type']
                data_list.append(data_dict)
                break
            elif size['type'] == 'm':
                data_dict['path'] = size['url']
                data_dict['size'] = size['type']
                data_list.append(data_dict)
                break
            elif size['type'] == 's':
                data_dict['path'] = size['url']
                data_dict['size'] = size['type']
                data_list.append(data_dict)
                break
                
            
            
    pprint(data_list)
    # pprint(data_dict)
        
    return data_list 


if __name__ == '__main__':

    login = API_VK('file.txt')
    get_photos = login.get_photos()
