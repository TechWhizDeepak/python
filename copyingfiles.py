import os
import shutil
import datetime

# Set the path to the folder

Source_files = 'F:\Python_Playstation\source'
Destination = 'F:\Python_Playstation\destination'

# Use the os.listdir() function to get a list of filenames in the folder
filenames = os.listdir(Source_files)

# Iterate through the list of filenames
for filename in filenames:
  # Construct the full path to the file
    file_path = os.path.join(Source_files, filename)
  
  # Get the modification time of the file in seconds since the epoch
    mod_time = os.path.getmtime(file_path)
  
  # Convert the modification time to a human-readable date using the datetime module
    from datetime import datetime
    mod_time_dt = datetime.fromtimestamp(mod_time)
    last_modified_date = mod_time_dt.fromtimestamp(mod_time).year
  
  # Print the filename and last modified date
  #print(filename, last_modified_date)

    if last_modified_date > 2021 :
            # Copy the file to the destination directory
        #print(filename, last_modified_date)
        #shutil.copy2(file_path, Destination)

        # Move the file to the destination directory
        shutil.move(file_path, Destination)