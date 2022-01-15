mport boto3
import json

def lambda_handler(event, context):
    client = boto3.client('sqs')
    response = client.send_message(
        QueueUrl= 'https://sqs.us-east-2.amazonaws.com/914043823852/test',
        MessageBody= 'Vamo guerreiro',
        DelaySeconds= 10,
        MessageAttributes= {
            'id': {
                'DataType': 'String',
                'StringValue': event['id']
            },
            'documents': {
                'DataType': 'String',
                'StringValue': json.dumps(event['list'])
             }
             
        }
    )
    return response