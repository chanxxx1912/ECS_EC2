
import boto3
import json
client = boto3.client("ecs", region_name="ap-northeast-1")
paginator = client.get_paginator('list_task_definitions')

response_iterator = paginator.paginate(
    PaginationConfig={
        'PageSize':100
    }
)

for page in response_iterator:
    for container_definitions in page['taskDefinitionArns']:
        response = client.describe_task_definition(taskDefinition=container_definitions )
    report = open('json.file', 'w')
    report.write( (json.dumps(response, indent=4, default=str)) )
    report.close()
   
#Opening the json file and printing the the content for what we are looking for
with open ('file.json') as f:
    data_file = json.load(f)       

containerDefinitions = []   

containers = data_file['taskDefinition']['containerDefinitions']

for container in containers:
    name = container['name']
    print(name)

for container in containers:
    image = container['image']
    print(image)
-----------------------------------------------------------
Console output : 
nginxContainer
nginx:latest
   
    


    





 



