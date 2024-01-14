# # Open the file
# with open('usgs_data.txt', 'r') as file:
    # # Read the lines of the file
    # lines = file.readlines()

    # # Loop through each line in the file
    # for line in lines:
        # # Check if the line contains the description
        # if "Precipitation, total, inches (Sum), [Operational]" in line:
            # # Split the line into columns
            # columns = line.split()

            # # Extract and combine TS, parameter, and statistics values
            # ts_parameter_statistics = f"{columns[1]}_{columns[2]}_{columns[3]}"
            
            # # Print the combined value
            # print("TS_parameter_statistics: ", ts_parameter_statistics)
            # break


# import pandas as pd

# # Open the file
# with open('usgs_data.txt', 'r') as file:
    # # Read the lines of the file
    # lines = file.readlines()

    # # Loop through each line in the file
    # for line in lines:
        # # Check if the line contains the description
        # if "Precipitation, total, inches (Sum), [Operational]" in line:
            # # Split the line into columns
            # columns = line.split()

            # # Extract and combine TS, parameter, and statistics values
            # ts_parameter_statistics = f"{columns[1]}_{columns[2]}_{columns[3]}"
            
            # # Print the combined value
            # print("TS_parameter_statistics:", ts_parameter_statistics)

            # # Now, use the identified value to extract data from the dataframe
            # data_path = "usgs_data.txt"
            # param_desc = ts_parameter_statistics

            # # Read the data from the file
            # data = pd.read_csv(data_path, sep='\t', comment='#', skiprows=30)
            
            # # Identify the column that contains the data for the specified parameter description
            # for col in data.columns:
                # if param_desc in col:
                    # # Print the data from the identified column
                    # print(data[col])
                    # break
            # else:
                # print("No data found for the specified parameter description.")
            # break


import pandas as pd

def extract_usgs_data(data_path, param_desc):
    # Open the file
    with open(data_path, 'r') as file:
        # Read the lines of the file
        lines = file.readlines()

        # Initialize skiprows and data_start variables
        skiprows = 0
        data_start = False

        # Loop through each line in the file
        for line in lines:
            skiprows += 1
            # Check if the line contains the description
            if param_desc in line:
                # Split the line into columns
                columns = line.split()

                # Extract and combine TS, parameter, and statistics values
                ts_parameter_statistics = f"{columns[1]}_{columns[2]}_{columns[3]}"

                # Now, use the identified value to extract data from the dataframe
                # Read the data from the file
                data = pd.read_csv(data_path, sep='\t', comment='#', skiprows=skiprows)

                # Identify the column that contains the data for the specified parameter description
                for col in data.columns:
                    if ts_parameter_statistics in col:
                        # Return the data from the identified column
                        return data[col]
                else:
                    print("No data found for the specified parameter description.")
                break
            elif data_start:
                # Skip the line immediately after the column name line
                data_start = False
                skiprows += 1
            elif "TS   parameter     statistic     Description" in line:
                # Mark the start of data
                data_start = True

data_path = "usgs_data.txt"
param_desc = "Precipitation, total, inches (Sum), [Operational]"

data = extract_usgs_data(data_path, param_desc)

print(data)

