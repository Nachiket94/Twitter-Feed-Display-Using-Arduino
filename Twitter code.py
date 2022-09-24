import urllib3
import serial
import time
import feedparser
from xml.dom import minidom
from xml.dom.minidom import parseString
import string
import xml.etree.ElementTree as ET
import os
import tweepy
from dotenv import load_dotenv
# from dicttoxml import dicttoxml
import sched

s = sched.scheduler(time.time, time.sleep)


consumer_key = 'Flv9uubVy6Ex1f7QxwsOeIS1N'
consumer_secret = 'yj7pCXn1DY5AMpcC2kQ8R4U2ZVcaWUAcplaqhyHtKB90WEqiEQ'
access_token = '1263383185313988609-JuH8ZyfB6y0vJOT9ykwCesLE2LAPxl'
access_token_secret = 'Ib5AoiZ3kPdHoGMZe354RvQjjhvshL22sEgySFWgvMosB'

auth = tweepy.OAuth1UserHandler(
  consumer_key, 
  consumer_secret, 
  access_token, 
  access_token_secret
)
api = tweepy.API(auth)
tweets = api.home_timeline(count = 5,trim_user = True)

final_tweets = []
for f_tweet in tweets:
  if(f_tweet.lang == 'en'):
    final_tweets.append(f_tweet.text)


def create_xml():
    usrconfig = ET.Element("usrconfig")
    usrconfig = ET.SubElement(usrconfig, "usrconfig")
    for user in range(len(final_tweets)):
        usr = ET.SubElement(usrconfig, "usr")
        usr.text = str(final_tweets[user])
    tree = ET.ElementTree(usrconfig)
    tree.write("Output.xml", encoding='utf-8', xml_declaration = True)
create_xml()
s.enter(60,1,create_xml())

i = 1
while i == 1:
     ser = serial.Serial()
     ser.__init__(port="COM3",baudrate = 9600)
     file = ET.parse('Output.xml')
     root = file.getroot()
     print(root)
     for tweet_text in root:
          print(tweet_text.text)
          ser.write(str.encode('~'))
          nums = tweet_text.text.split(' ')
          for num in nums:
            ser.write(str.encode(num))
            ser.write(str.encode(' '))
            time.sleep(1)
          ser.write(str.encode('~'))
           # if(tweet_text.text == "Water Plants"):
          #   print("jwvbv")
          #   ser.write(str.encode('*'))
          # if(f_tweet.text == "Turn On Fan"):
          #   ser.write(str.encode('|'))
          # elif(f_tweet.text == "Turn Off Fan"):
          #   ser.write(str.encode('='))
          # elif(f_tweet.text == "Turn On Light"):
          #   ser.write(str.encode('+'))
          # elif(f_tweet.text == "Turn Off Light"):
          #   ser.write(str.encode('_'))
          # else:
          #   print("Complete")
          time.sleep(20)       