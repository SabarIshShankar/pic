import requests
import shutil
url= "https://s3.amazonaws.com/www-inside-design/uploads/2019/07/anatomy-of-ux-case-study-details-sarah-doody.png"
filename = url.split("/")[-1]
r = requests.get(url, stream = True)
if r.status_code == 200:
    r.raw.decode_content = True
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)   




