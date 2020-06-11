import json
import time
import hashlib
import time
from datetime import datetime
from requests import get

def GetPic():
    
    local_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S+08:00')
    Hash = hashlib.md5((local_time + hash_secret).encode('utf-8')).hexdigest()
    print(local_time)
    print(Hash)
    api_url = r'https://api.lolicon.app/setu/?apikey=962440885eb117e14f71d1'
    api = get(api_url)
    json_data = json.loads(api.text)
    pic_url = json_data['data'][0]['url']
    pid = json_data['data'][0]['pid']
    open(r'./json/{0}.json'.format(pid), 'wb').write(api.content)
    print('Create Json Success!')
    pic = get(pic_url, stream=True)
    if(pic.status_code == 200):
        open(r'./pic/{0}.jpg'.format(pid), 'wb').write(pic.content)
        print('Create Image Success!')
    else:
        print('Create Image Faild!')

if __name__ == "__main__":
    GetPic()
