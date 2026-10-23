import mlflow
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# 1. Define the URI of the already logged model
# Replace with your actual run ID from the MLflow UI
run_id = "random_forest_model"

# 2. Load the model for inference
# # If it's a scikit-learn model with tree structures, pass trusted types if needed:
# loaded_model = mlflow.pyfunc.load_model(
#     model_uri, 
#     skops_trusted_types=["sklearn.tree._tree.Tree"]
# )

# loaded_model = mlflow.sklearn.load_model(
#     model_uri, 
#     skops_trusted_types=["sklearn.tree._tree.Tree"]
# )
run_id = "fc91fe21f90c4186af12143930adfe15"
model_uri = f"runs:/{run_id}/random_forest_model"

loaded_model = mlflow.pyfunc.load_model(f"runs:/{run_id}/random_forest_model")
print(f"Loading model from: {model_uri}")

#loaded_model = mlflow.pyfunc.load_model(model_uri)

# 3. Generate sample test data
_, X_test, _, y_test = train_test_split(
    *make_classification(n_samples=100, n_features=5, random_state=42),
    test_size=0.2,
    random_state=42
)
test_df = pd.DataFrame(X_test, columns=[f"feature_{i}" for i in range(5)])
test_df["target"] = y_test

# 4. Run Inference Test
print("--- Running Live Inference ---")
sample_features = test_df.drop(columns=["target"]).iloc[:3]
predictions = loaded_model.predict(sample_features)
print(f"Predictions for first 3 samples: {predictions}")

# 5. Run Automated Evaluation Against Ground Truth
print("\n--- Running Automated Evaluation Suite ---")
evaluation_result = mlflow.evaluate(
    model=model_uri,
    data=test_df,
    targets="target",
    model_type="classifier",
)

print(f"Evaluated Accuracy: {evaluation_result.metrics['accuracy_score']:.4f}")
print(f"Evaluated Precision: {evaluation_result.metrics['precision_score']:.4f}")