#!/bin/bash

while getopts u:a:f: flag
do
    case "${flag}" in
        t) token=${OPTARG};;
        r) realm=${OPTARG};;
    esac
done

# Install OTel Collector
curl -sSL https://dl.signalfx.com/splunk-otel-collector.sh > /tmp/splunk-otel-collector.sh && \
sudo sh /tmp/splunk-otel-collector.sh --realm $realm -- $token --mode agent
# Setup venv
python3 -m venv ./venv
# Install otel and bootstrap
pip3 install splunk-opentelemetry[all]
splunk-py-trace-bootstrap
export OTEL_SERVICE_NAME=myPythonService
# Run the app
splunk-py-trace python3 app.py