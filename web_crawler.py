#Finish crawl web https://www.udacity.com/cs101x/index.html

import urllib

def get_page(url):                       # get one page of html code
    page = urllib.urlopen(url).read()
    return page

def get_next_target(page):              # get the first/next link in source code of variable "page"
      
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link) #start search for " from psoition "startling" 
    end_quote = page.find('"', start_quote + 1) 
    url = page[start_quote + 1:end_quote]  #+1 so as to not capture the " ie start at HTTP
    print url
    return url, end_quote

#get_next_target("https://www.udacity.com/cs101x/index.html")

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):                    # get all the link on page by getting one at a time and storing the links
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    print links
    return links


def crawl_web(initialurl,max_pages):
    tocrawl = [initialurl]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages:
          union (tocrawl,get_all_links(get_page(page)))  
          crawled.append(page)
    return crawled 
crawl_web("https://www.udacity.com/cs101x/index.html",10)
