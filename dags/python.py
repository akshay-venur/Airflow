from airflow import DAG
from datetime import datetime , timedelta
from airflow.operators.python import PythonOperator 



def py_function(name ,age):
    print(f"hello this is python dag executed by {name} and his age is {age} ")


default_args = {
    "owner": "akshay kumar",
    "depends_on_fast" : False,
    "start_date" : datetime(2024,3,22),
    "email" : ["akshay16venur@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 1,
    "retries_delay": timedelta(minutes=1)

    }

with DAG(
    dag_id='python_dag',
    default_args=default_args,
    description='This is python dag',
    schedule_interval=timedelta(days=1),
    tags=['example'],
) as dag:
    
    t1 = PythonOperator(
        task_id = "python_task",
        python_callable = py_function,
        op_kwargs= {"name":"akshay kumar","age":24}
    )

t1