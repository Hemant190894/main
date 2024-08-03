import os
import sys
from datetime import datetime
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator  # Import DummyOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

local_tz = pendulum.timezone("Asia/Kolkata")

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline

default_args = {
    'owner': 'Hemant Dayma',
    'start_date': datetime(2024, 7, 31, tzinfo=local_tz),
}

# Use local_tz for file postfix
file_postfix = datetime.now(local_tz).strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# Define start and end dummy tasks
start = DummyOperator(
    task_id='start',
    dag=dag
)
# extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'Python',
        'time_filter': 'day',
        'limit': 1000
    },
    dag=dag
)
# upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

end = DummyOperator(
    task_id='end',
    dag=dag
)

start >> extract >> upload_s3 >> end