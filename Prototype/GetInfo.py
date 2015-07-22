#!/usr/bin/python
#  -*- coding: utf-8 -*-
# Created on 2015-07-08
# @author: kaneflysky
# @name: GetInfo.py

import pycurl
import StringIO
import json
from datetime import *
import time
import MySQLdb #注：备用

def getInfo(coin):
    url = "http://btc38.com/trade/getCoinHold.php?coinname="  + coin
    crl = pycurl.Curl()
    crl.fp = StringIO.StringIO()
    crl.setopt(pycurl.URL, url)
    crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
    crl.perform()
    GetInfo = crl.fp.getvalue()
    coinInfo = json.loads(GetInfo)
    return coinInfo


