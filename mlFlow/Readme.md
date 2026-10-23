###### mlflow

```
Invoke-RestMethod -Uri "http://127.0.0.1:5000/invocations" -Method Post -ContentType "application/json" -Body '{"inputs": [[1.0, 2.0, 3.0, 4.0, 5.0], [6.0, 7.0, 8.0, 9.0, 10.0]]}'

```


###### serve model

```
 mlflow models serve -m "models:/random_forest_model/1" -p 5000 --no-conda
python -c "import mlflow; client = mlflow.tracking.MlflowClient(); [print(m.name, [v.version for v in client.get_latest_versions(m.name)]) for m in client.search_registered_models()]"

```

