# redditCrawlerPRAW
Collecting hot topics data from subreddit "news" using PRAW.

Data collection for an academic project named Fake News Classification on Reddit.

To run the file:

Step1: Obtain clientID and clientSecret from reddit
  refer https://github.com/reddit-archive/reddit/wiki/OAuth2
  
Step2: Add following lines into your ~./bashrc
  ```export clientid="YOURCLIENTID"```
  ```export clientsecret="YOURCLIENTSECRET"```
  
Step3: Change user_agent's value in the code
  ```<ApplicaitonName> by /u/<YourUsername>"```
  
Step4: Install the libraries in requirements.txt
  ```pip install -r requirements.txt```
  
Step5: Run the file
  ```python dataCollection_v1.py```

The data will be stored in data folder with todays date and time as file name.
