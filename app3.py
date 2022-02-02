import time
import logging
import logging.handlers
import syslog

from opentelemetry import trace

if __name__ == "__main__":
  # Example 3: Applies a handler to send to syslog; in this case the formatter is used
  #            but seems slightly off (date is cut off) and I don't see any trace correlation 
  tracer = trace.get_tracer(__name__)
  handler = logging.handlers.SysLogHandler(address='/dev/log')
  myLogger = logging.getLogger('MyLogger')
  myLogger.addHandler(handler)
  with tracer.start_as_current_span("Example 3 - one"):
    myLogger.info('Example 3 - one')
    with tracer.start_as_current_span("Example 3 - two"):
      myLogger.info('Example 3 - two')
      with tracer.start_as_current_span("Example 3 - three"):
        myLogger.info('Example 3 - three')

  # Need to ensure all traces are sent
  trace.get_tracer_provider().shutdown()
