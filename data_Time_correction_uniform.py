import pandas as pd
import numpy as np
import math

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\Weyrd\Documents\Github\Cells_characteristics_Mems_ai\data_\cleaned_data.csv")

# isolate df by sample
all_samples = []
for sample in df['Sample_number'].unique():
    all_samples.append(df[df['Sample_number'] == sample])

#len
previous_value = 0

max_time = 500

# Create a list to store rows for the new DataFrame
new_data = []
dic = {}
for sample in all_samples:
    number_of_rows = len(sample)
    if number_of_rows < 10:
        #skip sample
        continue

    print(f"Cell {sample['Sample_number'].unique()[0]}:number of rows {number_of_rows}")
    nb_update = math.ceil(max_time /number_of_rows)
    sample_number = sample['Sample_number'].unique()[0]

    # print(f"nb_update {nb_update}")
    for time in range(max_time):
        new_row = [time]
        # print(time)
        if time % nb_update == 0 or  time-1 % nb_update == 0:
            # print(f'update {time} sample {sample_number} time {time}')
            for column in sample.columns:
                if column == 'Time':
                    continue
                try:

                    current_time_percentage = math.ceil(number_of_rows * time / max_time)
                    if current_time_percentage == 0:
                        current_time_percentage = 1
                    
                    #take mean of previous 3 and next value 3
                    previous_values = []
                    next_values = []
                    for i in range(3):
                        previous_values.append(sample[column].iloc[current_time_percentage - i])
                        next_values.append(sample[column].iloc[current_time_percentage + i])
                    mean_previous = sum(previous_values) / len(previous_values)
                    mean_next = sum(next_values) / len(next_values)
                    mean_value = (mean_previous + mean_next) / 2


                    # previous_value = sample[column].iloc[current_time_percentage - 1]
                    # current_value = sample[column].iloc[current_time_percentage]
                    # mean_value = (previous_value + current_value) / 2
                    # # print(f"mean value {mean_value} ")
                    new_row.append(mean_value)
                
                except Exception as e:
                    # print(f"error {e} on sample {sample_number} time {time} column {column}")
                    pass
        else:
            try:
                old_row = new_data[-1]
                # copy all except time
                for i in range(1, len(old_row)):
                    new_row.append(old_row[i])

             
            except Exception as e:
                pass



        new_data.append(new_row)
    dic[str(f"Sample_{str(sample_number)}")] = new_data

# Create a new DataFrame from the list of rows
new_df = pd.DataFrame(new_data, columns=df.columns)





new_df.to_csv(r"C:\Users\Weyrd\Documents\Github\Cells_characteristics_Mems_ai\data_\cleaned_data2.csv", index=False)





































# import pandas as pd
# import numpy as np

# # Read the data from the CSV file
# df = pd.read_csv(r"C:\Users\Weyrd\Documents\Github\Cells_characteristics_Mems_ai\data_\cleaned_data2.csv")

# # Target correlation value (0.8)
# target_corr = 0.8

# # Set the initial scaling factor and tolerance level
# scaling_factor = 1.0
# tolerance = 0.01  # Adjust this tolerance level as needed

# # Maximum number of iterations to avoid infinite loop
# max_iterations = 100

# for _ in range(max_iterations):
#     # Calculate the current correlation between Res_Freq and Amplitude
#     current_corr = df['Res_Freq'].corr(df['Amplitude'])

#     # Check if the correlation is within the tolerance
#     if abs(current_corr - target_corr) < tolerance:
#         break

#     # Calculate the scaling factor to achieve the target correlation
#     scaling_factor = target_corr / current_corr

#     # Check if the scaling factor is too large or too small
#     if not np.isfinite(scaling_factor) or abs(scaling_factor) > 1e6:
#         print("Scaling factor is too large. Target correlation may not be achievable.")
#         break

#     # Apply the scaling factor to the Amplitude column
#     df['Amplitude'] *= scaling_factor

# # Save the final data to a new CSV file
# df.to_csv(r"C:\Users\Weyrd\Documents\Github\Cells_characteristics_Mems_ai\data_\correlated_data.csv", index=False)

# # Check the final correlation between Res_Freq and Amplitude
# final_corr = df['Res_Freq'].corr(df['Amplitude'])
# print("Final correlation:", final_corr)
