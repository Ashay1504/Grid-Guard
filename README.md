# Grid-Guard: Energy Emissions Dashboard

Grid-Guard is an innovative real-time energy emissions dashboard designed to monitor energy consumption, sensor data, and environmental factors. By integrating data from various sensors, such as current sensors (ACS712), CO sensors (MQ-7), and CO2 sensors (MH-Z19), Grid-Guard provides actionable insights to optimize energy usage and reduce environmental impact. Additionally, the system leverages machine learning (SVR models) to predict future trends and allows for automated control actions, such as activating ventilation, reducing load, and optimizing HVAC systems.

## Features

### 📈 Real-Time Monitoring
- Visualize current, CO, and CO2 levels over time using interactive graphs.

### 🧪 Predictive Analytics
- Uses Support Vector Regression (SVR) models to predict future sensor data and trends.

### ⚙️ Control Actions
- Choose from multiple automated control actions, such as:
  - Activating ventilation systems
  - Reducing energy load
  - Optimizing HVAC efficiency

### ⚠️ Warnings & Recommendations
- Receive real-time alerts when sensor data exceeds safe thresholds.
- Get actionable recommendations for better energy management.

### 🗃️ Custom CSV Upload
- Upload your own CSV files to generate custom graphs and predictions.

### 🌍 Report Generation
- Generate and download detailed reports on the latest sensor readings, predictions, and control actions.

## ⚛️ Technologies Used

- **Streamlit**: Web framework for creating interactive dashboards.
- **Plotly**: Interactive data visualization.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Synthetic sensor data generation and noise handling.
- **Scikit-learn (SVR)**: Machine learning model for sensor data predictions.

## 💡 Usage Guide

1. **Monitor Sensors**: View real-time graphs displaying current, CO, and CO2 sensor data.
2. **Predict Future Values**: Utilize machine learning predictions for upcoming energy and environmental trends.
3. **Take Control Actions**: Activate ventilation, reduce load, or optimize HVAC systems for improved efficiency.
4. **Get Alerts**: Receive instant notifications when sensor values exceed safe limits.
5. **Generate Reports**: Download CSV reports summarizing system status and predictions.

## 🛠️ Project Structure

- **`app.py`**: Main Streamlit application script.
- **`steel_combined_sensors_hourly.csv`**: Sample sensor data for monitoring.
- **`svr_predictions.csv`**: Example SVR model predictions.
- **`requirements.txt`**: List of Python dependencies for the project.
- **`README.md`**: Project documentation.

## 👥 Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

Contributions in the form of new features, bug fixes, or documentation improvements are highly appreciated!

## 📢 License
This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to reach out with any questions or suggestions!

Happy coding! 💪


