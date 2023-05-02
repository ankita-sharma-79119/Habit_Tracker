import datetime
from flask import Blueprint, current_app, render_template, request
from model.habit import habit

add_page = Blueprint("habits_add", 
                __name__, 
                template_folder="template", 
                static_folder="static")

@add_page.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habit_name = request.form.get("habit")
        habit_obj = habit(habit_name)
        habit_obj.insert_db(current_app)

    return render_template(
        "add_habit.html", 
        title="Add new Habit",
        selected_date = datetime.datetime.today())