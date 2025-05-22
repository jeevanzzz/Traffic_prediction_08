# 🚦 Traffic Prediction using Machine Learning Technique 
A web-based application that predicts traffic volume based on environmental conditions and calendar inputs using a trained deep learning model.

## 🧠 Overview
This project uses a **Multi-Layer Perceptron (MLP) Regressor** to predict traffic volume based on factors such as weather, temperature, time, date, and holiday status to receive a predicted traffic volume and classification (e.g., LOW, MODERATE, HIGH).. The application is built using **Flask** and features a user-friendly frontend for input and visualization.

## 📁 Project Structure

![image](https://github.com/user-attachments/assets/f0eefd67-66b0-41b5-a449-92b9df1f6679)

## 💡 Features
- Interactive web interface built with HTML/CSS and Flask
- Web Interface: Simple UI to input conditions and receive predictions
- ML Model: Uses MLPRegressor from scikit-learn for regression on normalized data
- Dynamic background visuals based on weather selection
- Real-time traffic volume prediction
- Custom statement generation describing predicted traffic conditions
- Machine learning model trained on historical traffic data

## 🛠️ Installation & Setup
- Prerequisites
- Python 3.x
- Flask
- pandas
- scikit-learn

### Setup Instructions
**1. Clone the repository**
`git clone https://github.com/jeevanzzz/traffic-prediction.git`
`cd traffic-prediction`

**2. Install dependencies**
`pip install -r requirements.txt`

**3. Run the Flask application**
`python app.py`

## 🚀 Usage
**1. Train the Model**
- The model is automatically trained when you run the app (model.py handles this during import).
-  Make sure data/traffic_volume_data.csv exists and is formatted correctly.
  
**2. Run the Flask App**
     `python app.py`

**3. Open in Browser**
     - Navigate to:
      `http://127.0.0.1:5000/`

**4. Use the App**
- Click "Click me to Train Model" on the homepage.
- Enter details: date, time, weather, holiday, temperature, etc.
- Click Predict.
- View prediction result with a descriptive traffic statement.

## 📈 Machine Learning Model
- **Model Type**: MLP Regressor (scikit-learn)
- **Data Source**: Cleaned traffic volume dataset including weather and time-related features.
- **Scaling**: MinMaxScaler applied to features and target variable.
- **Evaluation Metric**: Mean Absolute Error (MAE)

## 📄 Dataset Description
**The dataset includes over 33,000 entries and contains features such as:**
- date_time, is_holiday, temperature
- weather_type, weather_description
- traffic_volume

**Preprocessing steps include:**
- Encoding categorical features
- Handling missing values
- Feature scaling

## 🧠 How It Works
- User inputs relevant details (date, time, weather, etc.)
- Inputs are transformed into a feature vector.
- Trained model predicts traffic volume.
- Volume is categorized and displayed in a user-friendly format.

## 📚 Project Report
- Introduction and problem statement
- Methodology and ML lifecycle
- Data preprocessing and visualization
- Model training and evaluation
- Results and future scope

## 📌 Future Scope
- Integration with real-time traffic APIs
- Deploy using Docker or cloud platforms
- Extend to city-level traffic analysis
- Use of advanced deep learning models (e.g., LSTM)
  
## 📸 Screenshots
### Result and Analysis

![image](https://github.com/user-attachments/assets/22004250-d8a7-435d-a7f3-cbae45a780f0)

  **Figure 1:** Traffic Prediction Using Machine Learning(HOME PAGE)
  
![image](https://github.com/user-attachments/assets/815256c6-e1d2-4817-ba81-38f0a62af9bf)

   **Figure 2:** Traffic Prediction Using Deep Learning (INPUT INTERFACE)
  
![image](https://github.com/user-attachments/assets/93a8cc0c-53bc-4469-ba66-24acd77a68ec)

  **Figure 3:** Traffic Prediction Using Deep Learning (RESULT INTERFACE)   

## 📃 License
- This project is licensed under the MIT License.
- You may freely use, modify, and distribute this software with proper attribution.

## 📬 Contact
For any questions, feedback, or contributions:
- Open an [issue](https://github.com/jeevanzzz/Traffic_prediction_08-/issues)
- Or contact the repository owner via [GitHub profile](https://github.com/jeevanzzz)

  
# "Predict tomorrow’s traffic today — smart, simple, and data-driven."
