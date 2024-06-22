from opentelemetry import metrics
from opentelemetry.exporter.zipkin.json import ZipkinExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
import time

# 1. Initialize Meter Provider (for metrics collection)
meter_provider = MeterProvider()
metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter(__name__)

# 2. Create Counter Instrument
counter = meter.create_counter(
    "my_counter",
    description="Counts the number of times this function is called",
    unit="1"
)

# 3. Metric Generation Function
def generate_metrics():
    for i in range(5):
        counter.add(1)
        print("Metric recorded!")
        time.sleep(2)  # Simulate work

# 4. Metric Exporters
# Console Exporter (for demo/debugging)
console_exporter = ConsoleMetricExporter()
meter_provider.start_pipeline(meter, console_exporter, 5)  # Export every 5 seconds

# Jaeger Exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)
meter_provider.start_pipeline(meter, jaeger_exporter, 5)

# Zipkin Exporter
zipkin_exporter = ZipkinExporter(
    endpoint="http://localhost:9411/api/v2/spans",
    local_endpoint="my_app_endpoint",  # Replace with your app's endpoint
)
meter_provider.start_pipeline(meter, zipkin_exporter, 5)

# 5. Generate and Export
if __name__ == "__main__":
    generate_metrics()