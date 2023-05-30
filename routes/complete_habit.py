from flask import Blueprint, current_app, request, redirect, url_for
from routes.routes import get_habit, get_completed_habit

complete_page = Blueprint("habits_complete", 
                __name__, 
                template_folder="template", 
                static_folder="static")


@complete_page.route("/complete", methods=["POST"])
def habit_complete():
    date_string = request.form.get("selectedDate")
    index = int(request.form.get("habit_index"))
    habit_obj = get_habit(index)

    habit_obj.complete_update_db(current_app)
    # append_complete_list(habit_obj)
    # remove_habit_list(habit_obj)
    
    return redirect(url_for("habits.view_page", date=date_string))

@complete_page.route("/incomplete", methods=["POST"])
def habit_incomplete():
    date_string = request.form.get("selectedDate")
    index = int(request.form.get("habit_index"))
    habit_obj = get_completed_habit(index)

    habit_obj.incomplete_update_db(current_app)
    
    return redirect(url_for("habits.view_page", date=date_string))
