import time
import logging
import logging.handlers
import syslog

from opentelemetry import trace

if __name__ == "__main__":
  # Example 2: Logs to syslog, which is automatically ingested into Log Observer
  #            (syslog natively supported). These show up in log observer witout
  #            the pattern applied and don't do trace correlation.
  tracer = trace.get_tracer(__name__)
  with tracer.start_as_current_span("Example 2 - fi"):
    syslog.syslog('Example 2 - fi')
    with tracer.start_as_current_span("Example 2 - fie"):
      syslog.syslog('Example 2 - fie')
      with tracer.start_as_current_span("Example 2 - fofum"):
        syslog.syslog('Example 2 - fofum')

  # Need to ensure all traces are sent
  trace.get_tracer_provider().shutdown()
