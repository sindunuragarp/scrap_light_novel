# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 06:24:50 2016

@author: sindunuragarp
"""

import scrapper

title = "Tales of Demons and Gods"
base = "http://www.wuxiaworld.com/tdg-index/tdg-chapter-"
maxchapter = 1000
    
def main():
    for chapter in range(1,maxchapter):
        url = base + str(chapter) + "/"
        filename = title + " - " + str(chapter)
        xpath = '//div[@itemprop="articleBody"]/p/strong//text() | //div[@itemprop="articleBody"]/p/span/text() | //div[@itemprop="articleBody"]/p/text()'
        if scrapper.save_text(url, xpath, title, filename) == False:
            break

if __name__ == "__main__":
    main()