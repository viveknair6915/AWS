import json

def lambda_handler(event, context):
    try:
        # Extract numbers from the event object
        number1 = event.get('number1')
        number2 = event.get('number2')
        
        # Validate the input
        if number1 is None or number2 is None:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid input: Both number1 and number2 are required.')
            }
        
        result = number1 + number2
        
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
