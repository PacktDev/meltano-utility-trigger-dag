from requests import post
from os import environ
from os.path import join

def main():
    print(f'URL : {environ.get("TRIGGER_DAG_URL")}')
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print(f'Username : {environ.get("TRIGGER_DAG_USERNAME")} and Password : {environ.get("TRIGGER_DAG_PASSWORD")}')
    response = post(
        url=environ.get('TRIGGER_DAG_URL'),
        auth=(
            environ.get('TRIGGER_DAG_USERNAME'),
            environ.get('TRIGGER_DAG_PASSWORD')
        ),
        json={
            "conf": {},
            "dag_run_id": f'{environ.get("AIRFLOW_CTX_DAG_ID")}_{environ.get("AIRFLOW_CTX_DAG_RUN_ID")}'
        }
    )
    print(f'Response Status Code >> {response.status_code}') 
    if response.status_code==200:
        return True
    else:
        response.raise_for_status()
