
#Details inside the container the name image,tags,cpu

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

        print(json.dumps(response, indent=4, default=str))        
        
        
------------------------------------------------------------------------------------------------------------------------------------RE
Result ;
{
    "taskDefinition": {
        "taskDefinitionArn": "arn:aws:ecs:ap-northeast-1:135634294856:task-definition/ngnix:1",
        "containerDefinitions": [
            {
                "name": "c2",
                "image": "nginx:latest",
                "cpu": 0,
                "portMappings": [],
                "essential": true,
                "entryPoint": [],
                "command": [],
                "environment": [],
                "mountPoints": [],
                "volumesFrom": [],
                "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                        "awslogs-group": "/ecs/ngnix",
                        "awslogs-region": "ap-northeast-1",
                        "awslogs-stream-prefix": "ecs"
                    }
                }
            }
        ],
        "family": "ngnix",
        "revision": 1,
        "volumes": [],
        "status": "ACTIVE",
        "requiresAttributes": [
            {
                "name": "com.amazonaws.ecs.capability.logging-driver.awslogs"
            },
            {
                "name": "com.amazonaws.ecs.capability.docker-remote-api.1.19"
            }
        ],
        "placementConstraints": [],
        "compatibilities": [
            "EXTERNAL",
            "EC2"
        ],
        "requiresCompatibilities": [
            "EC2"
        ],
        "cpu": "1024",
        "memory": "512",
        "registeredAt": "2022-11-22 17:36:24.401000+05:30",
        "registeredBy": "arn:aws:iam::135634294856:root"
    },
    "tags": [],
    "ResponseMetadata": {
        "RequestId": "ae627fd9-93be-4e9c-8d19-118823d2eb21",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "ae627fd9-93be-4e9c-8d19-118823d2eb21",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "864",
            "date": "Fri, 25 Nov 2022 08:29:00 GMT"
        },
        "RetryAttempts": 0
    }
}
Conclusion ; prints the container name, image,family,tages
        
