
import boto3
session = boto3.Session(profile_name='default')
client = session.client('ecs')

paginator = client.get_paginator('list_clusters')

response_iterator = paginator.paginate()
    

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
     print('ValueOfClusterTag_Channel = ', result_of_the_tag.get('value'))
     
     #Finding value of the tag with the key Env

     result_of_next_tag = next(
        ((item for item in cluster_tag if item ['key']=='Env')),
        {}
     )
     print('ValueOfClusterTag_Env = ', result_of_next_tag.get('value'))
     

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
                print(container['name']) 
                print(container['image'])
                print(each_cluster_arn)
                print(task_name)
                print(task_definition_name.split('/')[1])

                

-------------------------------------------------------------------------------------------------------------------------------
Output:
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
