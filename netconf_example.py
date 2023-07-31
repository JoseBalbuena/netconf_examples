#!/usr/bin/python3


from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
import json

router = {
   'host': '10.71.0.200',
   'port': '830',
   'username': 'admin',
   'password': 'admin'
}

m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'default'}, hostkey_verify=False)

netconf_filter_1 = """
<filter type='subtree'>
      <interfaces xmlns="http://openconfig.net/yang/interfaces" />
</filter>
"""

netconf_filter_2 = """
<filter>
      <components xmlns="http://openconfig.net/yang/platform" />
</filter>
"""


#Print Capabilities 
for capability in m.server_capabilities:
    print('*'*50)
    print(capability)


#Print Interfaces Data
#print("INTERFACE DATA")
#data = m.get(netconf_filter_1)
#data_xml = xmltodict.parse(data.xml)["rpc-reply"]["data"]
#data_pretty = json.dumps(data_xml,indent=6)
#print(data_pretty)

#Print HW Data
#print("HW DATA")
#data = m.get(netconf_filter_2)
#data_xml = xmltodict.parse(data.xml)["rpc-reply"]["data"]
#data_pretty = json.dumps(data_xml,indent=6)
#print(data_pretty)




m.close_session()
