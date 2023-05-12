#This sketch has a problems 

#soup.title
# <title>The Dormouse's story</title>

#soup.title.name
# u'title'

#soup.title.string
# u'The Dormouse's story'

#soup.title.parent.name
# u'head'

#soup.p
# <p class="title"><b>The Dormouse's story</b></p>

#soup.p['class']
# u'title'

#soup.a
# <a class="sister" href="http://example.com/                                                                                                                        elsie" id="link1">Elsie</a>

#soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#soup.find(id="link3+")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

import io, sys, random, requests
from bs4 import BeautifulSoup 
import pandas as pars


url = "https://techarks.ru/qa/python/oshibka-trassirovki-python-pr-X9/" # url

user_agents = [
           "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Safari/537.36",
           "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Safari/537.36"
           ]

random_user_agent = random.choice(user_agents)
       
headers = {
      
           'User-Agent': random_user_agent, 
         
         }

response = requests.get(url, headers=headers)

print("Status code"+"["+url+"]"+":", response.status_code) 


if response.status_code == 200: 
      
  def par():     
      
      a = BeautifulSoup(response.text, 'lxml')
      
      #soup = a.findAll('blockSettingArray')
      
      #soup_html = a.find_all({'meta'}) 
     

      #soup = a('meta', 'content')
      
      soup = a.findAll('p')
      
      with io.open("comment.txt", 'w', encoding='utf-8') as f: 
            var = f.write(str(soup))
            
      with io.open("comment.txt", 'r', encoding='utf-8') as f: 
           var = f.read()
           soup = var.replace('meta content', '')
           
      with io.open('comment.html', 'w', encoding= 'utf-8') as f: 
           f.write(str(soup)) 
           

      
  par()
  
           
      
else: 
      sys.exit() 
      
