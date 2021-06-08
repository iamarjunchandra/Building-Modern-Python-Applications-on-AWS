         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!
<br>
<br><br>LAB 1 - Get the front end up, by uploading a simple front-end where a user can search for an item.
<br>LAB 2 - Get the plumbing in place, by creating three placeholder API Mocks. You will have the website hit up 3 distinct API endpoints that just pipe back the same dummy data for reviews and ratings and create report regardless of what product ids your front-end sends.
<br>LAB 3 - Set up the authentication for staff using Cognito user pools. Wire that into the create report API endpoint and have it reject non authorized requests. 
<br>LAB 4 - Replace the mock AWS Lambda Functions with functions that use S3 SelectObject to return real data to the 2 GET endpoints: get_reviews and get_ratings.
<br>Lab 5 - Have the create_report API kick off a step function background process. Have the step function call various Lambda functions that do various things. Such as sentiment analysis on a review.  Look for key phrases to help with tagging in the report, and create the HTML report and pre-sign it. Finally sending that URL to the logged in user's cellphone.
<br>Lab 6 - Add metrics to instrument how it is performing (AWS X-Ray). Find ways to improve one of your Lambda functions with context reuse, and cache the response. 

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!
