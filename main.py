import json
import requests

from rego import ast, walk

company = "wbpro"

user_data = {
	"requests": {
		"request_ip": "127.0.0.1",
		"request_country": "Poland",
		"timestamp_ns": "2121"
	},
	"session": {
		"username": "wb",
		"company": company,
		"teams": ["hr"],
		"roles": ["dev"]
	},
	"features": {
		"1": {"name": "tasks.view.B"}
	}
}

input_dict = {
	"input": user_data
}

policy_per_company = """
package %s

teams = input.session.teams

# Allow HR to view the tasks
taskview = "deny" {
	input.session.username == "w2b"
} else = "allow" {
	teams[_] == "hr3"
} else = "allow" {
	input.features[_].name == "tasks.view.B"
}
""" % company

resp = requests.put(
	"http://localhost:8181/v1/policies/" + company, data=policy_per_company)
resp.raise_for_status()
print(resp.json())

resp = requests.post("http://127.0.0.1:8181/v1/data/" + company,
	json=input_dict)
resp.raise_for_status()

print(resp.json())



