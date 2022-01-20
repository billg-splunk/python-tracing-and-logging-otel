#!/bin/bash

# Assumes run_first_time.sh was run once

export OTEL_SERVICE_NAME=myPythonService
export OTEL_PYTHON_LOG_FORMAT='%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s resource.service.name=%(otelServiceName)s] - %(message)s'
export OTEL_PYTHON_LOG_LEVEL=info
# Run the app
splunk-py-trace python3 app.py