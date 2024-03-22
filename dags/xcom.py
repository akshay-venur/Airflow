from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta 

def py_fun(task_instance):
    # return "akshay"
    task_instance.xcom_push(key='name',value='akshay Kumar')
    task_instance.xcom_push(key='age',value=24)
    task_instance.xcom_push(key='place',value='mangalore')

def get_state_fun(task_instance):
    task_instance.xcom_push(key='state',value='karnataka')


def py_print(task_instance):
    name  = task_instance.xcom_pull(task_ids='py_call1',key='name')
    age = task_instance.xcom_pull(task_ids = 'py_call1',key='age')
    place = task_instance.xcom_pull(task_ids='py_call1',key='place')
    state = task_instance.xcom_pull(task_ids='get_state',key='state')
    print(f"my name is {name} and my age is {age} and i am from {place} and state is {state}")


default_args = {'owner': "akshay kumar",
    "owner": "akshay kumar",
    "depends_on_fast" : False,
    "start_date" : datetime(2024,3,22),
    "email" : ["akshay16venur@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 1,
    "retries_delay": timedelta(minutes=1)
        }

with DAG(dag_id='xcom_dag',
        default_args=default_args,
        description='this is xcom dag',
        schedule_interval= timedelta(days=1),
        catchup=False,
        tags=['example']
) as dag:

    t1 = PythonOperator(
        task_id ='py_call1',
        python_callable= py_fun
    )  

    t2 = PythonOperator(
        task_id = 'get_state',
        python_callable= get_state_fun
    )

    t3 = PythonOperator(
        task_id = "py_call2",
        python_callable = py_print,
        op_kwargs = {"age":24}
    )


    t1 >> t2  >> t3