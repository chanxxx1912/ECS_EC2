import boto3
import json
session = boto3.Session(profile_name='default')
client = session.client('ecs')


#Listing the clusters by its names
cluster_list = client.list_clusters()
cluster_name = cluster_list["clusterArns"]
for i in cluster_name:
   cluster_name=i
   #print(cluster_name)
   #Printing the tag present in cluster
   response = client.list_tags_for_resource(
        resourceArn=cluster_name
   )
   print(response['tags'])

   #Listing the task inside the cluster 
   task_list = client.list_tasks(
     cluster=(cluster_name)
   )
   task = task_list
   if task == task_list:
    task =  (task_list['taskArns'])
    for i in task:
        tag_in_task = i
        task= (i.split('/')[2])
        #print(task)
        #Printing the tags present in the task 
        response = client.list_tags_for_resource(
            resourceArn = tag_in_task
            
        )
        print(response['tags'])
        describe_task = client.describe_tasks(
          cluster = (cluster_name),
          tasks =[
            task
          ]
        ) 
        #print(describe_task)
               
        
        output = (json.dumps(describe_task,indent=4,default=str)) 
        report = open('test.json', 'w')
        report.write((json.dumps(describe_task,indent=4,default=str)))
        report.close()
        with open ('test.json') as f:
          data_file = json.load(f)
        containers = [] 
       
        tasks = data_file['tasks']
        for task in tasks:
          containers = task['containers']
          lastStatus = containers
          taskDefinitionArn = task
          
          RUNNING = lastStatus

          for container in containers:
            if lastStatus == RUNNING :
              print(container['name'])
              print(container['image'])
              print(container['lastStatus'])
              #print(task['taskDefinitionArn'])
              #printing the tags present in taskdefination
              response = client.list_tags_for_resource(
                resourceArn=(task['taskDefinitionArn'])
              ) 
              print(response['tags']) 
                 
--------------------------------------------------------------------------------------------------------------------------------
Output 
PS E:\7-12> python 8-12.py
[{'key': 'ecs', 'value': 'instance'}, {'key': 'aws', 'value': 'resource'}]
[{'key': 'value', 'value': 'micro'}, {'key': 'aws:ecs:clusterName', 'value': 'env'}]
redis1
redis:7.0.5
RUNNING    
[{'key': 'us-east-1', 'value': 'us-east-2'}, {'key': 'usa', 'value': 'france'}]
[{'key': 'aws:ecs:clusterName', 'value': 'env'}, {'key': 'pod ', 'value': 'cast'}]
redis2
redis:7.0.5-bullseye
RUNNING
[{'key': 'output ', 'value': 'value'}, {'key': 'parameter', 'value': 'json'}]
[{'key': 'environment ', 'value': 'green'}, {'key': 'aws:ecs:clusterName', 'value': 'env'}]
deployment
nginx:1.23.2
RUNNING     
[{'key': 'syntax', 'value': 'hello'}, {'key': 'print', 'value': 'helloworld'}]
nginx     
nginx:1.23
RUNNING   
[{'key': 'syntax', 'value': 'hello'}, {'key': 'print', 'value': 'helloworld'}]
[{'key': 'veg', 'value': 'carrot'}, {'key': 'fruit', 'value': 'apple'}]
[{'key': 'country ', 'value': 'india'}, {'key': 'aws:ecs:clusterName', 'value': 'prod'}]
testing
nginx:1.22-alpine
RUNNING
[{'key': 'jbl', 'value': 'go'}, {'key': 'sound', 'value': 'noise'}]
[{'key': 'skills', 'value': 'art'}, {'key': 'aws:ecs:clusterName', 'value': 'prod'}]
production
nginx:latest
RUNNING     
[{'key': 'name', 'value': 'task'}, {'key': 'image', 'value': 'pic'}]
[{'key': 'morals', 'value': 'value'}, {'key': 'aws:ecs:clusterName', 'value': 'prod'}]
c2
nginx:1.22.1-alpine-perl
RUNNING
[{'key': 'needs', 'value': 'food'}, {'key': 'shelter', 'value': 'building'}]
c1
redis:6-bullseye
RUNNING
[{'key': 'needs', 'value': 'food'}, {'key': 'shelter', 'value': 'building'}]
[{'key': 'region', 'value': 'ap-northeast-1'}, {'key': 'south', 'value': 'ap-southeast-1'}]
[{'key': 'aws:ecs:clusterName', 'value': 'dev'}, {'key': 'aggrement ', 'value': 'bond'}]
image2
nginx:stable
RUNNING
[{'key': 'bond ', 'value': 'hopes'}, {'key': 'family', 'value': 'villan'}]
image1
redis:7-alpine
RUNNING
[{'key': 'bond ', 'value': 'hopes'}, {'key': 'family', 'value': 'villan'}]
[{'key': 'container', 'value': 'image'}, {'key': 'aws:ecs:clusterName', 'value': 'dev'}]
devcontainer
redis:latest
RUNNING
[{'key': 'cluster ', 'value': 'task'}, {'key': 'name ', 'value': 'dev'}]
[{'key': 'aws:ecs:clusterName', 'value': 'dev'}, {'key': 'docker', 'value': 'hub'}]
containerc1
nginx:perl
RUNNING
[{'key': 'city', 'value': 'mumbai'}, {'key': 'capital', 'value': 'delhi'}]
              
              

   


   

       
 

   
