Grid-Guard is an innovative energy emissions dashboard designed to monitor energy consumption, sensor data, and environmental factors in real-time. It integrates sensor data from various devices such as current sensors (ACS712), CO sensors (MQ-7), and CO2 sensors (MH-Z19) to provide actionable insights for optimizing energy usage and reducing environmental impact. The system uses machine learning (SVR models) to predict future data, and allows for automated control actions like activating ventilation, reducing load, and optimizing HVAC.

Features
Real-Time Monitoring: Visualize current, CO, and CO2 levels over time using interactive graphs.
Predictive Analytics: Uses SVR (Support Vector Regression) models to predict future sensor data.
Control Actions: Choose from multiple actions such as activating ventilation, reducing load, or optimizing HVAC systems to ensure safe and efficient operations.
Warnings & Recommendations: Get real-time warnings if sensor data exceeds specified thresholds, along with actionable recommendations for better energy management.
Custom CSV Upload: Upload your own CSV files to generate graphs and predictions based on custom data.
Report Generation: Generate and download a report of the latest sensor readings, predictions, and control actions.
Technologies Used
Streamlit: Web framework for creating interactive dashboards.
Plotly: For visualizing sensor data and predictions in an interactive graph format.
Pandas: Data manipulation and analysis.
Numpy: For generating synthetic sensor data and noise.
Scikit-learn (SVR): For predicting sensor data using machine learning models.

Usage
Monitor Sensors: View real-time graphs for current, CO, and CO2 sensor data.
Predict Future Values: See predictions for current, CO, and CO2 levels based on your sensor data and machine learning models.
Control Actions: Choose actions like activating ventilation, reducing load, or optimizing HVAC to take real-time control of the system.
Get Alerts: Receive alerts and recommendations when sensor values exceed safe thresholds.
Generate Reports: Download CSV reports of the current system status.
Project Structure
app.py: Main Streamlit app script that contains the logic for the dashboard.
steel_combined_sensors_hourly.csv: Example sensor data for monitoring.
svr_predictions.csv: Example predictions generated from the SVR model.
requirements.txt: List of Python dependencies for the project.
README.md: Project documentation.
Contributing
If you'd like to contribute to Grid-Guard, feel free to fork this repository, make your changes, and submit a pull request. Contributions in the form of new features, bug fixes, or improvements to the documentation are welcome!
