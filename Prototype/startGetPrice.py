#!/usr/bin/python
#  -*- coding: utf-8 -*-
# Created on 2015-08-18
# @author: kaneflysky
# @name: startGetPrice.py

import GetInfo
import MySQLdb
#import ConfigParser
import time
import datetime
from _elementtree import tostring

#建立sql连接
conn=MySQLdb.connect( 
                     host="118.193.234.135", 
                     user="btc38", 
                     passwd="EZjNEsNBcWnfVJ", 
                     db="btc38", 
                     charset="utf8"
                     )
cursor=conn.cursor()

insert_price="insert into btc38Price(Currency,Coin,Price_cny,Vol,InsertTime) values(%s,%s,%s,%s,now())"

Currencys = {"CNY":['btc','doge'], "BTC":['vpn','doge']}
btcPrice=GetInfo.getInfo('cny','Price')['btc']["ticker"]["last"]
for (Currency,coins) in Currencys.items():
    Prices=GetInfo.getInfo(Currency,'Price')
    for coin in coins:
        if (Currency=='BTC'):
            price=Prices[coin]["ticker"]["last"]*btcPrice
        else:
            price=Prices[coin]["ticker"]["last"]
        param=(Currency,coin,price,Prices[coin]["ticker"]["vol"])
        try:
            cursor.execute(insert_price,param)
        except:
            print "error"
        

    time.sleep(0.5)
        
        
        