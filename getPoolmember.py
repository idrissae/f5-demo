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
        member_pool={}
        #print (pool.name)
        #( pool_dic[pool.fullPath]["membre_name"], pool_dic[pool.fullPath]["membre_ip"] ) = [ (member.fullPath,  member.address )for member in pool.members_s.get_collection() ] 
        for member in pool.members_s.get_collection():
            member_pool["membre_name"]= member.fullPath
            member_pool["membre_ip"]= member.address
            
        pool_dic[pool.fullPath]= member_pool
        
            


        
       
        #for member in pool.members_s.get_collection():
            
            #print (member.name)

            #m= [member.name for member in pool.members_s.get_collection()]

    print (pool_dic)
    file_name= "output_data/" + bigip_ip +"_pool.json"
    with open (file_name, 'w+') as pool_file:
        json.dump(pool_dic, pool_file, indent=4)
        pool_file.close()



if __name__ == "__main__":
    ## import arguments
    #sys.argv[1]  ## BigIP address
    #sys.argv[2]  ## BIGIP admin
    #sys.argv[3]  ## BigIP admin's password
    # getListPoolMembers(sys.argv[1] ,sys.argv[2] ,sys.argv[3] )
    devices=[        {
            "mgmt_ip": "",
            "user": "admin",
            "password": ""
          }
           
    ]

    for device in devices:
        ## call the getListPool
        getListPoolMembers(device["mgmt_ip"],device["user"] ,device["password"])

    

   
