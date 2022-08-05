from requests import post
from os import environ
from os.path import join

def main():
    response = post(
        url=environ.get('TRIGGER_DAG_URL')
        auth=(
            environ.get('TRIGGER_DAG_USERNAME'),
            environ.get('TRIGGER_DAG_PASSWORD')
        )
        json={
            conf: {},
            dag_run_id: f'{environ.get('AIRFLOW_CTX_DAG_ID')}_{environ.get('AIRFLOW_CTX_DAG_RUN_ID')}'
        }
    )
    if response.status is 200:
        return True
    else:
        response.raise_for_status()
