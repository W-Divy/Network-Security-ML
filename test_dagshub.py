import dagshub
import mlflow

# Connect MLflow to your DagsHub repository
dagshub.init(
    repo_owner="W-Divy",
    repo_name="Network-Security-ML",
    mlflow=True
)

print("Tracking URI:", mlflow.get_tracking_uri())

# Create an experiment and log a test run
mlflow.set_experiment("NetworkSecurity-Test")

with mlflow.start_run(run_name="connection-test"):
    mlflow.log_param("model", "test-model")
    mlflow.log_metric("f1_score", 0.95)

print("Test run logged successfully!")