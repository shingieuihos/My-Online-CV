AWS S3, CloudFront, Route 53 Setup Instructions

Key Steps:

Create an S3 Bucket:

Name your bucket the same as your domain (e.g., my-resume-website.com).

Enable "Static website hosting" in the bucket properties.

Set index.html as the index document.

Upload index.html, (style.css, and script.js) to this bucket.

Configure bucket policy to allow public read access.

Set up CloudFront Distribution:

Create a new CloudFront distribution.

Select your S3 bucket as the origin.

Choose "Redirect HTTP to HTTPS".

Request or select an SSL certificate from AWS Certificate Manager (ACM) for your custom domain.

Add your custom domain name (e.g., my-resume-website.com) as an Alternate Domain Name (CNAME).

Configure Route 53:

Register your custom domain if you haven't already.

Create a Hosted Zone for your domain in Route 53.

Create an A record (Alias) pointing to your CloudFront distribution.
