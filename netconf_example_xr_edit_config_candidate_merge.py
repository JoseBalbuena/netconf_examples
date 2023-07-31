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


route = """
<config>
  <router-static xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ip-static-cfg">
   <default-vrf>
    <address-family>
     <vrfipv4>
      <vrf-unicast>
       <vrf-prefixes>
        <vrf-prefix>
         <prefix>100.100.100.100</prefix>
         <prefix-length>32</prefix-length>
         <vrf-route>
          <vrf-next-hop-table>
           <vrf-next-hop-next-hop-address>
            <next-hop-address>10.71.0.80</next-hop-address>
           </vrf-next-hop-next-hop-address>
          </vrf-next-hop-table>
         </vrf-route>
        </vrf-prefix>
       </vrf-prefixes>
      </vrf-unicast>
     </vrfipv4>
    </address-family>
   </default-vrf>
  </router-static>
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

#Merge
data = m.edit_config(target='candidate', config=route, default_operation="merge")
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
