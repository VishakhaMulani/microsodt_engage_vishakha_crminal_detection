# -*- coding: utf-8 -*-
"""
Created on Sat May 28 22:51:21 2022

@author: 91935
"""

from twilio.rest import Client
from datetime import datetime

def sendMsg(name):              
   now=datetime.now() 
   current_time = now.strftime("%H:%M:%S")            
   msg = name+ "has been spotted at" + current_time +"in live cam"  
   account_sid = "ACd146a345d80ddfdd51d83feb7f329423"
   auth_token = "c13eebf2a819e723a93f3cded04de71b"
   client = Client(account_sid, auth_token)  
   message = client.messages.create(
            to="+919351191455",
            from_="+12055573573",
            body=msg)

   print(message.sid)