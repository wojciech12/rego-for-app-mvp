from famous import app
from flask import request as frequest
from datetime import datetime
import requests
from flask import abort


@app.route("/")
def hello():
    # here the authentication
    # whether the token is valid
    # JWT

    # construct the user
    # request data
    username = frequest.args.get("username")

    ts = datetime.timestamp(datetime.now())
    lt = frequest.args.get("local_time")

    request_dsc = {
        "request_ip": request.remote_addr,
        "request_country": "Poland",
        "timestamp_ns": "2121",
        "localtime": lt,
    }

    # retrive about the user
    company = frequest.args.get("company")
    session_dsc = {
        "username": username,
        "company": company,
        "teams": ["hr"],
        "roles": ["dev"],
    }

    # data for the access
    # evaluation
    user_data = {"request": request_dsc, "session": session_dsc}

    print(user_data)

    r = evaluate_access(company, user_data)
    if "taskview" not in r or r["taskview"] != "allow":
        abort(401)
    return "you can see me!"


def evaluate_access(company, opa_data):
    input_dict = {"input": opa_data}

    resp = requests.post("http://127.0.0.1:8181/v1/data/" + company, json=input_dict)
    resp.raise_for_status()
    return resp.json()


@app.route("/admin")
def rules_admin():
    return ", ".join(SUPPORTED)
