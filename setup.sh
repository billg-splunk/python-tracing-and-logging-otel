python3 -m venv ./venv
pip3 install splunk-opentelemetry[all]
splunk-py-trace-bootstrap
export OTEL_SERVICE_NAME=myPythonService
