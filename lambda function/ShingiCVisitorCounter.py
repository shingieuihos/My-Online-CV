import json
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'ShingiCVisitorCounter'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Handles incoming requests to increment and retrieve the visitor count.
    """
    print(f"Received event: {json.dumps(event)}")
    
    # Set default headers for CORS
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
        'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
    }
    
    # Handle preflight OPTIONS request for CORS
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    try:
        # Get the current count from DynamoDB
        response = table.get_item(Key={'id': 'page_views'})
        item = response.get('Item')
        
        current_count = 0
        if item and 'count' in item:
            current_count = int(item['count'])
            print(f"Current count retrieved: {current_count}")
        else:
            # If the item doesn't exist, create it with initial count 0
            table.put_item(Item={'id': 'page_views', 'count': 0})
            print("Item 'page_views' not found, initialized with count 0.")
            current_count = 0
        
        # Increment the count
        new_count = current_count + 1
        print(f"New count after increment: {new_count}")
        
        # Update the count in DynamoDB
        update_response = table.update_item(
            Key={'id': 'page_views'},
            UpdateExpression='SET #c = :val',
            ExpressionAttributeNames={'#c': 'count'},
            ExpressionAttributeValues={':val': new_count},
            ReturnValues='UPDATED_NEW'
        )
        
        print(f"DynamoDB update response: {json.dumps(update_response, default=str)}")
        
        # Extract the updated count and ensure it's an integer
        updated_count_from_db = update_response['Attributes']['count']
        final_count_to_return = int(updated_count_from_db)
        
        # Return the new count - try both formats
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'count': final_count_to_return,
                'visitor_count': final_count_to_return,  # Alternative key
                'success': True
            })
        }
        
    except ClientError as e:
        print(f"DynamoDB Client Error: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'error': 'Failed to interact with database',
                'details': e.response['Error']['Message'],
                'success': False
            })
        }
    except Exception as e:
        print(f"General Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'error': 'Internal server error',
                'details': str(e),
                'success': False
            })
        }
