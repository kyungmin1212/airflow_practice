from airflow import DAG
import pendulum

# from airflow.operators.python import PythonOperator
from airflow.decorators import task
import random

with DAG(
    dag_id="dags_python_decorators",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 6, 16, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    @task(task_id="python_task_1")
    def select_fruit():
        fruit = ["APPLE", "BANANA", "ORANGE", "AVOCADO"]
        rand_int = random.randint(0, 3)
        print(fruit[rand_int])

    python_task_1 = select_fruit()

    python_task_1
