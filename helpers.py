import os
from amadeus import Client, ResponseError
from dotenv import load_dotenv
from flask import redirect, render_template, request, session

load_dotenv('dotenv.env')

amadeus = Client(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET')
)

def matchAirline(airline_code):
    try:
        airline_name = amadeus.reference_data.airlines.get(airlineCodes=airline_code).data
        return airline_name[0]['commonName']
    except ResponseError:
        return airline_code

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code
    