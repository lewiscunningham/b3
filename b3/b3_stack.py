"""
  Creates the lambda function and api gateway for the barometer take home
"""
from aws_cdk import (
    Duration,
    aws_lambda as lambda_,
    aws_apigateway as apig,
    Stack,
)
from constructs import Construct
import os.path as path

class B3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # identify the lambda function
        lambdaFn = lambda_.Function(
            self, 'cdk-r4p-lambda',
            runtime=lambda_.Runtime.PYTHON_3_7,
            function_name='cdk-r4p-lambda',
            description='Lambda function deployed using AWS CDK Python',
            code=lambda_.Code.from_asset('./resources'),
            handler='barometer_get.lambda_handler',
        )        

        """Using the AWS CDK, deploy a basic Lambda REST API using AWS Lambda and 
            AWS API Gateway with the following requirements:
                The API Gateway should have one endpoint (or resource) called /barometer 
                    that has the allowed methods: GET|POST. 
                The endpoint should be able to integrate with and call the Lambda 
                    function you’ll create next.
        """
        restAPI  = apig.RestApi(self, "Api", rest_api_name="barometerAPI") 
        proxyIntegration = apig.LambdaIntegration(lambdaFn);

        # create the endpoint name
        resource = restAPI.root.add_resource('barometer');
        resource.add_method("POST", proxyIntegration)
        resource.add_method("GET", proxyIntegration)
