from operator import truediv
from application import app, db
from application.models import Todo

@app.route('/add')
def add():
    new_task = Todo(task="Go Shopping")
    db.session.add(new_task)
    db.session.commit()
    return "Added new to do task to the database"

@app.route('/read')
def read():
    all_tasks = Todo.query.all()
    tasks_string = ""
    for thing in all_tasks:
        tasks_string += "<br>"+ thing.task + str(thing.status)
    return tasks_string

@app.route('/update/<task>')
def update(task):
    first_task = Todo.query.first()
    first_task.task = task
    db.session.commit()
    return first_task.task


@app.route('/delete')
def delete():
    first_task = Todo.query.first()
    db.session.delete(first_task)
    db.session.commit()
    return "You have deleted a task on your to do list"


@app.route('/completed')
def completed():
    first_status = Todo.query.first()
    if first_status.status is False:
        first_status.status = True
        db.session.commit()
        return "Your task is now complete"
    else:
        return "Your task is already complete"
    