# TITLE
## WAMBUI'S GALLERY
# Description
This is an amazing application to showcase beautiful pictures. Users can view photos uploaded by admin,see photos based on the location , by clicking on the listed locations in the menu and of different categories. They can also copy the link to a photo to paste at their discretion. They can also search for photos based on the categories.

# Screenshot

# Features
* The home page allows users to see various images
* User can see all images per location they were taken
* Users can also search for images based categories
* Admin can upload images from a django dashboard


# View Live Site here
*https://wambuiphoto.herokuapp.com/

# Technologies Used
- Python 3.6
- Django MVC framework
- HTML, CSS and Bootstrap
- JavaScript
- Postgressql
- Heroku

# Setup and installation

Clone the repo on https://github.com/pwambui2020/djangogallery.git

Figma design https://www.figma.com/file/pi3RM3x2PrXbj37IueQPfr/Untitled?node-id=0%3A1

Activate the virtual environment:python3.6 -m venv virtual 
                                then source virtual/bin/activate

# Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

# Create the Database
- psql
- CREATE DATABASE gallery;


# .env file
Create .env file and paste paste the following filling where appropriate:

* SECRET_KEY = '<Secret_key>'
* DBNAME = 'gallery'
* USER = '<Username>'
* PASSWORD = '<password>'
* DEBUG = True

# Run initial Migration
* python3.6 manage.py makemigrations gallery
* python3.6 manage.py migrate

# Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000

# Known bugs
No bugs known 

# Contact Information
paulynewambui2020@gmail.com
