import boto3

client=boto3.client('s3',
      region_name="us-east-1"
                   )
response=client.create_bucket(
  Bucket='ranjan-demo-boto3-12321'
)

print("Bucket created", resonse)


response=client.get_bucket_acl(
  bucket'ranjan-demo-boto3-12321'
)

print(response)

$ python test.py 
Bucket created: {'ResponseMetadata': {'RequestId': '5XK4PXKSDVJ5SK29', 'HostId': 'beDpjANYVhhP1HAa7udrap0dg1+Qnd1c+0jltEWOZdi58+xLDXmQTloGE6HFhcWxzB+4eC9nJw1dcQ/iHhk8AfNwOMp/+EoW', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'beDpjANYVhhP1HAa7udrap0dg1+Qnd1c+0jltEWOZdi58+xLDXmQTloGE6HFhcWxzB+4eC9nJw1dcQ/iHhk8AfNwOMp/+EoW', 'x-amz-request-id': '5XK4PXKSDVJ5SK29', 'date': 'Sun, 12 Oct 2025 11:13:10 GMT', 'location': '/ranjan-demo-boto3-123', 'content-length': '0', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Location': '/ranjan-demo-boto3-123'}
{'ResponseMetadata': {'RequestId': '5XK645YVY0YC65M4', 'HostId': 'ggQvGYoDg+dN/sKxJaT+b0TVuUS0Xh8zc6iHxuFcAAdn6aYeUDhCTmZaG1oLXp558epLM+HS2VCMh0S+E9csRPlnZbkqP3BU', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'ggQvGYoDg+dN/sKxJaT+b0TVuUS0Xh8zc6iHxuFcAAdn6aYeUDhCTmZaG1oLXp558epLM+HS2VCMh0S+E9csRPlnZbkqP3BU', 'x-amz-request-id': '5XK645YVY0YC65M4', 'date': 'Sun, 12 Oct 2025 11:13:10 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Owner': {'DisplayName': 'souravsrivastava027', 'ID': 'c5c831ebae6c7130ae3e13d9f3fb6e33bbcbfa1270911a09b2174c1f2b5bad62'}, 'Grants': [{'Grantee': {'DisplayName': 'souravsrivastava027', 'ID': 'c5c831ebae6c7130ae3e13d9f3fb6e33bbcbfa1270911a09b2174c1f2b5bad62', 'Type': 'CanonicalUser'}, 'Permission': 'FULL_CONTROL'}]}
