from pipeline_health_checker import evaluate_pipeline_health

def main():
    pipeline_log = {
        "pipeline_name": "user_events_ingestion",
        "status_code": 200,
        "duration_seconds": 452,
        "record_count": 124500,
        "max_latency_seconds": 5.6,
        "errors": [],
        "warnings": ["late data arrival"],
        "ingestion_time": "2025-10-08T02:30:00Z",
        "source": "kafka"
    }

    result = evaluate_pipeline_health(pipeline_log)
    print(result)

if __name__ == "__main__":
    main()
