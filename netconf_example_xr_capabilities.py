#!/usr/bin/python3


from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
import json

router = {
   'host': '10.71.0.88',
   'port': '830',
   'username': 'xrv9000',
   'password': 'xrv9000'
}

m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'default'}, hostkey_verify=False)



#Print Capabilities 
for capability in m.server_capabilities:
    print('*'*50)
    print(capability)



m.close_session()
