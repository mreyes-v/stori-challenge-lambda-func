from decimal import *

from boto3.dynamodb.types import TypeDeserializer

from services.aws import dynamodb

deserializer = TypeDeserializer()


class Transactions:
    def __init__(self):
        self.table = dynamodb.Table('stori-transactions')

    def get_transactions(self, id=None):
        try:
            if id is None:
                response = self.table.scan()
                return response['Items']

            response = self.table.get_item(Key={
                "id": Decimal(id)
            })
            if 'Item' in response:
                return response['Item']
            raise 'Item not found'

        except Exception as e:
            raise e

    def insert_transactions(self, data):
        try:
            if data is None:
                return "No data", 400

            with self.table.batch_writer() as batch:
                for item in data:
                    batch.put_item(
                        Item={
                            'uid': str(item['uid']),
                            'id': item['id'],
                            'date': str(item['date']),
                            'transaction': Decimal(item['transaction']),
                            'type': item['type']
                        }
                    )
            return 'You will receive an email with your summary'

        except Exception as e:
            print(e)
            raise e
