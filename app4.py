import time
import logging
import logging.handlers
import syslog

from opentelemetry import trace

if __name__ == "__main__":
  # Example 4: Applies a handler to send to syslog; in this case the formatter 
  #            is applied manually. This is the only one I get trace correlation working
  #            (although interestingly I see duplicate logs)
  tracer = trace.get_tracer(__name__)
  handler = logging.handlers.SysLogHandler(address='/dev/log')
  formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s resource.service.name=%(otelServiceName)s] - %(message)s')
  handler.setFormatter(formatter)
  myLogger = logging.getLogger('MyLogger')
  myLogger.addHandler(handler)
  with tracer.start_as_current_span("Example 4 - A"):
    myLogger.info('Example 4 - A')
    with tracer.start_as_current_span("Example 4 - B"):
      myLogger.info('Example 4 - B')
      with tracer.start_as_current_span("Example 4 - C"):
        myLogger.info('Example 4 - C')

  # Need to ensure all traces are sent
  trace.get_tracer_provider().shutdown()
