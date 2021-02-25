#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import request
import json
from os import path
import time

app = Flask(__name__)

readFile = "db.json"

currentDir = path.dirname(__file__)
resourcePath = path.join(currentDir, readFile)

with open(resourcePath, "r", encoding='utf_8_sig') as readfs:
    tasks = json.loads(readfs.read())
    readfs.close()


# print(tasks)

# Get请求
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # 检查tasks内部的元素，是否有元素的id值和参数相匹配
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    # 有的话，就返回列表形式包裹的这个元素，没有的话就报错404
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


# Post请求
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    # 如果请求里面没有json数据，或者json数据里面name,age的内容为空
    if not request.json or not 'name' in request.json:
        abort(400)  # 返回404错误
    if not request.json or not 'age' in request.json:
        abort(400)  # 返回404错误
    task = {
        'id': tasks[-1]['id'] + 1,  # 取末尾tasks的id号+1
        'name': request.json['name'],  # name必须设置，不能为空。
        'age': request.json['age'],
        'category': ["weisuo", "haose"],
        'createTimeStamp': time.time()
    }
    tasks.append(task)  # 完了之后，添加这个task进tasks列表
    return jsonify({'task': task}), 201  # 并且返回这个添加的task内容和状态码


# PUT请求
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # 检查是否有这个id数据
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    # 如果请求中没有附带json数据，则报错400
    if not request.json:
        abort(400)
    # 如果name对应的值，不是字符串类型，则报错400
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'age' in request.json and type(request.json['age']) is not int:
        abort(400)
    if 'category' in request.json and type(request.json['category']) is not list:
        abort(400)
    # 如果上述条件全部通过的话，更新name的值，同时设置默认值
    task[0]['name'] = request.json.get('name', task[0]['name'])
    task[0]['age'] = request.json.get('age', task[0]['age'])
    task[0]['category'] = request.json.get('category', task[0]['category'])
    # 返回修改后的数据
    return jsonify({'task': task[0]})


# Delete请求
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # 检查是否有这个数据
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    # 从tasks列表中删除这个值
    tasks.remove(task[0])
    # 返回结果状态，自定义的result
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
