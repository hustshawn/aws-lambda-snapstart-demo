import json

from snapshot_restore_py import register_before_snapshot, register_after_restore


@register_before_snapshot
def before_snapshot_function():
    print("Before snapshot...")


@register_after_restore
def after_restore_function():
    print("After restore...")


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    print("Hello from lambda function handler...")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "hello world"}),
    }
