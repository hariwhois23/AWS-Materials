import json

def lambda_handler(event, context):
    # TODO implement


    return {
        'statusCode': 200,
        'body': json.dumps('Hello Lambda, From my S3!')
    }
 