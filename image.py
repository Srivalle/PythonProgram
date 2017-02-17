from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
import os

base_url = "https://apod.nasa.gov/apod/archivepix.html"
download_dir="C:\\Srivalle111416\\PythonProgram"
content =urllib.request.urlopen(base_url).read()
for link in BeautifulSoup(content,"lxml").findAll("a"):
    print("Follwing link" ,link)
    href=urljoin(base_url,link["href"])
    content =urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content,"lxml").findAll("img"):
        img_href =urljoin(href,img["src"])
        #print("img_href" , img_href)
        print("Downloading Image :",img_href)
        img_name= img_href.split("/")[-1]
        print("img_name" , img_name)
        urllib.request.urlretrieve(img_href,download_dir +"\\" + img_name)
    
