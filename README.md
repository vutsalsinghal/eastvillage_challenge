# Tourism in the East Village

## Overview
The app allows people to see cool events happening today in the [East Village](https://www.google.com/maps/place/East+Village,+New+York,+NY/@40.7265994,-73.9909083,15z/data=!3m1!4b1!4m5!3m4!1s0x89c25977e7cc4e45:0x6fa935f3400f68ec!8m2!3d40.7264773!4d-73.9815337), ordered by distance.

## Instructions for running
- Replace 'API_KEY' in `./eastvillage_challenge/mysite/yelp/views/eventDetail.py` & `./eastvillage_challenge/mysite/yelp/views/eventList.py` with your Yelp API keys.
- Install dependancies: `sudo pip install -r requirements.txt` (use of virtualenv is strongly recommended!)
- Run localserver: `python manage.py runserver` and navigate to `localhost:8000`
  - NOTE: All functionalities are not available on locoalserver
- Demo is available at [eastvillage.pythonanywhere.com](https://eastvillage.pythonanywhere.com)
