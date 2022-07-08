#! /usr/bin/env python
import sys
from f5.bigip import ManagementRoot
import sys, json



def getListPoolMembers (bigip_ip,bigip_admin, bigip_password):
    # Connect to the BigIP
    mgmt = ManagementRoot(bigip_ip, bigip_admin, bigip_password)
    # Get a list of all pools on the BigIP and print their names and their
    # members' names
    pools = mgmt.tm.ltm.pools.get_collection()

    pool_dic={}
    for pool in pools:
        #print (pool.name)
        pool_dic[pool.name]= [member.name for member in pool.members_s.get_collection()]
        
        #for member in pool.members_s.get_collection():
            
            #print (member.name)

            #m= [member.name for member in pool.members_s.get_collection()]

    print (pool_dic)
    file_name= bigip_ip +"_pool.json"
    with open (file_name, 'w+') as pool_file:
        json.dump(pool_dic, pool_file)
        pool_file.close()



if __name__ == "__main__":
    ## import arguments
    #sys.argv[1]  ## BigIP address
    #sys.argv[2]  ## BIGIP admin
    #sys.argv[3]  ## BigIP admin's password
    # getListPoolMembers(sys.argv[1] ,sys.argv[2] ,sys.argv[3] )
    devices=[        {
            "mgmt_ip": "172.16.45.20",
            "user": "admin",
            "password": 'Idri$$2020'
          },
           {
            "mgmt_ip": "172.16.45.21",
            "user": "admin",
            "password": 'Idri$$2020'
          }
           
    ]

    for device in devices:
        ## call the getListPool
        getListPoolMembers(device["mgmt_ip"],device["user"] ,device["password"])

    

   