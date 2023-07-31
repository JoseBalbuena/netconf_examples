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
   'password': 'xrv9000',
   'platform': 'iosxr'
}

m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':router['platform']}, hostkey_verify=False)

netconf_filter = """
<filter type='subtree'>
      <interfaces xmlns="http://openconfig.net/yang/interfaces" />
</filter>
"""

#Print Interfaces Data
print("INTERFACE DATA")
data = m.get(netconf_filter)
data_xml = xmltodict.parse(data.xml)["rpc-reply"]["data"]
data_pretty = json.dumps(data_xml,indent=6)
print(data_pretty)

m.close_session()
