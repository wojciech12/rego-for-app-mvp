from famous import app
from flask import request as frequest
from datetime import datetime
import requests
from flask import abort
import json


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
        "request_ip": frequest.remote_addr,
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

    r = evaluate_access(company, user_data)
    if "taskview" not in r or r["taskview"] != "allow":
        abort(401)
    return "you can see me!"


def evaluate_access(company, opa_data):
    input_dict = {"input": opa_data}
    print(json.dumps(input_dict, indent=4))
    resp = requests.post("http://127.0.0.1:8181/v1/data/" + company, json=input_dict)
    resp.raise_for_status()
    return resp.json()


@app.route("/admin")
def admin_panel():
    company = frequest.args.get("company")

    policy_per_company = (
        """
package %s

teams = input.session.teams

# Allow HR to view the tasks
taskview = "allow" {
  input.session.username == "natalia"
} else = "allow" {
  teams[_] == "hr3"
} else = "allow" {
  input.features[_].name == "tasks.view.B"
}"""
        % company
    )
    return submit_rule(company, policy_per_company)


def submit_rule(company, policy_per_company):
    print(policy_per_company)
    resp = requests.put(
        "http://localhost:8181/v1/policies/" + company, data=policy_per_company
    )
    resp.raise_for_status()
    return resp.json()
