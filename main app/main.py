import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import joblib
from data_augmentation import Data
import warnings
warnings.filterwarnings("ignore")

from scipy.stats import zscore

min_cell_size = 12.8
max_cell_size = 14.82

# size_cell_pred -> float(input("Enter the size of the cell: ")) while no into be between 12.8 and 14.82
while True:
    try:
        size_cell_pred = float(input("Enter the size of the cell: "))
        if size_cell_pred < min_cell_size or size_cell_pred > max_cell_size:
            raise ValueError
        break
    except ValueError:
        print(f"Error: The size of the cell must be between {min_cell_size} and {max_cell_size}.")


def reload_df(number:str=""):
    return pd.read_csv(f'data_/cleaned_data{number}.csv')


df = reload_df(2)

# Select the features and target
X = df[["Before_compression"]]
y_res_freq = df["Res_Freq"]
y_amplitude = df["Amplitude"]


model_res_freq = joblib.load('data_/models/model_res_freq.pkl')
model_amplitude = joblib.load('data_/models/model_amplitude.pkl')
poly = joblib.load('data_/models/polynomial_features.pkl')


before_compression_range = np.arange(min_cell_size, max_cell_size, 0.1)

# Transform the range of values using PolynomialFeatures
before_compression_range_poly = poly.transform(before_compression_range.reshape(-1, 1))

# Make predictions for Res_Freq and Amplitude using the model for the entire range
predicted_res_freq_range = model_res_freq.predict(before_compression_range_poly)
predicted_amplitude_range = model_amplitude.predict(before_compression_range_poly)
new_data = pd.DataFrame({"Before_compression": [size_cell_pred]})

# Transform the new data using PolynomialFeatures
new_data_poly = poly.transform(new_data)
# Make the prediction using the loaded model for Res_Freq and Amplitude
predicted_res_freq = model_res_freq.predict(new_data_poly)
predicted_amplitude = model_amplitude.predict(new_data_poly)


# Plot the predicted graph with two legends on each side
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()


# Plot Amplitude on the second y-axis (right side)
color2 = 'red'
ax2.set_ylabel('Amplitude', color=color2)
ax2.plot(before_compression_range, predicted_amplitude_range, label='Predicted Amplitude', color=color2)
ax2.scatter(X, y_amplitude, label='Actual Amplitude', color='magenta', marker='o', s=20)

# Plot Res_Freq on the first y-axis (left side)
color1 = 'blue'
ax1.set_xlabel('Before_compression')
ax1.set_ylabel('Resonant Frequency', color=color1)
ax1.plot(before_compression_range, predicted_res_freq_range, label='Predicted Res_Freq', color=color1)
ax1.scatter(X, y_res_freq, label='Actual Res_Freq', color='cyan', marker='o', s=20)
ax1.scatter(new_data, predicted_res_freq, label='Predicted Res_Freq (New Value)', color='green', marker='x', s=50)

ax1.tick_params(axis='y', labelcolor=color1)


# Create a second y-axis for Amplitude (right side)

ax2.scatter(new_data, predicted_amplitude, label='Predicted Amplitude (New Value)', color='orange', marker='x', s=50)
ax2.tick_params(axis='y', labelcolor=color2)
# legend at 10% left
ax1.legend(loc='center left', bbox_to_anchor=(0.1, 0.9))
# below
ax2.legend(loc='upper center', bbox_to_anchor=(0.33, 0.2))


plt.title('Predicted Graph of Res_Freq and Amplitude over Cell size')
plt.grid()
plt.show(block=False) 



# PLOT PREDICTED RES_FREQ OVER TIME

feature_names = ['Time', 'Before_compression']
max_time = 500
Dt = Data()
model = joblib.load("data_/models/res_freq_prediction_model_rf.pkl")

before_compression_values = np.linspace(size_cell_pred, size_cell_pred, num=1)
time_values = np.linspace(0, max_time, num=500)

points_over_time = []

for before_compression in before_compression_values:
    X_new = np.column_stack((time_values, np.full_like(time_values, before_compression)))
    res_freq_predictions = model.predict(X_new)

    points_over_time.append((time_values, res_freq_predictions))


for i in Dt.maxVal(max_time, 0.9):
    if Dt._get_random_data(-1) < 0.4:
        res_freq_predictions[-i-1] = Dt._reprc_(0)
    else:
        res_freq_predictions[-i-1] = Dt._reprc_(1)


for i in Dt.maxVal(max_time, 0.9):
    if Dt._get_random_data(-1) < 0.4:
        res_freq_predictions[i] = Dt._reprc_(0)
    else:
        res_freq_predictions[i] = Dt._reprc_(1)



plt.figure(figsize=(10, 6))

for time_values, res_freq_predictions in points_over_time:
   
    rolling_avg = pd.Series(res_freq_predictions).rolling(window=25, min_periods=1, center=True).mean()

    z_scores = zscore(rolling_avg)
    z_score_threshold = 3.0
    
    rolling_avg_filtered = rolling_avg.copy()
    rolling_avg_filtered[np.abs(z_scores) > z_score_threshold] = np.nan
    
    mask = np.array(res_freq_predictions) >= 1000
    
    plt.plot(time_values[mask], res_freq_predictions[mask], label=f'Before_compression={before_compression:.2f}', color='blue', marker='o', markersize=5)
    
    plt.plot(time_values[mask], rolling_avg_filtered[mask], label=f'Smoothed (Before_compression={before_compression:.2f})', linewidth=2, color='red')

plt.xlabel('Time')
plt.ylabel('Res_Freq')
plt.title(f'Res_Freq vs. Time for a cell of size {size_cell_pred}μm (Random Forest)')
plt.legend()
plt.show(block=False) 

input("Press Enter to continue...")
plt.close('all')