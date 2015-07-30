#!/usr/bin/python
#  -*- coding: utf-8 -*-
# Created on 2015-07-22
# @author: kaneflysky
# @name: startGetInfo.py

import GetInfo
import json

coins = ['btc','vpn']
for coin in coins:
    coininfo = GetInfo.getInfo(coin)
    print coin
    print coininfo["updateTime2"]
    print coininfo["updateTime"]

