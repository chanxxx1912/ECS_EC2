import boto3
import json
session = boto3.Session(profile_name='default')
client = session.client('ecs')


cluster_list = client.list_clusters()
cluster_name = cluster_list["clusterArns"]
for i in cluster_name:
   cluster_name=(i.split('/')[1])

   task_list = client.list_tasks(
     cluster=(cluster_name)
   )
   task = task_list
   if task == task_list:
    task =  (task_list['taskArns'])
    for i in task:
        task= (i.split('/')[2])
        #print(task)
       
        describe_task = client.describe_tasks(
          cluster = (cluster_name),
          tasks =[
            task
          ]
        ) 
        #print(describe_task)
               
        
        output = (json.dumps(describe_task,indent=4,default=str)) 
        report = open('file.json', 'w')
        report.write((json.dumps(describe_task,indent=4,default=str)))
        report.close()
        with open ('file.json') as f:
          data_file = json.load(f)
        containers = []  
        tasks = data_file['tasks']
        for task in tasks:
          containers = task['containers']
          lastStatus = containers
          RUNNING = lastStatus

          for container in containers:
            if lastStatus == RUNNING :
              print(container['name'])
              print(container['image'])
              print(container['lastStatus'])


----------------------------------------------------------------------------------------------------------------------------------
Output:
  PS E:\5-12> python git.py
redis1
redis:7.0.5
RUNNING    
redis2
redis:7.0.5-bullseye
RUNNING
deployment
nginx:1.23.2
RUNNING     
nginx       
nginx:1.23  
RUNNING     
testing
nginx:1.22-alpine
RUNNING
production
nginx:latest
RUNNING     
c2
nginx:1.22.1-alpine-perl
RUNNING
c1
redis:6-bullseye
RUNNING
image2
nginx:stable
RUNNING
image1
redis:7-alpine
RUNNING
devcontainer
redis:latest
RUNNING
containerc1
nginx:perl
RUNNING
PS E:\5-12> python test.py
redis1
redis:7.0.5
RUNNING    
redis2
redis:7.0.5-bullseye
RUNNING
deployment
nginx:1.23.2
RUNNING     
nginx       
nginx:1.23  
RUNNING     
testing
nginx:1.22-alpine
RUNNING
production
nginx:latest
RUNNING     
c2
nginx:1.22.1-alpine-perl
RUNNING
c1
redis:6-bullseye        
RUNNING
image2
nginx:stable  
RUNNING       
image1        
redis:7-alpine
RUNNING       
devcontainer
redis:latest
RUNNING
containerc1
nginx:perl
RUNNING
   

       
 

   
