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
    
    
    describe_task = client.describe_tasks(
      cluster = cluster_name,
      tasks =[
        task
      ]
    )  
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



   

       
 

   
