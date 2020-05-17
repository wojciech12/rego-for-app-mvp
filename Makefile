opa:
	docker run -d -p 8181:8181 openpolicyagent/opa \
	    run --server --log-level debug
