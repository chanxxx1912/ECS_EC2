
import boto3
import sys
session = boto3.Session(profile_name='default')
client = session.client('ecs')

paginator = client.get_paginator('list_clusters')

response_iterator = paginator.paginate()
    

#stdoutOrigin=sys.stdout 
#sys.stdout = open("log.txt", "w")
for clusters_arn in response_iterator:
    #Listing clusters arn
    for each_cluster_arn in clusters_arn['clusterArns']:
     tags_inside_cluster = client.list_tags_for_resource(
     resourceArn=each_cluster_arn
     ) 
     
     #Finding value of the tag with the key Channel
     cluster_tag = tags_inside_cluster['tags']
     result_of_the_tag = next(
        ((item for item in cluster_tag if item['key']=='Channel')),
        {}
     )
     #print('ValueOfClusterTag_Channel = ', result_of_the_tag.get('value'))
     
     #Finding value of the tag with the key Env

     result_of_next_tag = next(
        ((item for item in cluster_tag if item ['key']=='Env')),
        {}
     )
     #print('ValueOfClusterTag_Env = ', result_of_next_tag.get('value'))
     

     #Listing tasks of each cluster present 
     task_list = client.list_tasks(
        cluster = (each_cluster_arn)
     )
     task_arn_inside_task_list =(task_list['taskArns'])

     for elements_in_task_list in task_arn_inside_task_list:
        task_arn = (elements_in_task_list)
        task_name = (elements_in_task_list.split('/')[1])
        task_id = (elements_in_task_list.split ('/')[2]) 

        #tags for task if required 

        tags_inside_task = client.list_tags_for_resource(
            resourceArn = task_arn
        )

        #Describe task
        describe_task =  client.describe_tasks(
            cluster = (each_cluster_arn),
            tasks =[
                task_id
            ]
        )
        
        containers = []

        tasks = describe_task['tasks']

        for task_details in tasks:
            containers = task_details['containers']
            task_definition_name  = task_details['taskDefinitionArn']
            

            for container in containers:
                #Cluster Name

                str = (f"ClusterName = {each_cluster_arn}")
                dictionary = dict(subString.split("=") for subString in str.split(";"))
                #print(dictionary)
                
                

                #Task id or Name
              
                str1 = (f"TaskId/Name = {task_name}")
                dictionary1 = dict(subString.split("=") for subString in str1.split(";"))
                #print( dictionary1)

               

                #Task Def id or name
                str2 = (f"TaskDefId/Name = {task_definition_name.split('/')[1]}")   
                dictionary2 = dict(subString.split("=") for subString in str2.split(";"))
                #print(dictionary2) 

                #Image name
                image = (container['name'])
                str3 = (f"ImageName = {image}")
                dictionary3 = dict(subString.split("=") for subString in str3.split(";"))
                #print(dictionary3)
                              
                #Image tag
                image_tag = (container['image'])
                str4 = (f"ImageTag = {image_tag}")
                dictionary4 = dict(subString.split("=") for subString in str4.split(";"))
                #print(dictionary4)

                #Tag of channel
                str5 = (f"ValueOfClusterTag_Channel = {result_of_the_tag.get('value')}")
                dictionary5 = dict(subString.split("=") for subString in str5.split(";"))
               # print(dictionary5)
                
                
               
             
                
                def Merge (dictionary1,dictionary2,dictionary3,dictionary4,dictionary5):
                    res = dictionary1 | dictionary2 | dictionary3 |dictionary4 |dictionary5
                    return res 

                dictionary6= Merge(dictionary1, dictionary2 , dictionary3 ,dictionary4 ,dictionary5)    
                #print(dicto)  
               

                my_list = []
                dict_copy = dictionary6.copy()
                my_list.append(dict_copy)
                #print(my_list)

   
                
                
               

         









#sys.stdout.close()
#sys.stdout=stdoutOrigin
                
               



                
                
                                





                    
