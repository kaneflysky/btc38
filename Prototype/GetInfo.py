#!/usr/bin/python
#  -*- coding: utf-8 -*-
# Created on 2015-07-08
# @author: kaneflysky
# @name: GetInfo.py

import pycurl
import StringIO
import json

def getInfo(coin,mode='Large'):
    if (mode == 'Large'): #Large=大户持仓
        url = "http://btc38.com/trade/getCoinHold.php?coinname="  + coin
    elif (mode == 'Price'):  #Price=价格
        url = "http://api.btc38.com/v1/ticker.php?c=all&mk_type="  + coin
    else:
        return 'error'
    crl = pycurl.Curl()
    crl.fp = StringIO.StringIO()
    crl.setopt(pycurl.URL, url)
    crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
    crl.perform()
    GetInfo = crl.fp.getvalue()
    coinInfo = json.loads(GetInfo)
    return coinInfo


