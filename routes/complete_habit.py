import datetime
from flask import Blueprint, current_app, render_template, request, redirect, url_for
from model.habit import habit
from routes.routes import get_habit

complete_page = Blueprint("habits_complete", 
                __name__, 
                template_folder="template", 
                static_folder="static")


@complete_page.route("/complete", methods=["POST"])
def habit_complete():
    date_string = request.form.get("selectedDate")
    index = int(request.form.get("habit_index"))

    habit_obj = get_habit(index)
    date = datetime.date.fromisoformat(date_string)

    habit_obj.update_db(current_app)
    # append_complete_list(habit_obj)
    # remove_habit_list(habit_obj)
    
    return redirect(url_for("habits.home_page", date=date_string))
