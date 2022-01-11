import boto3


def lambda_handler(event, context):
    # client for dynamoDB
    dynamodb_client = boto3.client('dynamodb')

    # set table
    customer_table = 'customer'

    item = {
        "customer_id": {'S': '1'},
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

    # put item into dynamo
    resp = dynamodb_client.put_item(TableName=customer_table, Item=item)

    '''
    get item from product_table
    '''
    # need to set a key to elete
    key = {
        'customer_id': {'S': '1'}
    }

    response = dynamodb_client.update_item(
        TableName=customer_table,
        Key=key,
        ExpressionAttributeNames={
            '#ia': 'IA'
        },
        UpdateExpression="SET Previsão = :pr, SET Data_retorno = :dr",
        ExpressionAttributeValues={
            ":pr": {
                "S": 'Deu Bom'
            },
            ":dr": {
                "S": "'2018-07-17 22:54:25'"
            }
        }

    )
    return {
        'statusCode': 201,
    }
