import boto3
import json
session = boto3.Session(profile_name='default')
client = session.client('ecs')

#Listing the clusters by its names
cluster_list = client.list_clusters()
cluster_name = cluster_list["clusterArns"]
for name in cluster_name:
   cluster_name = name
   cluster_short_name = (name.split('/')[1])
   
   #print(cluster_name)
   #Printing the tag present in cluster
   tags_inside_cluster = client.list_tags_for_resource(
        resourceArn=cluster_name
   )
   print(cluster_short_name , tags_inside_cluster['tags'])

   #Listing task ----> 19,20 line is according to doc variable name cant be changed AttributeError:
   task_list = client.list_tasks(
    cluster=(cluster_name)
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
    print(task_name ,tags_inside_task['tags'])

    #Describe task
    describe_task = client.describe_tasks(
        cluster = (cluster_name),
        tasks =[
            task_id
        ]

    )
    
   
  
    containers = []   
    
    tasks = describe_task['tasks']
    
    for task_details in tasks:
        containers = task_details['containers']
        
        
        for container in containers:
         print(container['name'])  
         print(container['image'])  
         print(container['lastStatus'])
         

         tags_in_task_definition  =  client.list_tags_for_resource(
            resourceArn=(task_details['taskDefinitionArn'])
         )
         print( container['name'],tags_in_task_definition['tags'])
        
---------------------------------------------------------------------------------------------------------------------


Output
PS E:\7-12> python new.py
env [{'key': 'ecs', 'value': 'instance'}, {'key': 'aws', 'value': 'resource'}]
env [{'key': 'value', 'value': 'micro'}, {'key': 'aws:ecs:clusterName', 'value': 'env'}]
redis1
redis:7.0.5
RUNNING    
redis1 [{'key': 'us-east-1', 'value': 'us-east-2'}, {'key': 'usa', 'value': 'france'}]
env [{'key': 'aws:ecs:clusterName', 'value': 'env'}, {'key': 'pod ', 'value': 'cast'}]
redis2
redis:7.0.5-bullseye
RUNNING
redis2 [{'key': 'output ', 'value': 'value'}, {'key': 'parameter', 'value': 'json'}]
env [{'key': 'environment ', 'value': 'green'}, {'key': 'aws:ecs:clusterName', 'value': 'env'}]
deployment
nginx:1.23.2
RUNNING     
deployment [{'key': 'syntax', 'value': 'hello'}, {'key': 'print', 'value': 'helloworld'}]
nginx     
nginx:1.23
RUNNING   
nginx [{'key': 'syntax', 'value': 'hello'}, {'key': 'print', 'value': 'helloworld'}]
prod [{'key': 'veg', 'value': 'carrot'}, {'key': 'fruit', 'value': 'apple'}]
prod [{'key': 'country ', 'value': 'india'}, {'key': 'aws:ecs:clusterName', 'value': 'prod'}]
testing
nginx:1.22-alpine
RUNNING
testing [{'key': 'jbl', 'value': 'go'}, {'key': 'sound', 'value': 'noise'}]
prod [{'key': 'skills', 'value': 'art'}, {'key': 'aws:ecs:clusterName', 'value': 'prod'}]
production
nginx:latest
RUNNING
production [{'key': 'name', 'value': 'task'}, {'key': 'image', 'value': 'pic'}]
prod [{'key': 'morals', 'value': 'value'}, {'key': 'aws:ecs:clusterName', 'value': 'prod'}]
c2
nginx:1.22.1-alpine-perl
RUNNING
c2 [{'key': 'needs', 'value': 'food'}, {'key': 'shelter', 'value': 'building'}]
c1
redis:6-bullseye
RUNNING
c1 [{'key': 'needs', 'value': 'food'}, {'key': 'shelter', 'value': 'building'}]
dev [{'key': 'region', 'value': 'ap-northeast-1'}, {'key': 'south', 'value': 'ap-southeast-1'}]
dev [{'key': 'aws:ecs:clusterName', 'value': 'dev'}, {'key': 'aggrement ', 'value': 'bond'}]
image2
nginx:stable
RUNNING
image2 [{'key': 'bond ', 'value': 'hopes'}, {'key': 'family', 'value': 'villan'}]
image1
redis:7-alpine
RUNNING
image1 [{'key': 'bond ', 'value': 'hopes'}, {'key': 'family', 'value': 'villan'}]
dev [{'key': 'container', 'value': 'image'}, {'key': 'aws:ecs:clusterName', 'value': 'dev'}]
devcontainer
redis:latest
RUNNING
devcontainer [{'key': 'cluster ', 'value': 'task'}, {'key': 'name ', 'value': 'dev'}]
dev [{'key': 'aws:ecs:clusterName', 'value': 'dev'}, {'key': 'docker', 'value': 'hub'}]
containerc1
nginx:perl
RUNNING
containerc1 [{'key': 'city', 'value': 'mumbai'}, {'key': 'capital', 'value': 'delhi'}]
