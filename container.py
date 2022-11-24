import boto3


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
        print(response)

----------------------------------------------------------------------------------------------------------------------------------------------------
Result when u run the following script:
{'taskDefinition': {'taskDefinitionArn': 'arn:aws:ecs:ap-northeast-1:135634294856:task-


definition/ngnix:1', 'containerDefinitions': [{'name': 'c2', 'image': 'nginx:latest', 

'cpu': 0, 'portMappings': [], 'essential': True, 'entryPoint': [], 'command': [], 

'environment': [], 'mountPoints': [], 'volumesFrom': [], 'logConfiguration': 

{'logDriver': 'awslogs', 'options': {'awslogs-group': '/ecs/ngnix', 'awslogs-region': 

'ap-northeast-1', 'awslogs-stream-prefix': 'ecs'}}}], 'family': 'ngnix', 'revision': 1, 

'volumes': [], 'status': 'ACTIVE', 'requiresAttributes': [{'name': 

'com.amazonaws.ecs.capability.logging-driver.awslogs'}, {'name': 


'com.amazonaws.ecs.capability.docker-remote-api.1.19'}], 'placementConstraints': [], 

'compatibilities': ['EXTERNAL', 'EC2'], 'requiresCompatibilities': ['EC2'], 'cpu': 

'1024', 'memory': '512', 'registeredAt': datetime.datetime(2022, 11, 22, 17, 36, 24, 

401000, tzinfo=tzlocal()), 'registeredBy': 'arn:aws:iam::135634294856:root'}, 'tags': [], 'ResponseMetadata': {'RequestId': '3b756b5f-a949-409b-80f0-1a7a90b85748', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '3b756b5f-a949-409b-80f0-1a7a90b85748', 'content-type': 'application/x-amz-json-1.1', 'content-length': '864', 'date': 'Thu, 24 Nov 2022 10:29:31 GMT'}, 'RetryAttempts': 0}}

