# Graded Assignment on Python

## Q1: Create a Python script to check the password strength. 

●       Implement a Python function called check_password_strength that takes a password string as input.

●       The function should check the password against the following criteria:

      ○       Minimum length: The password should be at least 8 characters long.
      ○       Contains both uppercase and lowercase letters.
      ○       Contains at least one digit (0-9).
      ○       Contains at least one special character (e.g., !, @, #, $, %).

●       The function should return a boolean value indicating whether the password meets the criteria.

●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

●       Provide appropriate feedback to the user based on the strength of the password.  

[Solution](Python/GradedAssign1/check_password_strength.py)

## Q2: Write a Python program to monitor the health of the CPU. 

Few pointers to be noted:

●       The program should continuously monitor the CPU usage of the local machine.

●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.

●       The program should run indefinitely until interrupted.

●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.

### Hint:

●       The psutil library in Python can be used to retrieve system information, including CPU usage. You can install it using pip install psutil.

●       Use the psutil.cpu_percent() method to get the current CPU usage as a percentage.

      Expected Output:

      Monitoring CPU usage...
      Alert! CPU usage exceeds threshold: 85%
      Alert! CPU usage exceeds threshold: 90%
      ... (continues until interrupted) 

[Solution](Python/GradedAssign1/check_cpu_health.py)

## Q4:  Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.

●       The script should copy all files from the source directory to the destination directory.

●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.

●       Handle errors gracefully, such as when the source directory or destination directory does not exist.

Sample Command:

      python backup.py /path/to/source /path/to/destination
      
By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.

[Solution](Python/GradedAssign1/file_backup.py)

