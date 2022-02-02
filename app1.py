import time
import logging
import logging.handlers
import syslog

from opentelemetry import trace

if __name__ == "__main__":
  # Example 1: Default logging (which goes to sysout, not log observer, but applies the pattern correctly)
  tracer = trace.get_tracer(__name__)
  with tracer.start_as_current_span("Example 1 - foo"):
    logging.info('Example 1 - foo')
    with tracer.start_as_current_span("Example 1 - bar"):
      logging.info('Example 1 - bar')
      with tracer.start_as_current_span("Example 1 - baz"):
        logging.error('Example 1 - baz')
        print("Hello world from OpenTelemetry Python!")

  # Need to ensure all traces are sent
  trace.get_tracer_provider().shutdown()
