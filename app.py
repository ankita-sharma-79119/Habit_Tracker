import os
from pymongo import MongoClient
from routes.routes import pages
from routes.add_habit import add_page
from routes.complete_habit import complete_page
from flask import Flask
import datetime
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.habits_tracker
    app.register_blueprint(pages)
    app.register_blueprint(add_page)
    app.register_blueprint(complete_page)

    @app.context_processor
    def add_calc_date_range():
        def date_range(start: datetime.date):
            dates = [start + datetime.timedelta(days=diff) for diff in range(-3,4)]
            return dates
        return {"date_range" : date_range}
    
    return app
