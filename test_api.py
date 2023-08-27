import requests
import json

end_url = "https://todo.pixegami.io/"


def create_task(payload):
    return requests.put(end_url + "/create-task", json=payload)


def get_task(task_id):
    return requests.get(end_url + "/get-task/" + task_id)

def update_task(test_id,payload):
    return requests.put(end_url + "/update-task" + "/" + test_id, json=payload)

def payload_info():
    return {"content": "test my content", "user_id": "test_user", "is_done": False}


def test_get():
    response = requests.get(end_url)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["message"] == 'Hello World from Todo API'


def test_create():
    payload = payload_info()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    create_json = create_task_response.json()

    # created task id
    created_task_id = create_json["task"]["task_id"]

    # get the json of the created task id
    get_task_id = get_task(created_task_id)

    assert get_task_id.status_code == 200
    get_json = get_task_id.json()

    assert get_json["content"] == payload["content"]
    assert get_json["user_id"] == payload["user_id"]

def test_update_task():
    # create the data
    payload = payload_info()
    createResponse = create_task(payload)

    assert createResponse.status_code == 200
    createdTaskId = createResponse.json()["task"]["task_id"]

    # # update the data
    new_payload = {"content": "test my content", "user_id": payload["user_id"], "task_id": createdTaskId, "is_done": True}
    Updated_response = update_task(createdTaskId, new_payload)
    # assert Updated_response.status_code == 200
    UpdatedJsonTaskId = Updated_response.json()
    print(UpdatedJsonTaskId)
    # get the data
    # GetResponse = get_task(UpdatedJsonTaskId)
    # print(GetResponse.status_code == 200)