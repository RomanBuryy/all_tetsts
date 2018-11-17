from flask import Flask
from flask import request
import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'denis'}
}


def add_member(name, age, gender):
    response_data = {"jsonrpc": "2.0"}
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    response_data["result"] = f"We add your member {MEMBERS[name]}"
    return json.dumps(response_data)


def response_data(name):
    header = {"jsonrpc": "2.0"}
    header['result'] = MEMBERS[name]
    return json.dumps(header)


def get_member(name):
    return json.dumps(MEMBERS[name])


METHODS = {
    "getMember": get_member,
    "addMember": add_member,
    "response_data": response_data,

}


@app.route('/', methods=['POST'])
def handle():
    data = json.loads(request.data.decode('utf-8'))
    method_view = METHODS.get(data.get('method'))
    if not method_view:
        return json.dumps({"error": {"code": -32601, "message": "Method not found"}})

    result = method_view(**data.get("params"))
    return result


if __name__ == '__main__':
    app.run(port=4000, host="127.0.0.1")
