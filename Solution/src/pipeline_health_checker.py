import re
def evaluate_pipeline_health(log):

    # Critical health status
    if log["status_code"] != 200 or (log["errors"] != [])\
    or log["duration_seconds"] > 1200 or log["max_latency_seconds"] > 30\
    or log["record_count"] == 0:

      log.update(health_status="Critical")


      # High Priority Alert
      time = log["ingestion_time"]

      result = re.search('[.*T].*[Z]', time)
      index1, index2 = result.span()
      new_time = time[index1+1:index2-1]

      if new_time >= "00:00:00" and new_time <= "04:00:00":
        log.update(health_status="High Priority Alert")


    # Warning health status
    elif log["status_code"] == 200 and ((log["duration_seconds"] >= 600 and log["duration_seconds"] <= 1200)\
    or (log["max_latency_seconds"] >= 10 and log["max_latency_seconds"] <= 30)\
    or ("late data arrival" not in log["warnings"]))\
    or (log["record_count"] < 100 and (log["errors"] == [])):
      log.update(health_status="Warning")


    # Healthy health status
    elif log["status_code"] == 200 and (log["errors"] == []) and\
    (log["warnings"] == [] or "late data arrival" in log["warnings"])\
    and (log["duration_seconds"] < 600) and (log["max_latency_seconds"] < 10):

      log.update(health_status="Healthy")


    return log
