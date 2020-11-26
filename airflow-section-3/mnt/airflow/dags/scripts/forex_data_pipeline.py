from airflow import DAG
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow", 
    "start_date": datetime( 2019, 12, 4), 
    "depends_on_past": False, 
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "rossanomarcos@gmail.com"
    "retries": 1, 
    "retry_delay": timedelta(minutes=5), 
}

with DAG(dag_id="forex_data_pipeline", 
        schedule_interval="@daily", 
        default_args-default_args, 
        catchup=False) as dag:
    None
