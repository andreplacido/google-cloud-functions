# Google Cloud Functions Samples
Some samples for better understanding about google cloud functios

## Before Start
Create a Google cloud Project.
To start a new project in Google Cloud, we can go to the [Firebase Console](https://console.firebase.google.com) or 
creat it from [Google Cloud Platform Console](https://console.cloud.google.com)

## Creating a virtual environment
First we have to install ' python3-env' with the following coomand:
````
sudo apt install python3-venv
````
Create virtual environment
````
python3 -m venv venv
````
 Remember to add venv/ folder at .gitignore list
 
To activate the virtual environment:
```
source venv/bin/activate
```

In order to add new packages o our new virtual environment (venv) we create a file called 'requirements.txt' and execute the following command:
````
pip install -r requirements.txt
````
To check the packages installed (pycharm)
 menu: File >> settings >> Project >> Project Interpreter
 Select the (*) Engine symbol >> Add >> Existing environment


Log error
- Failed building wheel for pathtools. => pip install wheel

## Deploying our functions
First, we have to set our project ID with the following command:
````
gcloud config set project [YOUR_PROJECT_ID]
````
then we deploy our function with this command:
````
 gcloud functions deploy [FUNCTION_NAME] --runtime python37 --trigger-http
````
## Send email
This code use [sendgrid API](https://sendgrid.com/) - folder emails <br/>
Required : sendgrid package
````
pip install -r requirements.txt 
````

## Cors
After works to solve CORS in the code (helloworl/main.py) to test you canuse the console from your browser and use Javascript to call as the example bellow:<br/>
````
fetch('https://[project-URL].cloudfunctions.net/hello_world',{method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({'name':'Jane','lastname':'Due'})}).then(response => response.text()).then(result => console.log(result))
````

## Schedule Cloud Functions
We execute the following commands:

```
gcloud components install beta
gcloud components update
gcloud pubsub topics create [TOPIC NAME]
gcloud pubsub subscriptions create cron-sub --topic [TOPIC NAME]
```

## Delete cloud Functions
to delete a Cloud Function execute the following command:
```
gcloud functions delete [FUNCTION NAME]
```