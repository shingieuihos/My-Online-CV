# My-Online-CV
This repository contains the code and configuration for my online Curriculum Vitae, hosted on AWS as a static website with a visitor counter.
Project Components
Frontend:

index.html: The main HTML file for the CV content.

style.css: CSS for styling the CV.

script.js: JavaScript for the visitor counter, interacting with the backend API.

Backend (AWS Serverless):

lambda/visitor_counter_function.py: Python code for the AWS Lambda function that handles visitor count updates in DynamoDB.

AWS Infrastructure:

Amazon S3: Hosts the static website files.

Amazon CloudFront: Provides HTTPS and content delivery.

Amazon Route 53: Manages custom domain DNS.

Amazon API Gateway: Exposes the Lambda function as a REST API.

Amazon DynamoDB: Stores the visitor count.

Documentation:

s3 bucket/S3-CloudFront-Route53-Setup.md: Instructions for setting up the static website hosting.

lambda function/API-Gateway-Lambda-DynamoDB-Setup.md: Instructions for setting up the visitor counter backend.

Repository Structure
my-online-cv/
├── README.md
    S3 StaticWebCV/
      └── index.html
├── lambda function/
      └── ShingiCVisitorCounter.py
      └── API-Gateway-Lambda-DynamoDB-Setup.md
└── s3 bucket/
      └── API-Gateway-Lambda-DynamoDB-Setup.md

Setup Instructions
To get this CV online and the visitor counter functioning, you will need to follow the AWS setup instructions provided in the aws-setup/ directory.

Clone this repository:

git clone https://github.com/your-username/my-online-cv.git
cd my-online-cv

Set up AWS Static Website Hosting: Follow the instructions in s3 bucket/S3-CloudFront-Route53-Setup.md to deploy your index.html, style.css, and script.js files to S3, configure CloudFront for HTTPS, and set up your custom domain with Route 53.

Set up AWS Visitor Counter Backend: Follow the instructions in lambda function/API-Gateway-Lambda-DynamoDB-Setup.md to create your DynamoDB table, deploy the lambda/"visitor_counter_function.py" to Lambda, and set up API Gateway to expose it.

Update Frontend API Endpoint: Once your API Gateway is deployed, you will get an "Invoke URL". Update the API_ENDPOINT variable in script.js with this URL.

Upload Updated script.js: Upload the modified script.js to your S3 bucket, overwriting the old one.

Test: Open your custom domain in a web browser and verify that the visitor counter appears and increments.
