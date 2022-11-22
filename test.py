import boto3
import json
client = boto3.client('ecs')

#Listing cluster

client = boto3.client("ecs", region_name="ap-northeast-1")

paginator = client.get_paginator('list_clusters')

response_iterator = paginator.paginate(
    PaginationConfig={
        'PageSize':100
})

for each_page in response_iterator:
    for each_arn in each_page['clusterArns']:
        print(each_arn)




#Describe Task Definition

import boto3
import json

client = boto3.client("ecs", region_name="ap-northeast-1")

paginator = client.get_paginator('list_task_definitions')

response_iterator = paginator.paginate(
    PaginationConfig={
        'PageSize':100
    }
)

for each_page in response_iterator:
    for each_task_definition in each_page['taskDefinitionArns']:
        response = client.describe_task_definition(taskDefinition=each_task_definition)
        print(json.dumps(response, indent=4, default=str))



#Printing ec2 cluster running
import boto3
ec2 = boto3.resource('ec2')
instance_iterator = ec2.instances.filter(Filters=[{'Name': 'tag-key', 'Values': ['Name']}])
for instance in instance_iterator:
    for tag in instance.tags:
        if tag['Key'] == 'Name':
            print(instance.id, instance.instance_type, 'Name :', tag['Value'] )


#List Task Definition Families

client = boto3.client("ecs", region_name="ap-northeast-1")

paginator = client.get_paginator('list_task_definition_families')

response_iterator = paginator.paginate(
    PaginationConfig={
        'PageSize':100
    }
)

for each_page in response_iterator:
    print(each_page['families'])


#List Task Definitions
import boto3
import json

client = boto3.client("ecs", region_name="ap-northeast-1")

paginator = client.get_paginator('list_task_definitions')

response_iterator = paginator.paginate(
    PaginationConfig={
        'PageSize':100
    }
)

for each_page in response_iterator:
    for each_task in each_page['taskDefinitionArns']:
        print(each_task)    



#ec2 tages 
def get_tag(tags, key='Name'):
    if not tags: return ''
    for tag in tags:
        if tag['Key'] == key:
            return tag['Value']
    return ''

conn = boto3.resource('ec2')
instances = conn.instances.filter()
for instance in instances:
    instance_name = get_tag(instance.tags)        
    print (instance_name, instance.id, instance.instance_type)


ecs = boto3.client('ecs')
ecs.list_tasks(
    cluster='cluster_name',
    containerInstance='container_instance_arn',
)    
