import time
from opentelemetry import metrics
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.zipkin.json import ZipkinExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics._internal.export import ConsoleMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter

# Configure Jaeger exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

# zipkin_exporter = ZipkinExporter(
# )
# otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:6831")

reader = PeriodicExportingMetricReader(
    ConsoleMetricExporter()
)

# Create a meter provider and configure it to export metrics to Jaeger
meter_provider = MeterProvider(
 metric_readers=[reader],
 resource=Resource.create({SERVICE_NAME: "my-python-service"})
)

metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter(__name__)

# Create metrics
requests_counter = meter.create_counter(
    "requests",
    description="Number of requests",
    unit="1",
)
latency_histogram = meter.create_histogram(
    "request_latency",
    description="Request latency",
    unit="ms",
)

# Simulate some work and record metrics
for i in range(10):
    requests_counter.add(1)
    start_time = time.time()
    # Simulate some work here
    time.sleep(0.1)
    latency_histogram.record((time.time() - start_time) * 1000)