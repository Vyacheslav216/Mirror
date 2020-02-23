#!/usr/bin/python3
#from bs4 import BeautifulSoup
import bs4
import requests
import urllib.request
#import cairosvg


def gettemp():

   s=requests.get('https://yandex.ru/pogoda/saint-petersburg')
   soup = bs4.BeautifulSoup(s.text,"html.parser")
   day=[]
   night=[]
   
   s=""
   i=0
   for hit in soup.find_all(class_ ='temp__value'):
   	if i>3 and i<18:
   		s+="\n"
   		s+=" ".join(hit.contents)
   		if i%2==0:
   		  day.append(hit.contents)
   		else:
   		  night.append(hit.contents)
   	i+=1
   i=0
   pic=[]
   for a in soup.find_all(class_="forecast-briefly__condition"):
     if(i<7):
      pic.append(a.contents)
     i+=1
   return {'day':day,'night':night,'pic':pic}
 #  print(s)
  # print(len(s))
  #for i in range(0,len(pic)):
   # s="imageW/"+str(i)+".png"
    #urllib.request.urlretrieve(pic[i],s )
   # cairosvg.svg2png(url=pic[i],write_to=s)
gettemp()