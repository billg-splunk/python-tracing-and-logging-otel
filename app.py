import time
import logging
import logging.handlers
import syslog

from opentelemetry import trace

if __name__ == "__main__":
  # Example 1: Default logging (which goes to sysout but applies the pattern correctly)
  tracer = trace.get_tracer(__name__)
  with tracer.start_as_current_span("foo"):
    logging.info('Foo')
    with tracer.start_as_current_span("bar"):
      logging.info('bar')
      with tracer.start_as_current_span("baz"):
        logging.error('baz')
        print("Hello world from OpenTelemetry Python!")

  # Example 2: Logs to syslog, which is automatically ingested into Log Observer
  #            (syslog natively supported)
  with tracer.start_as_current_span("fi"):
    syslog.syslog('fi')
    with tracer.start_as_current_span("fie"):
      syslog.syslog('fie')
      with tracer.start_as_current_span("fofum"):
        syslog.syslog('fofum')

  # Example 3: Applies a handler to send to syslog; in this case the formatter from 
  #            the environment variable isn't used and this needs to be applied manually
  handler = logging.handlers.SysLogHandler(address='/dev/log')
  formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s resource.service.name=%(otelServiceName)s] - %(message)s')
  handler.setFormatter(formatter)
  myLogger = logging.getLogger('MyLogger')
  myLogger.addHandler(handler)
  with tracer.start_as_current_span("one"):
    myLogger.info('one')
    with tracer.start_as_current_span("two"):
      myLogger.info('two')
      with tracer.start_as_current_span("three"):
        myLogger.info('three')

  # Need to sleep a bit to ensure all traces are sent
  time.sleep(10)
