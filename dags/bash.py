from airflow import DAG
from datetime import datetime , timedelta
from airflow.operators.bash import BashOperator

default_args ={
    'owner': 'akshay kumar',
    'depends_on_fast': False,
    'start_date': datetime(2024,3,21),
    'email': ['akshay16venur@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retries_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='first_dag',
    default_args=default_args,
    description='This is the first dag',
    schedule=timedelta(days=1),
    tags=['example'],
) as dag:
    
    t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

t4 = BashOperator(
    task_id='echo_hello',
    bash_command='echo "Hello, Airflow!"',
    dag=dag
)

t3 = BashOperator(
    task_id="also_run_this",
    bash_command='echo "ti_key={{ task_instance_key_str }}"',
)


t1 >> [t2,t3] >> t4