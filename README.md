### Make sure you have Python 3 installed and MySQL running

Clone this repository

Navigate to the project's root directory

    $ cd carrental

Create a virtual environment

    $ python3 -m venv myvenv

Activate the virtual environment

    $ source myvenv/bin/activate

Install the project's dependencies

    $ pip3 install -r requirements.txt

In the project's root directory, create a .env file using .env.example as a template and fill in the details

In your MySQL, create a database using the name you entered in the .env file

Go back to the terminal and run the migrations

    $ python3 manage.py migrate

Create a Superuser

    $ python3 manage.py createsuperuser

Run the project

    $ python3 manage.py runserver

Open the project on your browser at http://127.0.0.1:8000