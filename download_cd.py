# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 08:28:50 2016

@author: sindunuragarp
"""

import scrapper

title = "Coiling Dragon"
base = "http://www.wuxiaworld.com/cdindex-html/"
maxbook = 21    
    
def main():
    for book in range(1, maxbook+1):
        for chapter in range(1,100):
            url = base + "book-" + str(book) + "-chapter-" + str(chapter) + "/"
            filename = title + " - " + str(book) + ":" + str(chapter)
            xpath = '//div[@itemprop="articleBody"]/p/b//text() | //div[@itemprop="articleBody"]/p/strong//text() | //div[@itemprop="articleBody"]/p/span/text() | //div[@itemprop="articleBody"]/p/text()'
            if scrapper.save_text(url, xpath, title, filename) == False:
                break

if __name__ == "__main__":
    main()