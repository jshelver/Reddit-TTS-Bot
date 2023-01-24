# Reddit-TTS-Bot
Generates Reddit text-to-speech videos for platforms like Tiktok and Youtube.


## Get Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
* Python 3.7 or higher installed on your system.
* API application on Reddit account.
  * Go to [App Preferences](https://www.reddit.com/prefs/apps)
  * Click "**_create another app_**" at the bottom of the page
  * Fill out the required details and make sure to select **script**
  * Finish by clicking "**_create app_**"

## Setup the project
This section will go through the installion steps and setting up config files.

### Install the requirements
You will need to install [moviepy](https://zulko.github.io/moviepy/index.html), [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/), and [PRAW](https://praw.readthedocs.io/en/stable/index.html) by running the following commands.
```
pip install moviepy
pip install pyttsx3
pip install praw
```
### Create and edit config files
This project uses a `.env` file to store sensitive data. Simply create a `.env` file in the project directory and put the following code block inside of it.
```
CLIENT_ID=example_id
CLIENT_SECRET=example_secret
```
  * Replace "example_id" with the id located under **_personal use script_** in your Reddit API application. 
  * Replace "example_secret" with the id located next to **_secret_** in the same application.
#### _Where to find your client id and secret_
 ![example](https://user-images.githubusercontent.com/97709845/214391291-1fb9dd30-bf5e-44d0-a4f4-d69d064a693a.png)

