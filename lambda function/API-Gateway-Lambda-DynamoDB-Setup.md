# AWS API Gateway, Lambda, DynamoDB Setup Instructions

# Key Steps:

## Create DynamoDB Table:

Create a new table (e.g., visitor-count).

Define a primary key (e.g., id as a String).

Choose on-demand capacity mode.

## Create Lambda Function:

Create a new Lambda function (e.g., visitorCounterFunction).

Choose Python 3.x runtime.

Create a new IAM role with basic Lambda permissions and add DynamoDB:GetItem, DynamoDB:UpdateItem, DynamoDB:PutItem permissions for your visitor-count table.

Copy the content of lambda/visitor_counter_function.py into your Lambda function code.

Add an environment variable TABLE_NAME with the value visitor-count (or your table's name).

## Create API Gateway:

Create a new REST API.

Create a new resource (e.g., /visitor-counter).

Create a POST (or GET) method for this resource.

Set the integration type to "Lambda Function" and select your visitorCounterFunction.

Enable CORS for your resource, ensuring your website's domain is allowed for Access-Control-Allow-Origin.

Deploy the API to a stage (e.g., prod). Note down the "Invoke URL".
