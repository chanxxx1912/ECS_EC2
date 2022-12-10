
import boto3
import json
import sys
session = boto3.Session(profile_name='default')
client = session.client('ecs')

paginator = client.get_paginator('list_clusters')

response_iterator = paginator.paginate()
    
#sys.stdout = open("test.txt", "w")
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
                #Converting into dict
                
                
                
                
                str = (f"ClusterName = {each_cluster_arn}")
                dictionary = dict(subString.split("=") for subString in str.split(";"))
                print(dictionary)
                
                

                #Task id or Name
              
                str1 = (f"TaskId/Name = {task_name}")
                dictionary = dict(subString.split("=") for subString in str1.split(";"))
                print( dictionary)

               

                #Task Def id or name
                str2 = (f"TaskDefId/Name = {task_definition_name.split('/')[1]}")   
                dictionary = dict(subString.split("=") for subString in str2.split(";"))
                print(dictionary) 

                #Image name
                image = (container['name'])
                str3 = (f"ImageName = {image}")
                dictionary = dict(subString.split("=") for subString in str3.split(";"))
                print(dictionary)
                              


                #Image tag
                image_tag = (container['image'])
                str4 = (f"ImageTag = {image_tag}")
                dictionary = dict(subString.split("=") for subString in str4.split(";"))
                print(dictionary)

                #Tag of channel
                str5 = (f"ValueOfClusterTag_Channel = {result_of_the_tag.get('value')}")
                dictionary = dict(subString.split("=") for subString in str5.split(";"))
                print(dictionary)


-------------------------------------------------------------------------------
Output:
  {'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/env'}
{'TaskId/Name ': ' env'}
{'TaskDefId/Name ': ' envtask1:1'}     
{'ImageName ': ' redis1'}
{'ImageTag ': ' redis:7.0.5'}
{'ValueOfClusterTag_Channel ': ' voot'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/env'}
{'TaskId/Name ': ' env'}
{'TaskDefId/Name ': ' envtask2:4'}
{'ImageName ': ' redis2'}
{'ImageTag ': ' redis:7.0.5-bullseye'}
{'ValueOfClusterTag_Channel ': ' voot'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/env'}
{'TaskId/Name ': ' env'}
{'TaskDefId/Name ': ' envtask3:1'}
{'ImageName ': ' deployment'}
{'ImageTag ': ' nginx:1.23.2'}
{'ValueOfClusterTag_Channel ': ' voot'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/env'}
{'TaskId/Name ': ' env'}
{'TaskDefId/Name ': ' envtask3:1'}
{'ImageName ': ' nginx'}
{'ImageTag ': ' nginx:1.23'}
{'ValueOfClusterTag_Channel ': ' voot'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/prod'}
{'TaskId/Name ': ' prod'}
{'TaskDefId/Name ': ' prodtask2:2'}
{'ImageName ': ' testing'}
{'ImageTag ': ' nginx:1.22-alpine'}
{'ValueOfClusterTag_Channel ': ' prime'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/prod'}
{'TaskId/Name ': ' prod'}
{'TaskDefId/Name ': ' prodtask1:2'}
{'ImageName ': ' production'}
{'ImageTag ': ' nginx:latest'}
{'ValueOfClusterTag_Channel ': ' prime'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/prod'}
{'TaskId/Name ': ' prod'}
{'TaskDefId/Name ': ' prodtask3:1'}
{'ImageName ': ' c2'}
{'ImageTag ': ' nginx:1.22.1-alpine-perl'}
{'ValueOfClusterTag_Channel ': ' prime'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/prod'}
{'TaskId/Name ': ' prod'}
{'TaskDefId/Name ': ' prodtask3:1'}
{'ImageName ': ' c1'}
{'ImageTag ': ' redis:6-bullseye'}
{'ValueOfClusterTag_Channel ': ' prime'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/dev'}
{'TaskId/Name ': ' dev'}
{'TaskDefId/Name ': ' devtask3:1'}
{'ImageName ': ' image2'}
{'ImageTag ': ' nginx:stable'}
{'ValueOfClusterTag_Channel ': ' netflix'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/dev'}
{'TaskId/Name ': ' dev'}
{'TaskDefId/Name ': ' devtask3:1'}
{'ImageName ': ' image1'}
{'ImageTag ': ' redis:7-alpine'}
{'ValueOfClusterTag_Channel ': ' netflix'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/dev'}
{'TaskId/Name ': ' dev'}
{'TaskDefId/Name ': ' devtask1:1'}
{'ImageName ': ' devcontainer'}   
{'ImageTag ': ' redis:latest'}    
{'ValueOfClusterTag_Channel ': ' netflix'}
{'ClusterName ': ' arn:aws:ecs:ap-northeast-1:135634294856:cluster/dev'}
{'TaskId/Name ': ' dev'}
{'TaskDefId/Name ': ' devtask2:1'}
{'ImageName ': ' containerc1'}
{'ImageTag ': ' nginx:perl'}
{'ValueOfClusterTag_Channel ': ' netflix'}

                
               



                
                
                                





                    
