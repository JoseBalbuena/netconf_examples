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

#Print Running Config 
data = m.edit_config(target='running', config=route, default_operation="merge")
data_xml = xmltodict.parse(data.xml)["rpc-reply"]["data"]
data_pretty = json.dumps(data_xml,indent=6)
print(data_pretty)


m.close_session()
