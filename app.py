import time
import logging
import logging.handlers
import syslog

from opentelemetry import trace

def merge(arr, l, m, r):
  n1 = m - l + 1
  n2 = r - m

  # create temp arrays
  L = [0] * (n1)
  R = [0] * (n2)

       # Copy data to temp arrays L[] and R[]
  for i in range(0, n1):
    L[i] = arr[l + i]

  for j in range(0, n2):
    R[j] = arr[m + 1 + j]

  # Merge the temp arrays back into arr[l..r]
  i = 0     # Initial index of first subarray
  j = 0     # Initial index of second subarray
  k = l     # Initial index of merged subarray

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
      k += 1

  # Copy the remaining elements of L[], if there
  # are any
  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

  # Copy the remaining elements of R[], if there
  # are any
  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted

def mergeSort(arr, l, r):
  if l < r:
    # Same as (l+r)//2, but avoids overflow for
    # large l and h
    m = l+(r-l)//2

    # Sort first and second halves
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
    merge(arr, l, m, r)

if __name__ == "__main__":
  tracer = trace.get_tracer(__name__)
  with tracer.start_as_current_span("foo"):
    logging.info('Foo')
    with tracer.start_as_current_span("bar"):
      logging.info('bar')
      with tracer.start_as_current_span("baz"):
        logging.error('baz')
        print("Hello world from OpenTelemetry Python!")

  with tracer.start_as_current_span("fi"):
    syslog.syslog('fi')
    with tracer.start_as_current_span("fie"):
      syslog.syslog('fie')
      with tracer.start_as_current_span("fofum"):
        syslog.syslog('fofum')

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

  # Driver code to test above
  arr = [12, 11, 13, 5, 6, 7]
  n = len(arr)
  print("Given array is")
  for i in range(n):
    print("%d" % arr[i], end=" ")

  mergeSort(arr, 0, n-1)
  print("\n\nSorted array is")
  for i in range(n):
    print("%d" % arr[i], end=" ")

  # Need to sleep a bit to ensure all traces are sent
  time.sleep(10)

# This code is contributed by Mohit Kumra
# to geeksforgeeks.org
# Modified by BG