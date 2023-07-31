#!/usr/bin/python3


from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
import json

router = {
   'host': '10.71.0.88',
   'port': '830',
   'username': 'root',
   'password': 'xrv9000',
   'platform': 'iosxr'
}

m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':router['platform']}, hostkey_verify=False)

#Print Running Config 
data = m.get_config('running')
print(data)
data_xml = xmltodict.parse(data.xml)["rpc-reply"]["data"]
data_pretty = json.dumps(data_xml,indent=6)
print(data_pretty)

#Print Candidate Config
data = m.get_config('candidate')
data_xml = xmltodict.parse(data.xml)["rpc-reply"]["data"]
data_pretty = json.dumps(data_xml,indent=6)
print(data_pretty)


m.close_session()
