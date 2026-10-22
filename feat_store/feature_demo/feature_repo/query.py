from feast import FeatureStore

store = FeatureStore(repo_path=".")

# Fetch the live feature values for driver 1005
response = store.get_online_features(
    features=[
        "driver_hourly_stats:conv_rate",
        "driver_hourly_stats:acc_rate",
        "driver_hourly_stats:avg_daily_trips",
    ],
    entity_rows=[{"driver_id": 1005}],
).to_dict()

print(response)