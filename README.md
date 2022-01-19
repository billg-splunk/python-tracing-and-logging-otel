# python-tracing-and-logging-otel

## Setup environment

```
git clone https://github.com/billg-splunk/python-tracing-and-logging-otel.git
cd python-tracing-and-logging-otel
```

## Run (first time)

```
./setup.sh
splunk-py-trace python3 app.py
```

## Run (subsequent times)
```
./activate.sh
splunk-py-trace python3 app.py
```