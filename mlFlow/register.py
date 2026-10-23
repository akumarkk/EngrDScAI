import mlflow

result = mlflow.register_model(
    model_uri="runs:/fc91fe21f90c4186af12143930adfe15/random_forest_model",
    name="random_forest_model"
)