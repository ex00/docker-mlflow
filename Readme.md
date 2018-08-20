## Non-official docker image for [MLflow](https://github.com/mlflow/mlflow)
[MLflow documentation](https://mlflow.org/docs/latest/index.html)

### Build

```
git clone https://github.com/ex00/docker-mlflow.git
cd docker-mlflow
docker build -t ex00/mlflow .
```

### Usage
```
docker run -d -p 5000:5000 -p 6233:6233 --name ex00/docker-mlflow mlflow
```
after first build you can use next command:
```
docker start ex00/docker-mlflow
```
### Run examples
```
docker exec -i ex00/docker-mlflow python /examples/example.py
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
docker exec -i ex00/docker-mlflow mlflow sklearn serve --port 6233 -r 92568a4725634a6abbca71bf1ef3fdfc model
curl -d '[{"x": 1}, {"x": -1}]' -H 'Content-Type: application/json' -X POST $(docker-machine ip):6233/invocations
```

### Run example project in docker
```
docker exec -i ex00/docker-mlflow mlflow run https://github.com/mlflow/mlflow-example.git -P alpha=0.4
```

### Example log local model in docker mlflow
```
python examples/test_connect_to_docker.py http://$(docker-machine ip):5000
```
