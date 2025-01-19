from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_percentage_error
import pandas as pd

# Load the dataset
data = pd.read_csv('steel_combined_sensors_hourly.csv')

# Feature columns (excluding the Timestamp column)
features = ['CO Concentration (ppm)', 'CO2 Concentration (ppm)', 'Temperature (°C)']

# Target parameters to predict
targets = ['Current (A)', 'CO Concentration (ppm)', 'CO2 Concentration (ppm)']

# Dictionary to store predictions for each parameter
predictions = {}

# Train and predict for each target parameter
for target in targets:
    X = data[features]
    y = data[target]
    
    # Initialize SVR model
    svr_model = SVR(kernel='rbf')
    
    # Train the SVR model on the entire dataset
    svr_model.fit(X, y)
    
    # Predict for every row in the dataset
    y_pred = svr_model.predict(X)
    
    # Calculate MAPE for the model
    mape = mean_absolute_percentage_error(y, y_pred) * 100
    print(f"{target} - SVR Model MAPE: {mape:.2f}%")
    
    # Save predictions
    predictions[target] = y_pred

# Now, create a DataFrame with the predictions and actual values
results_df = pd.DataFrame({
    'Timestamp': data['Timestamp'],
    'Actual_Current': data['Current (A)'],
    'Predicted_Current': predictions['Current (A)'],
    'Actual_CO': data['CO Concentration (ppm)'],
    'Predicted_CO': predictions['CO Concentration (ppm)'],
    'Actual_CO2': data['CO2 Concentration (ppm)'],
    'Predicted_CO2': predictions['CO2 Concentration (ppm)']
})

# Save the results to a CSV file (matching the number of rows in the original dataset)
results_df.to_csv('svr_predictions.csv', index=False)
print("Predictions saved to 'svr_predictions.csv'.")
