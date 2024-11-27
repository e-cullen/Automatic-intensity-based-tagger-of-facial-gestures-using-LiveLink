from datetime import datetime
import os
import pandas as pd

# Input your filename here
FILE = ' .csv'
OUTPUT_FILE = (f'Zeroed_Timestamps_{FILE}')

# Live Link updated their column names in 2023, this ensures all csv. files have interoperable 
# column names for processing multiple live Link csv. outputs
def rename_columns(df_data):
    df_data = df_data.rename({'Timecode': 'Timecode',
                              'BlendShapeCount': 'BlendshapeCount',
                              'EyeBlinkRight': 'eyeBlink_R',
                              'EyeLookDownRight': 'eyeLookDown_R',
                              'EyeLookInRight': 'eyeLookIn_R',
                              'EyeLookOutRight': 'eyeLookOut_R',
                              'EyeLookUpRight': 'eyeLookUp_R',
                              'EyeSquintRight': 'eyeSquint_R',
                              'EyeWideRight': 'eyeWide_R',
                              'EyeBlinkLeft': 'eyeBlink_L',
                              'EyeLookDownLeft': 'eyeLookDown_L',
                              'EyeLookInLeft': 'eyeLookIn_L',
                              'EyeLookOutLeft': 'eyeLookOut_L',
                              'EyeLookUpLeft': 'eyeLookUp_L',
                              'EyeSquintLeft': 'eyeSquint_L',
                              'EyeWideLeft': 'eyeWide_L',
                              'JawForward': 'jawForward',
                              'JawRight': 'jawRight',
                              'JawLeft': 'jawLeft',
                              'JawOpen': 'jawOpen',
                              'MouthClose': 'mouthClose',
                              'MouthFunnel': 'mouthFunnel',
                              'MouthPucker': 'mouthPucker',
                              'MouthRight': 'mouthRight',
                              'MouthLeft': 'mouthLeft',
                              'MouthSmileRight': 'mouthSmile_R',
                              'MouthSmileLeft': 'mouthSmile_L',
                              'MouthFrownRight': 'mouthFrown_R',
                              'MouthFrownLeft': 'mouthFrown_L',
                              'MouthDimpleRight': 'mouthDimple_R',
                              'MouthDimpleLeft': 'mouthDimple_L',
                              'MouthStretchRight': 'mouthStretch_R',
                              'MouthStretchLeft': 'mouthStretch_L',
                              'MouthRollLower': 'mouthRollLower',
                              'MouthRollUpper': 'mouthRollUpper',
                              'MouthShrugLower': 'mouthShrugLower',
                              'MouthShrugUpper': 'mouthShrugUpper',
                              'MouthPressRight': 'mouthPress_R',
                              'MouthPressLeft': 'mouthPress_L',
                              'MouthLowerDownRight': 'mouthLowerDown_R',
                              'MouthLowerDownLeft': 'mouthLowerDown_L',
                              'MouthUpperUpRight': 'mouthUpperUp_R',
                              'MouthUpperUpLeft': 'mouthUpperUp_L',
                              'BrowDownRight': 'browDown_R',
                              'BrowDownLeft': 'browDown_L',
                              'BrowInnerUp': 'browInnerUp',
                              'BrowOuterUpRight': 'browOuterUp_R',
                              'BrowOuterUpLeft': 'browOuterUp_L',
                              'CheekPuff': 'cheekPuff',
                              'CheekSquintRight': 'cheekSquint_R',
                              'CheekSquintLeft': 'cheekSquint_L',
                              'NoseSneerRight': 'noseSneer_R',
                              'NoseSneerLeft': 'noseSneer_L',
                              'TongueOut': 'tongueOut',
                              'HeadYaw': 'HeadYaw',
                              'HeadPitch': 'HeadPitch',
                              'HeadRoll': 'HeadRoll',
                              'LeftEyeYaw': 'LeftEyeYaw',
                              'LeftEyePitch': 'LeftEyePitch',
                              'LeftEyeRoll': 'LeftEyeRoll',
                              'RightEyeYaw': 'RightEyeYaw',
                              'RightEyePitch': 'RightEyePitch',
                              'RightEyeRoll': 'RightEyeRoll',
                              }, axis='columns')

    return df_data


def extract_time(string):
    # Get the hour, minute, second, and ms from the input string
    hour, minute, second, leftover = string.split(':')
    ms = leftover.split('.')[1]

    # Create a new string with the components we need
    datetime_str = f'{hour}:{minute}:{second}.{ms}'

    # Convert the new string to a datetime object
    output = datetime.strptime(datetime_str, '%H:%M:%S.%f')
    
    return output


def extract_frame(string):
    frame = int(string.split(':')[3].split('.')[0])
    return frame


def create_time_columns(df_data):
    # Create the Frames column
    df_data['Frame'] = df_data['Timecode'].apply(extract_frame)

    # Find the start time
    start_time = extract_time(df_data['Timecode'][0])

    # Create a list of timedeltas and convert them to strings
    time_elapsed = [str(extract_time(time)-start_time)[:-3] for time in df_data['Timecode']]

    # Fix a formating issue with the first element (by default millisecond zeroes are left off)
    time_elapsed[0] = '0:00:00.000'

    # Create a column to store the time elapsed since beginning
    df_data['Time Elapsed'] = time_elapsed

    # Split the time elapsed column into Hour, Minute, Second, Millisecond
    df_data[['Hour', 'Minute', 'Leftover']] = df_data['Time Elapsed'].str.split(':', expand=True)
    df_data[['Second', 'Millisecond']] = df_data['Leftover'].str.split('.', expand=True)
    df_data = df_data.drop('Leftover', axis='columns')
    
    return df_data


def reorder_columns(df_data):

    df_data = df_data[['Timecode','Time Elapsed', 'Hour', 'Minute', 'Second','Millisecond', 'Frame',
                       'BlendshapeCount','eyeBlink_R','eyeLookDown_R','eyeLookIn_R','eyeLookOut_R',
                       'eyeLookUp_R','eyeSquint_R','eyeWide_R','eyeBlink_L','eyeLookDown_L',
                       'eyeLookIn_L','eyeLookOut_L','eyeLookUp_L','eyeSquint_L','eyeWide_L',
                       'jawForward','jawRight','jawLeft','jawOpen','mouthClose','mouthFunnel',
                       'mouthPucker','mouthRight','mouthLeft','mouthSmile_R','mouthSmile_L',
                       'mouthFrown_R','mouthFrown_L','mouthDimple_R','mouthDimple_L',
                       'mouthStretch_R','mouthStretch_L','mouthRollLower','mouthRollUpper',
                       'mouthShrugLower','mouthShrugUpper','mouthPress_R','mouthPress_L',
                       'mouthLowerDown_R','mouthLowerDown_L','mouthUpperUp_R','mouthUpperUp_L',
                       'browDown_R','browDown_L','browInnerUp','browOuterUp_R','browOuterUp_L',
                       'cheekPuff','cheekSquint_R','cheekSquint_L','noseSneer_R','noseSneer_L',
                       'tongueOut','HeadYaw','HeadPitch','HeadRoll','LeftEyeYaw','LeftEyePitch',
                       'LeftEyeRoll','RightEyeYaw','RightEyePitch','RightEyeRoll']]
    return df_data

def convert_to_30_fps(df_data):

    # Get a list of all the row numbers, which are the start of a new set of frames (either 30 fps, or 60 fps)
    indexes = []
    for index, row in df_data.iterrows():
        if (row['Frame'] == 0) or (index == 0 and row['Frame'] != 0):
            indexes.append(index)

    # Use the list of row number to split the DataFrame into many DataFrame, each one stores information for 1 second
    dfs = []
    for i in range(0,len(indexes)-1):
        new_df = df_data[indexes[i]:indexes[i+1]]
        new_df = new_df.reset_index(drop=True)
        dfs.append(new_df)

    # Check the number of frame in each DataFrame and if there are 60, remove every other frame

    reduced_dfs = []
    for df in dfs:
        # If there are 60 frames (or 59 because of that edge-case) drop half the frames
        if len(df) == 60 or len(df) == 59:
            rows_to_drop = list(range(1,len(df),2))
            new_df = df.drop(rows_to_drop).reset_index(drop=True)
            new_df['Frame'] = list(range(len(new_df)))
            reduced_dfs.append(new_df)

        else:
            reduced_dfs.append(df)

    # Combine all the DataFrames back together
    df_final = pd.DataFrame()

    for df in reduced_dfs:
        df_final = pd.concat([df_final, df])

    # Reset the index one last time
    df_final = df_final.reset_index(drop=True)
    
    return df_final


def main():

        print(f'CONVERTING {FILE}')

        # Read in the data
        df_data = pd.read_csv(FILE)

        # Rename the columns (if necessary)
        df_data = rename_columns(df_data)
        
        # Add the hour, minute, second, and millisecond columns
        df_data = create_time_columns(df_data)

        # Reorder the columns
        df_data = reorder_columns(df_data)

        # Convert to 30 FPS
        df_data = convert_to_30_fps(df_data)

        # Save the updated file
        df_data.to_csv((OUTPUT_FILE), index=False)


if __name__ == '__main__':
    main()