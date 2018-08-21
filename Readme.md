## Non-official docker image for [MLflow](https://github.com/mlflow/mlflow)
[MLflow documentation](https://mlflow.org/docs/latest/index.html)

### Build

```
git clone https://github.com/ex00/docker-mlflow.git
cd docker-mlflow
docker build -t ex00/docker-mlflow .
```

### Usage
```
docker run -d -p 5000:5000 -p 6233:6233 --name mlflow-container ex00/docker-mlflow
```
after first build you can use next command:
```
docker start mlflow-container
```
### Run examples
```
docker exec -i mlflow-container python /examples/example.py
```
You should get same output in console
```
Running example.py
Train model
Score of LogisticRegression: 0.6666666666666666
Model saved in run 92568a4725634a6abbca71bf1ef3fdfc
Success
```
Also you can check results in mlflow ui - `http://$(docker-machine ip):5000`

run and check model:

```
docker exec -i mlflow-container mlflow sklearn serve --port 6233 --host 0.0.0.0 -r 92568a4725634a6abbca71bf1ef3fdfc model
curl -d '[{"x": 1}, {"x": -1}]' -H 'Content-Type: application/json' -X POST $(docker-machine ip):6233/invocations
```
result:
```
{
    "predictions": [
        1,
        0
    ]
}
```

### Run example project in docker
```
docker exec -i mlflow-container mlflow run https://github.com/mlflow/mlflow-example.git -P alpha=0.4
```

### Example log local model in docker mlflow
```
python examples/test_connect_to_docker.py http://$(docker-machine ip):5000
```
