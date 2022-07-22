from flask import render_template, request, redirect
from app import app
from models.todo_list import tasks, add_task
from models.task import Task

@app.route('/tasks')
def index():
    return render_template('tasks/index.html', title='Home', tasks=tasks)

@app.route('/tasks/new')
def new():
    return render_template('tasks/new.html', title='New Task')

@app.route('/tasks', methods=['POST'])
def create():
    title = request.form['title']
    description = request.form['description']
    new_task = Task(title, description, False)
    add_task(new_task)
    return redirect('/tasks')

