#!/bin/bash

# Assumes run_first_time.sh was run once
source venv/bin/activate
splunk-py-trace python3 app.py