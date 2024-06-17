import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler # For scaling the data
from sklearn.neural_network import MLPRegressor # Neural network model
from sklearn.model_selection import train_test_split # For splitting the data into training and testing sets
from sklearn.metrics import mean_absolute_error # For evaluating the model

# Load the traffic volume data from CSV file
data = pd.read_csv("data/traffic_volume_data.csv")

# Define columns with numeric and label data
label_columns = ['weather_type', 'weather_description']
numeric_columns = ['is_holiday', 'temperature',
                   'weekday', 'hour', 'month_day', 'year', 'month']

# Prepare the feature (X) and target (y) dataframes
features = numeric_columns # Use only numeric columns for features
target = ['traffic_volume']
X = data[features]
y = data[target]

# Scale the feature data using MinMaxScaler
x_scaler = MinMaxScaler()
X = x_scaler.fit_transform(X)

# Scale the target data using MinMaxScaler and flatten it
y_scaler = MinMaxScaler()
y = y_scaler.fit_transform(y).flatten()

# Create and train the MLPRegressor model
model = MLPRegressor(random_state=1, max_iter=500).fit(X, y)