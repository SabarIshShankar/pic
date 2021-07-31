import requests
import shutil
url= "https://portfolio.sabarishshankar.repl.co/images/5.png"
filename = url.split("/")[-1]
r = requests.get(url, stream = True)
if r.status_code == 200:
    r.raw.decode_content = True
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)   




