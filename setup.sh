#!/bin/bash

while getopts t:r: flag
do
    case "${flag}" in
        t) token=${OPTARG};;
        r) realm=${OPTARG};;
    esac
done

# Install OTel Collector
curl -sSL https://dl.signalfx.com/splunk-otel-collector.sh > /tmp/splunk-otel-collector.sh && \
sudo sh /tmp/splunk-otel-collector.sh --realm $realm -- $token --mode agent
# Install pip3
sudo apt install -y python3-pip
# Install Otel Python libraries
pip3 install splunk-opentelemetry[all]
# Bootstrap
splunk-py-trace-bootstrap
