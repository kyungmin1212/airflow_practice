from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
from utils.common_func import regist

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 6, 14, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    regist_t1 = PythonOperator(
        task_id="regist_t1",
        python_callable=regist,
        op_args=["km", "man", "kr", "seoul"],
        op_kwargs={"email": "uiuiui12@naver.com", "phone": "010"},
    )

    regist_t1
