import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# 1. Group runs under a named experiment
mlflow.set_experiment("driver_acceptance_prediction")

# 2. Simulate training data (mirroring our driver metrics)
X, y = make_classification(n_samples=1000, n_features=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Start an MLflow tracking run
with mlflow.start_run():
    # Hyperparameters
    n_estimators = 50
    max_depth = 4

    # Train model
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # Log parameters and metrics
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_metric("accuracy", acc)

    # Save the trained model artifact to MLflow
    mlflow.sklearn.log_model(model, "random_forest_model")

    print(f"Run completed! Model Accuracy: {acc:.4f}")