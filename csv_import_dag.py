import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import retrieve_csv
from retrieve_csv import main



DAG_START_DATE = datetime(2023, 1, 15, 19, 45)

DAG_DEFAULT_ARGS = {
    'owner': 'airflow',
    'start_date': DAG_START_DATE,
    'retries': 1,
    'retry_delay': timedelta(seconds = 5)
}


with DAG('pandas_read_csv_dag', default_args= DAG_DEFAULT_ARGS, schedule_interval='0 1 * * *') as dag:

    read_csv_task = PythonOperator(
        task_id='read_csv',
        python_callable= retrieve_csv.main,
        #op_kwargs = {'filepath': CSV_PATH},
        dag=dag
        )
    read_csv_task
