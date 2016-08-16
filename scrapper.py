# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:36:52 2016

@author: sindunuragarp
"""

from lxml import html
import requests
import os

download_folder = "Downloads"

def save_text(url, xpath, directory, filename): 
    lines = scrap_text(url, xpath)
    if lines == False:
        return False
                
    directory_path = download_folder + "/" + directory
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        
    file_path = directory_path + "/" + filename + " - " + lines[0]
    f = open(file_path, "w")    
    
    for text in lines:
        f.write(text + "\n\n")
        
    f.close()
    return True    

def scrap_text(url, xpath):
    page = requests.get(url)
    print url
    
    if page.status_code != 200:
        return False
    
    tree = html.fromstring(page.content)
    text = tree.xpath(xpath)
    text = filter(lambda item: item != " ", text)
    text = filter(lambda item: item != "", text)
    text = filter(lambda item: item != "\n", text)
    text = filter(lambda item: item != unichr(160), text)
           
    return text