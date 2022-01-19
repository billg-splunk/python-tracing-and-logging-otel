#!/bin/bash

# Assumes run_first_time.sh was run once

# Bootstrap
splunk-py-trace-bootstrap
export OTEL_SERVICE_NAME=myPythonService
# Run the app
splunk-py-trace python3 app.py