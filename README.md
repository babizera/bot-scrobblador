# LastFM Bot Scroblador

Bot-Scrobblador is an automatic scrobbler that lets you log (“scrobble”) your favorite songs easily and as many times as you want. Perfect for boosting your stats, reliving beloved tracks, or simply showing the world what’s playing on your profile.

<img align="center"  src="https://babibreaths.nekoweb.org/img/prin1.PNG">

## Attention

Remember: Last.fm has a daily limit of 2,800 scrobbles. Exceeding this will trigger a “Rate Limit” error, blocking your access to the scrobble API for 24 hours

## Requirements :

	•	Python
	•	A Last.fm API account
    •	Rich (For the effects console output)
	•	dotenv (for environment variable management)
	•	pylast (Last.fm API wrapper)

## How To Use :

	1.	Clone this repository.
	2.	Install all required dependencies by running:
pip install -r requirements.txt

    3.	Create a Last.fm API account at:
https://www.last.fm/api/account/create

	4.	Rename the file .env.example to .env and add your Last.fm API credentials:
API_KEY=your_api_key
API_SECRET=your_api_secret
LASTFM_USERNAME=your_lastfm_username
LASTFM_PASSWORD=your_lastfm_password
