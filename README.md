## 19522419 - 19522534 - 19522538 - 19522285 - Apache Airflow

### How to install Apache Airflow using Docker 
*Execute the following commands* 

- Check Docker And Docker compose installation \
`docker --version` and `docker-compose --version`
- Clone docker-compose.yaml file \
`curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.2/docker-compose.yaml'` \
*Edit according to me or copy if necessary*
- Create 3 folder `dags`, `logs` and `plugins` inside main folder (`project`)
- Initialize necessary configuration of Apache Airflow
`docker compose up airflow-init` 
- Run project \
`docker-compose up -d` 

- Access Admin UI and login \
`http://localhost:8080` and login with account `airflow` - `airflow` 

- Install `apache-airflow` package by accessing inside `Scripts` folder and execute `activate.bat`, then execute `pip install apache-airflow`

### How to fix errors during installation: 
https://stackoverflow.com/questions/70687650/invoke-webrequest-a-parameter-cannot-be-found-that-matches-parameter-name-lfo

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

### Ref Video: 
https://www.youtube.com/watch?v=KM5TkCPyIzc&ab_channel=sumitkumar

### Document
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html