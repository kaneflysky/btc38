#!/usr/bin/python
#  -*- coding: utf-8 -*-
# Created on 2015-07-22
# @author: kaneflysky
# @name: startGetInfo.py

import GetInfo
#import json
import MySQLdb
#import ConfigParser
import time
import datetime

#建立sql连接
conn=MySQLdb.connect( 
                     host="118.193.234.135", 
                     user="btc38", 
                     passwd="EZjNEsNBcWnfVJ", 
                     db="btc38", 
                     charset="utf8"
                     )
cursor=conn.cursor()
insert_btc38="insert into btc38Info(coin,holders,totalCoins,coinsPerHolders,inflow24H,outflow24H,change24H,inflowWeek,outflowWeek,changeWeek,top10,updateTime,updateTime2) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

coins = ['BTC','VPN','BLK','DOGE','BTS','NXT','YBC','XRP','TMC']
#coins = ['BTC']  #测试用

for coin in coins:
    coininfo=GetInfo.getInfo(coin)
    select_newtime="select updatetime from btc38info where coin = '"+ coin + "' order by updatetime desc limit 1"
    cursor.execute(select_newtime)
    sqltime=cursor.fetchall()
    #转换urltime字符串为datetime
    urltime = datetime.datetime.strptime(coininfo["updateTime"],"%Y-%m-%d %X")

    try:
        sqltime=sqltime[0][0]
    except:
        sqltime=1
        
    if (sqltime != urltime):
        param=(coin,coininfo["holders"],coininfo["totalCoins"],coininfo["coinsPerHolders"],coininfo["inflow24H"],coininfo["outflow24H"],coininfo["change24H"],coininfo["inflowWeek"],coininfo["outflowWeek"],coininfo["changeWeek"],coininfo["top10"],coininfo["updateTime"],coininfo["updateTime2"])
        try:
            cursor.execute(insert_btc38,param)
        except:
            print "error"
        time.sleep(0.5)

conn.close()

