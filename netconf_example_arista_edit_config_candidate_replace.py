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
                            <prefix operation="replace">100.100.100.100/32</prefix>
                            <config>
                                <prefix operation="replace">100.100.100.100/32</prefix>
                            </config>
                            <next-hops>
                                <next-hop>
                                    <index operation="replace">AUTO_1_10-71-0-100</index>
                                    <config>
                                        <index operation="replace">AUTO_1_10-71-0-100</index>
                                        <metric>1</metric>
                                        <next-hop operation="replace">10.71.0.100</next-hop>
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

#Lock Candidate Config 
print('Lock Candidate Conf')
data = m.lock('candidate')
print(data)

#Lock Running Config
print('Lock Running Conf')
data = m.lock('running')
print(data)

#Replace
data = m.edit_config(target='candidate', config=route, default_operation="none")
print(data)

#Commit
data = m.commit()
print(data)

#Unlock Candidate
data = m.unlock('candidate')
print(data)

#Unlock Running
data = m.unlock('running')
print(data)


m.close_session()
