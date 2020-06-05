##EDA AVCUOĞLU
##150709001

import os
import requests
import hashlib
import uuid

def download_file(urls):
    unique_hash = set()
    

    for url in urls:

        r = requests.get(url, allow_redirects=True)
        
        h = hashlib.sha256(r.content).hexdigest()

        
        if h not in unique_hash:
            
            unique_hash.add(h)
            file = str(uuid.uuid4())
            open(file, 'wb').write(r.content)

def child():
    urls = [
        "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
        "https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
        "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"
    ]
    download_file(urls)


childprocess_pid = os.fork()

if childprocess_pid == 0:

    child()

else:

    
    print(f"Child pid is {childprocess_pid}")

    os.wait()


print("Child process exited")


