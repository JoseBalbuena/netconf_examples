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
   'password': 'admin',
   'platform': 'default'
}

m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':router['platform']}, hostkey_verify=False)


route = """
<config>
    <network-instances xmlns="http://openconfig.net/yang/network-instance">
        <network-instance>
            <name>default</name>
            <protocols>
               <protocol>
                    <identifier>STATIC</identifier>
                    <name>STATIC</name>
                    <config>
                        <identifier>STATIC</identifier>
                        <name>STATIC</name>
                    </config>
                    <static-routes>
                        <static>
                            <prefix>100.100.100.100/32</prefix>
                            <config>
                                <prefix>100.100.100.100/32</prefix>
                            </config>
                            <next-hops>
                                <next-hop>
                                    <index>AUTO_1_10-71-0-80</index>
                                    <config>
                                        <index>AUTO_1_10-71-0-80</index>
                                        <metric>1</metric>
                                        <next-hop>10.71.0.80</next-hop>
                                    </config>
                                </next-hop>
                            </next-hops>
                        </static>
                    </static-routes>
               </protocol> 
            </protocols>
        </network-instance>
    </network-instances>
</config>
"""

#Print Running Config 
data = m.edit_config(target='running', config=route, default_operation="merge")
print(data)

m.close_session()
