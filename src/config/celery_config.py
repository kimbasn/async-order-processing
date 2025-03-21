# -*- coding: utf-8 -*-
"""
Copyright: Wilde Consulting
  License: Apache 2.0

VERSION INFO::
    $Repo: fastapi_celery
  $Author: Anders Wiklund
    $Date: 2023-08-27 14:34:48
     $Rev: 46
"""

# Local modules
from .setup import config

# ---------------------------------------------------------

# Broker settings.
broker_url = config.rabbit_url

# Using the database to store task state and results.
result_backend = config.redis_url

# Add input parameters to backend result (used by retry endpoint).
result_extended = True

# List of modules to import when the Celery
# worker starts (improves start time).
imports = ('src.worker.tasks', 'src.worker.customers_tasks',
           'src.worker.employees_tasks', 'src.worker.orders_tasks',
           'src.worker.quotations_tasks', 'src.worker.realisations_tasks')

# Normalize logging format.
worker_log_format = '%(asctime)s | %(levelname)-8s | %(processName)s | %(message)s'
worker_task_log_format = '%(asctime)s | %(levelname)-8s | %(processName)s | ' \
                         '%(task_name)s[%(task_id)s] | %(message)s'

# Decrease the message rates substantially.
worker_send_task_event = False

# task messages will be acknowledged after the task has been executed,
# not just before (the default behavior).
task_acks_late = True

# One worker takes 10 tasks from queue at a time
# and will increase the performance.
worker_prefetch_multiplier = 10

# task will be killed after 60 seconds
# task_time_limit = 60

# task will raise exception SoftTimeLimitExceeded after 50 seconds.
# task_soft_time_limit = 50
