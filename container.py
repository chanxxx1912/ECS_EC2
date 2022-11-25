#ContainerInstance


import boto3
import json
client = boto3.client("ecs", region_name="ap-northeast-1")

response = client.list_container_instances(
    cluster='first-cluster',
)


for containerInstanceArns in response['containerInstanceArns']:
    for nextToken in containerInstanceArns [45]:
        print(json.dumps(response, indent=4, default=str))

------------------------------------------------------------
Result of the following code:
    
{
    "containerInstanceArns": [
        "arn:aws:ecs:ap-northeast-1:135634294856:container-instance/first-cluster/a69652351d5346f6b0ea85220322b60e"
    ],
    "ResponseMetadata": {
        "RequestId": "433abeb1-a070-4321-8b1f-909902ba1130",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "433abeb1-a070-4321-8b1f-909902ba1130",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "135",
            "date": "Fri, 25 Nov 2022 08:13:49 GMT"
        },
        "RetryAttempts": 0
    }
}    

Concluson : IT prints the container instance details / id 
