import boto3
from datetime import datetime


def lambda_handler(event, context):
    sess = boto3.Session(region_name='us-east-2')
    db = sess.client('dynamodb')

    table = 'id_root'

    item = {
        "id": {
            "S": event['id_root']
        },
        "Data": {
            "S": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        "IA": {
            "M": {
                "Previsão": {
                    "S": "'correto'"
                },
                "Data_retorno": {
                    "S": "'2018-07-17 22:54:25'"
                }
            }
        }
    }
    db.put_item(
        TableName=table,
        Item=item
    )
    return {
        'statusCode': 201,
    }
