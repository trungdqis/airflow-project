from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def process_greeting(ti, *args, **kwargs):
    gr = ti.xcom_pull(task_ids=['greeting'])
    if not gr:
        raise Exception('No greeting value.')

    variable = kwargs.get("name", "Didn't get the key")
    print(gr[0] + ' ' + variable)
    return gr[0] + ' ' + variable


with DAG(
        dag_id='first_dag',
        description='A first DAG sample by TrungDq',
        schedule_interval="* * * * *",
        # Run each one minute, hour, day, month, year,... using @once,... or like currently
        start_date=datetime(2023, 4, 13),
        tags=['airflow_demo'],
        catchup=False
) as dag:
    # 1. Get current datetime
    task_greeting = BashOperator(
        task_id='greeting',
        bash_command='echo Hello'
    )

    # 2. Process current datetime
    task_process_greeting = PythonOperator(
        task_id='process_greeting',
        python_callable=process_greeting,
        op_kwargs={"name": "Quoc Trung"}
    )

    task_greeting >> task_process_greeting
