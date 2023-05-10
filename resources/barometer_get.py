"""
The Lambda function that will be integrated with your API endpoint should return Getting… 
when the HTTP method is a GET request, and Posting… when the HTTP method is a POST request. 
You can decide the structure of the response payload so long as Getting... or Posting... 
is in the body of the payload.
"""
import json

def lambda_handler(event, context):

    # API gateway proxy sends in the httpMethod
    method = event['httpMethod']
    if method == "GET":
        return {
            'statusCode': 200,
            'body': 'Getting'
    }
    if method == "POST":
        return {
            'statusCode': 200,
            'body': 'Posting'
    }
    
   