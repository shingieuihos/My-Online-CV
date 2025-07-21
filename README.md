


# My-Online-CV
This repository contains the code and configuration for my online Curriculum Vitae, hosted on AWS as a static website with a visitor counter.

![AWS Visitor Counter Architecture](https://s3.af-south-1.amazonaws.com/cv.shingimudyirwa.click/My+Online+CV.png)


## Project Components
Frontend:

index.html: The main HTML file for the CV content.

script.js: JavaScript for the visitor counter, interacting with the backend API.

## Backend (AWS Serverless):

lambda/visitor_counter_function.py: Python code for the AWS Lambda function that handles visitor count updates in DynamoDB.

## AWS Infrastructure:

Amazon S3: Hosts the static website files.

Amazon Route 53: Manages custom domain DNS.

Amazon API Gateway: Exposes the Lambda function as a REST API.

Amazon DynamoDB: Stores the visitor count.

## Documentation:

s3 bucket/S3-CloudFront-Route53-Setup.md: Instructions for setting up the static website hosting.

lambda function/API-Gateway-Lambda-DynamoDB-Setup.md: Instructions for setting up the visitor counter backend.

## Repository Structure
my-online-cv/

├── README.md
    S3 StaticWebCV/
      
       └── index.html

├── lambda function/
      
      └── ShingiCVisitorCounter.py
      
      └── API-Gateway-Lambda-DynamoDB-Setup.md

└── s3 bucket/
      
      └── S3-CloudFront-Route53-Setup.md

## Setup Instructions
To get this CV online and the visitor counter functioning, you will need to follow the AWS setup instructions provided in the aws-setup/ directory.

## Clone this repository:

git clone https://github.com/your-username/my-online-cv.git
cd my-online-cv

1. Set up AWS Static Website Hosting: Follow the instructions in s3 bucket/S3-CloudFront-Route53-Setup.md to deploy your index.html file (with style.css, script.js) to S3, and set up your custom domain with Route 53. (I am yet to configure CloudFront for HTTPS)

https://s3.af-south-1.amazonaws.com/cv.shingimudyirwa.click/index.html

2. Set up AWS Visitor Counter Backend: Follow the instructions in lambda function/API-Gateway-Lambda-DynamoDB-Setup.md to create your DynamoDB table, deploy the lambda/"visitor_counter_function.py" to Lambda, and set up API Gateway to expose it.

3. Update Frontend API Endpoint: Once your API Gateway is deployed, you will get an "Invoke URL". Update the API_ENDPOINT variable in script.js with this URL.

4. Upload Updated script.js: Upload the modified script.js to your S3 bucket, overwriting the old one.

Test: Open your custom domain in a web browser and verify that the visitor counter appears and increments.

## Technical Challenges I encountered:
With the Lambda function, and API ENDPOINT and the DynamoDB working perfectly to generate the view count, the front end html which is configured to request the count from ENDPOINT can not seem to make the query to the API ENDPOINT. There might be an error in the code before the fetch call is executed that prevents the request from being initiated.
Prior to this I experienced a CORS related errors with the API ENDPOINT. I resolved it by manually creating the visitor-count - "GET" - Method execution as only the OPTIONS and POST methods were active. This resolved all the errors I was getting, and now everything is functioning perfectly.  

Custom domain with Route 53

http://cv.shingimudyirwa.click
