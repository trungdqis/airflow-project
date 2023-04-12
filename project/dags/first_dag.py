from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    'first_dag',
    default_args={
        'email': ['trungdq.httt@gmail.com'],
        'email_on_failure': True,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='A first DAG sample by TrungDq',
    schedule_interval="@once",  # Run each one day
    start_date=datetime(2023, 4, 12),
    tags=['airflow_demo'],
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='echo Hello World',
    dag=dag
)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag
)

t3 = BashOperator(
    task_id='echo',
    bash_command='echo There is Airflow demo by Trungdq',
    dag=dag
)

t1 >> t2 >> t3
