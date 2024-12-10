from prometheus_client import start_http_server, Gauge
import psutil
import time
import os

# Переменные окружения
EXPORTER_HOST = os.getenv("EXPORTER_HOST", "127.0.0.1")
EXPORTER_PORT = int(os.getenv("EXPORTER_PORT", 8000))

# Метрики
cpu_usage = Gauge("cpu_usage", "CPU usage percentage per core", ['core'])
memory_total = Gauge("memory_total", "Total memory in bytes")
memory_used = Gauge("memory_used", "Used memory in bytes")
disk_total = Gauge("disk_total", "Total disk space in bytes")
disk_used = Gauge("disk_used", "Used disk space in bytes")

def collect_metrics():
    # CPU usage
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpu_usage.labels(core=f"core_{i}").set(percentage)

    # Memory usage
    mem = psutil.virtual_memory()
    memory_total.set(mem.total)
    memory_used.set(mem.used)

    # Disk usage
    disk = psutil.disk_usage('/')
    disk_total.set(disk.total)
    disk_used.set(disk.used)

if __name__ == "__main__":
    # Запускаем сервер Prometheus
    start_http_server(EXPORTER_PORT, addr=EXPORTER_HOST)
    print(f"Exporter running on {EXPORTER_HOST}:{EXPORTER_PORT}")

    while True:
        collect_metrics()
        time.sleep(5)  # Сбор метрик каждые 5 секунд
