import boto3
import json
session = boto3.Session(profile_name='default')
client = session.client('ecs')


#Listing the clusters by its names
cluster = client.list_clusters()
cluster_arn_list = cluster["clusterArns"]
#cluster_arn_list = cluster['clusterArns']
for cluster in cluster_arn_list:
   cluster_arn_list = cluster
   
   
   #print(cluster_name)
   #Printing the tag present in cluster
   tags_inside_cluster = client.list_tags_for_resource(
        resourceArn=cluster_arn_list
   )
   #Finding Specific key : value in tags
   tag =  tags_inside_cluster['tags']
   result = next(
    ( (item for item in tag if item['key'] == 'Channel')),
    {}
   )
   print('ValueOfClusterTag_Channel = ', result.get('value'))
 
   
   next_result  = next(
    ( (item for item in tag if item['key'] == 'Env')),
    {}
   )
   print('ValueOfClusterTag_Env = ', next_result.get('value'))
   

   #Listing task ----> 19,20 line is according to doc variable name cant be changed AttributeError:
   task_list = client.list_tasks(
    cluster=(cluster_arn_list)
   )
   task_arn_inside_task_list =(task_list['taskArns'])

   for elements_in_task_list in task_arn_inside_task_list:
    task_arn = (elements_in_task_list)
    #print(task_arn)
    
    task_name = (elements_in_task_list.split('/')[1])
        
    task_id = (elements_in_task_list.split ('/')[2]) 
        
    #tags
    tags_inside_task = client.list_tags_for_resource(
        resourceArn = task_arn
    )
           
    
    #Describe task
    describe_task = client.describe_tasks(
        cluster = (cluster_arn_list),
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
         print(container['name'])  
         print(container['image'])  
         print(cluster_arn_list)
         print(task_name)
         print(task_definition_name.split('/')[1])

      
-----------------------------------------------------------------------------------------------------
Output
ValueOfClusterTag_Channel =  voot
ValueOfClusterTag_Env =  forest
redis1
redis:7.0.5
arn:aws:ecs:ap-northeast-1:135634294856:cluster/env
env
envtask1:1
redis2
redis:7.0.5-bullseye
arn:aws:ecs:ap-northeast-1:135634294856:cluster/env
env
envtask2:4
deployment
nginx:1.23.2
arn:aws:ecs:ap-northeast-1:135634294856:cluster/env
env
envtask3:1
nginx
nginx:1.23
arn:aws:ecs:ap-northeast-1:135634294856:cluster/env
env
envtask3:1
ValueOfClusterTag_Channel =  prime
ValueOfClusterTag_Env =  prodenvironment
testing
nginx:1.22-alpine
arn:aws:ecs:ap-northeast-1:135634294856:cluster/prod
prod
prodtask2:2
production
nginx:latest
arn:aws:ecs:ap-northeast-1:135634294856:cluster/prod
prod
prodtask1:2
c2
nginx:1.22.1-alpine-perl
arn:aws:ecs:ap-northeast-1:135634294856:cluster/prod
prod
prodtask3:1
c1
redis:6-bullseye
arn:aws:ecs:ap-northeast-1:135634294856:cluster/prod
prod
prodtask3:1
ValueOfClusterTag_Channel =  netflix
ValueOfClusterTag_Env =  green
image2
nginx:stable
arn:aws:ecs:ap-northeast-1:135634294856:cluster/dev
dev
devtask3:1
image1
redis:7-alpine
arn:aws:ecs:ap-northeast-1:135634294856:cluster/dev
dev
devtask3:1
devcontainer
redis:latest
arn:aws:ecs:ap-northeast-1:135634294856:cluster/dev
dev
devtask1:1
containerc1
nginx:perl
arn:aws:ecs:ap-northeast-1:135634294856:cluster/dev
dev
devtask2:1


         
     

       
        



   

 
 
    

     
  
  
  

   
  
    
     
     

     
     


    
    
    

 
 
    
    
   


