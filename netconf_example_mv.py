#!/usr/bin/python3


from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
import json



router1 = {
   'name': 'R1-vXR',
   'host': '10.71.0.88',
   'port': '830',
   'username': 'xrv9000',
   'password': 'xrv9000',
   'platform': 'iosxr'
   }

router2 = {
   'name': 'R2-vEOS',
   'host': '10.71.0.200',
   'port': '830',
   'username': 'admin',
   'password': 'admin',
   'platform': 'default'
}

routers = []

routers.append(router1)
###routers.append(router2)

netconf_filter_1 = """
<filter>
      <interfaces xmlns="http://openconfig.net/yang/interfaces" />
</filter>
"""

netconf_filter_2 = """
<filter>
      <components xmlns="http://openconfig.net/yang/platform" />
</filter>
"""




for router in routers:
    with manager.connect(host=router['host'], port=router['port'], username=router['username'],password=router['password'], device_params={'name':router['platform']}, hostkey_verify=False) as m:
        filename = router['name'] + '.json'
        with open(filename,'w') as fw: 
            fw.write("INTERFACE DATA")
            data = m.get(netconf_filter_1)
            data_xml = xmltodict.parse(data.xml)["rpc-reply"]["data"]
            data_pretty = json.dumps(data_xml,indent=6)
            fw.write(data_pretty)

            fw.write("HW DATA")
            data = m.get(netconf_filter_2)
            data_xml = xmltodict.parse(data.xml)["rpc-reply"]["data"]
            data_pretty = json.dumps(data_xml,indent=6)
            fw.write(data_pretty)


