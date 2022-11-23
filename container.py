import boto3
import json
client = boto3.client('ecs')
#client = session.client('route53domains', region_name='us-east-1')
paginator = client.get_paginator('list_account_settings')

client = boto3.client("ecs", region_name="ap-northeast-1")

paginator = client.get_paginator('list_container_instances')

response_iterator = paginator.paginate(
    
    response = client.list_container_instances(
    cluster='string',
    filter='string',
    nextToken='string',
    maxResults=12,
    status=["ACTIVE","DRAINING","REGISTERING","DEREGISTERING","REGISTRATION_FAILED"]
)
)   
   

for each_page in response_iterator:
    for each_arn in each_page['containerInstanceArns']:
        print("list_container_instances")

# Errors
File "E:\ECS_EC2\demo.py", line 13, in <module>
    response = client.list_container_instances(
  File "C:\Users\Chandana\AppData\Local\Programs\Python\Python310\lib\site-packages\botocore\client.py", line 530, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "C:\Users\Chandana\AppData\Local\Programs\Python\Python310\lib\site-packages\botocore\client.py", line 919, in _make_api_call
    request_dict = self._convert_to_request_dict(
  File "C:\Users\Chandana\AppData\Local\Programs\Python\Python310\lib\site-packages\botocore\client.py", line 990, in _convert_to_request_dict
    request_dict = self._serializer.serialize_to_request(
  File "C:\Users\Chandana\AppData\Local\Programs\Python\Python310\lib\site-packages\botocore\validate.py", line 381, in serialize_to_request
    raise ParamValidationError(report=report.generate_report())
botocore.exceptions.ParamValidationError: Parameter validation failed:
Invalid type for parameter status, value: ['ACTIVE', 'DRAINING', 'REGISTERING', 'DEREGISTERING', 'REGISTRATION_FAILED'], type: <class 'list'>, valid types: <class 'str'>
