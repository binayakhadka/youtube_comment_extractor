from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from youtube import youtube_comments

# Define the default_args for the DAG
default_args = {
   'owner': 'bk',
   'start_date': datetime(2023, 8, 31),   #date can't have 08
   'retries': 1,
   'retry_delay': timedelta(minutes=2)
}
# Create a DAG instance
dag = DAG(
   'YC',
   default_args=default_args,
   description='Gets comments from YouTube video',
   start_date =  datetime(2023, 8, 31),
   schedule_interval='@daily',
   catchup = True
)

task1 = PythonOperator(
   task_id='YouTube',
   python_callable=youtube_comments,
   dag=dag
   )

task1