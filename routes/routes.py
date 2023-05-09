import datetime
import os
from flask import Blueprint, current_app, render_template, request, redirect, url_for
from model.habit import habit
from collections import defaultdict

habit_list = list()
completion_list = list()

pages = Blueprint("habits", 
                __name__, 
                template_folder="template", 
                static_folder="static")

linkedin = os.getenv("LINKEDIN_URI")
github = os.getenv("GITHUB_URI")
medium = os.getenv("MEDIUM_URI")

@pages.route("/view", methods=["GET", "POST"])
def view_page():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()

    get_habit_list_db(selected_date)

    return render_template(
        "view_habit.html", 
        habits=habit_list, 
        title="Habit Tracker",
        completions = completion_list,
        selected_date=selected_date,
        linkedin=linkedin,
        github=github,
        medium=medium)

@pages.route("/", methods=["GET", "POST"])
def home_page():
    return render_template(
        "homepage.html",  
        title="Habit Tracker",
        linkedin=linkedin,
        github=github,
        medium=medium)

@pages.route("/about", methods=["GET", "POST"])
def about_page():
    return render_template(
        "about.html",  
        title="Habit Tracker",
        linkedin=linkedin,
        github=github,
        medium=medium)

def get_habit_list_db(selected_date: datetime.date):
    cur = current_app.db.habits.find({"createdAt" : selected_date.strftime("%Y-%m-%d")})
    habit_list.clear()
    completion_list.clear()

    for val in cur:
        is_completed = val.get("is_completed")
        if is_completed:
            completion_list.append(habit.create_ui_format(val.get("name"),
                                val.get("createdAt"),
                                is_completed,
                                val.get("_id")))
        else:
            habit_list.append(habit.create_ui_format(val.get("name"),
                                val.get("createdAt"),
                                is_completed,
                                val.get("_id")))

def get_habit(index):
    return habit_list[index]

