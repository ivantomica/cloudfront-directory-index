# Cloudfront directory index

Simple Lambda@Edge function which provides directory index for the requests sent to S3 origin for example.

By default Cloudfront can specify only the main index file, which is being served when you visit `/` URI. If your URI contains a path it will be sent to S3 like `/about-me/`, and S3 will return the error if that's not an object, but directory.

Default static page option in S3 is able to serve directory index instead (`/about-me/index.html`) in the background.

If the URI already has `/index.html`, it will be stripped and visitor will be redirected to `/about-me/` so we keep the prett-urls.

This lambda currently covers only basic needs I have for my private Hugo based website hosted on S3 + Cloudfront

### Installation

0. create IAM role
   a. attach AWSLambdaBasicExecutionRole policy to it
   b. edit trust relationship, it should look somewhat like:
   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": [
                       "lambda.amazonaws.com",
                       "edgelambda.amazonaws.com"
                   ]
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```
1. package up lambda_handler.py into .zip file
2. create lambda function in us-east-1 region (if you want to use it as Lambda@Edge)
   a. author from scratch
   b. when configuring function, use latest Python runtime
   c. use existing execution role and select previously created IAM role
3. open lambda and Upload from .zip file
4. add trigger
   a. select Cloudfront
   b. click on Deploy to Lambda@Edge
   c. select distribution
   d. cache behaviour: *
   e. cloudfront event: origin request
   f. I acknowledge
   g. Deploy
