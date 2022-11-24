
#ECS.Client.list_container_instances()

import boto3
client = boto3.client("ecs", region_name="ap-northeast-1")

response = client.list_container_instances(
    cluster='first-cluster',
)

print (response)

for containerInstanceArns in response['containerInstanceArns']:
    for nextToken in containerInstanceArns [45]:
        print(containerInstanceArns)
        
        
        
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Result :
    
{'containerInstanceArns': ['arn:aws:ecs:ap-northeast-1:135634294856:container-instance/first-cluster/a69652351d5346f6b0ea85220322b60e'], 'ResponseMetadata': {'RequestId': 'ace34f2e-86e3-4d15-af25-79e3d97273cf', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'ace34f2e-86e3-4d15-af25-79e3d97273cf', 'content-type': 'application/x-amz-json-1.1', 'content-length': '135', 'date': 'Thu, 24 Nov 2022 08:02:43 GMT'}, 'RetryAttempts': 0}}
arn:aws:ecs:ap-northeast-1:135634294856:container-instance/first-cluster/a69652351d5346f6b0ea85220322b60e    
