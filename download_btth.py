# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 10:48:59 2016

@author: sindunuragarp
"""

import scrapper

title = "Battle Through The Heavens"
base = "http://www.wuxiaworld.com/btth-index/btth-chapter-"
maxchapter = 1000

def main():
    url = 'https://hellotranslations.wordpress.com/2015/01/30/dou-po-cang-qiong-chapter-1/'
    filename = title + " - " + str(1)
    xpath = '//div[@class="entry-content"]/p/text()'
    scrapper.save_text(url, xpath, title, filename)

    url = 'https://hellotranslations.wordpress.com/2015/02/08/dou-po-cang-qiong-chapter-2/'
    filename = title + " - " + str(2)
    xpath = '//div[@class="entry-content"]/p/text()'
    scrapper.save_text(url, xpath, title, filename)
    
    for chapter in range(3, maxchapter+1):
        url = base + str(chapter) + "/"
        filename = title + " - " + str(chapter)
        xpath = '//div[@itemprop="articleBody"]/p//strong//text() | //div[@itemprop="articleBody"]/h3/text() | //div[@itemprop="articleBody"]/p/span/text() | //div[@itemprop="articleBody"]/p/text()'
        if scrapper.save_text(url, xpath, title, filename) == False:
            break

if __name__ == "__main__":
    main()