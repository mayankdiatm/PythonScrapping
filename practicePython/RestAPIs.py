from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
app = Flask(__name__)


tasks = [
    {'id'    : 1,
     'title' : 'Buy groceries',
     'descr' : 'Milk, Cheese, Pizza, Fruit, Tylenol',
     'done'  : False
    },
    {'id'   : 2,
     'title': 'Learn Python',
     'descr': 'find a good Python tutorial web',
     'done' : False
    }
]


@app.route('/todo/api/v1.0/createtasks', methods=['GET','POST'])
#@app.route('/todo/api/v1.0/createtasks', methods=['POST'])
def createtasks():
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': "C++",
        'descr': "begginers code ",
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': tasks}), 201

@app.errorhandler(404)
def not_found(error):
 return make_response(jsonify({'error':'Not found'}), 404)


@app.route('/todo/api/v1.0/tasks/', methods=['GET'])
def get_tasks():
    return jsonify({'task': tasks})



@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task=[task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)