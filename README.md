# otpro10
OTPRO labs

# ЛР №10: Time Series база данных Prometheus

## Описание лабораторной работы
Разработан экспортёр метрик на Python, он собирает данные об использовании процессора, оперативной памяти и дискового пространства. Экспортёр интегрирован с Prometheus для сбора метрик и выполнения запросов на их основе.

## Сбор метрик
Экспортёр собирает следующие метрики:
- **Использование процессоров**: процент загрузки каждого ядра CPU.
- **Использование памяти**:
  - Общее количество доступной оперативной памяти.
  - Объём используемой памяти.
- **Использование дисков**:
  - Общий объём дискового пространства.
  - Используемый объём дискового пространства.

Метрики доступны по корневому пути `/` в формате, совместимом с Prometheus.

## Запросы PromQL
Для анализа собранных данных можно использовать следующие запросы PromQL:

1. **Использование процессоров**:
   ```promql
   avg(cpu_usage) by (core)
   ```
   Рассчитывает среднюю загрузку процессоров по ядрам.

2. **Используемая память (в процентах)**:
   ```promql
   (memory_used / memory_total) * 100
   ```
   Показывает процент используемой оперативной памяти.

3. **Используемое место на диске (в процентах)**:
   ```promql
   (disk_used / disk_total) * 100
   ```
   Показывает процент использованного дискового пространства.

## Инструкция по запуску

### Установка и запуск экспортёра
1. Клонируйте репозиторий с экспортёром:
   ```bash
   git clone https://github.com/LizzBizzLol/otpro10.git
   cd otpro10
   ```
2. Установите зависимости Python:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите экспортёр:
   ```bash
   python exporter.py
   ```
   Экспортёр будет работать по адресу `http://127.0.0.1:8000` (если переменные окружения не переопределены).

### Настройка Prometheus
1. Скачайте и распакуйте Prometheus с [официального сайта](https://prometheus.io/download/).
2. В файле `prometheus.yml` добавьте следующую конфигурацию для сбора метрик с экспортёра:
   ```yaml
   scrape_configs:
     - job_name: "exporter"
       static_configs:
         - targets: ["127.0.0.1:8000"]
   ```
3. Запустите Prometheus:
   ```bash
   prometheus --config.file=prometheus.yml
   ```
   Интерфейс Prometheus будет доступен по адресу `http://127.0.0.1:9090`.

## Результаты работы
- Экспортёр собирает и предоставляет метрики.
- Prometheus интегрируется с экспортёром и выполняет запросы PromQL.
