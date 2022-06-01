# Photo Gallery App

## Description
A django photo gallery app that gives photographers a portfolio to showcase their images to potential clients.
## Visit site
[www.galla-app.com](https://galla-app.herokuapp.com/)

### Author
Mungai Mbugua

## Technologies used
- MDBootstrap
- FancyBox
- Typed.js
- Select2
- AOS
- Django
- Jquery

## User Stories
As a user of the application I should be able to:

   - View different photos that interest me.
   - Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
   - Search for different categories of photos. (ie. Travel, Food)
   - Copy a link to the photo to share with my friends.
   - View photos based on the location they were taken.


## Setup Instructions
- `git init` and run `git remote add origin `https://github.com/munga114/gallery`
-  From the project directory run `conda create --prefix=./env` or `python -m venv virtual`
- Run `source activate ./env` for conda or `source virtual/bin/activate`
- run`touch .env` in the root project directory and add the following to your file
```
SECRET_KEY=''
DEBUG=True
DB_NAME='<your database_name>'
DB_USER='<your database username>'
DB_PASSWORD='<your database password>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```
- Run `pip install -r requirements.txt`
- Run `python manage.py migrate`
- Run `python manage.py createsuperuser` and follow the steps provided
- Your app your be able to start by running `python manage.py runserver`

## Author's Info
[mungai-mbugua twitter](https://mobile.twitter.com/mungaimbugua4)