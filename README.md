
Pi Camera calibration:

Set up your Raspberry Pi with the Pi Camera module attached.
To enable the Raspberry Pi camera module, you can follow these steps:
Connect the camera module to the Raspberry Pi using the camera ribbon cable. The camera module connector is located between the HDMI and audio ports on the Raspberry Pi board.
Boot up your Raspberry Pi and log in to the terminal.
Type the following command to open the Raspberry Pi configuration tool:
sudo raspi-config  
Use the arrow keys to navigate to Interfacing Options and press Enter.
Navigate to Camera and press Enter.
Select Yes to enable the camera module.
Press Enter to confirm and then select Finish to exit the configuration tool.
Reboot your Raspberry Pi by typing the following command:
sudo reboot
Once your Raspberry Pi has rebooted, you can test the camera module by typing the following command in the terminal:
raspistill -o test.jpg
This command will take a still image using the camera module and save it as test.jpg in your home directory.
If the camera module is working properly, you should see a preview of the image on your screen before it is saved. If you encounter any issues, make sure the camera module is properly connected and try again.

Print a chessboard pattern,  use this pattern only. (https://raw.githubusercontent.com/opencv/opencv/4.x/doc/pattern.png ) 
Mount the chessboard in various orientations and distances from the camera, making sure that it is visible in the camera frame.
Take several images of the chessboard from different angles and distances using the Pi Camera module, and save them in a folder named "chess_board".
Open the terminal on your Raspberry Pi and navigate to the directory where the "picam_calibration.py" script is located.
Run the "picam_calibration.py" script by typing "python picam_calibration.py" in the terminal and press enter.
Follow the prompts in the script to input the path to the folder containing your chessboard images, the number of rows and columns in your chessboard pattern, and the size of each square in millimeters.
The script will then use the OpenCV library to detect the corners of the chessboard in each image, and use this data to compute the camera matrix and distortion coefficients.
The camera matrix and distortion coefficients will be printed to the terminal once the calibration process is complete. Copy these parameters (Ay,V0,U0) as they will be used in the "rc_driver.py" script.
Update the "rc_driver.py" script with the camera matrix and distortion coefficients that you obtained from the calibration process.
Save the changes to the "rc_driver.py" script and run it to see the effect of the camera calibration on your Pi Camera module.


Collecting training Data:

Connect your Raspberry Pi to your RC car and make sure that it is powered on.
Navigate to the directory where you have saved the file "collect_training_data.py" and replace
sp = "/dev/tty.usbmodem1421" by sp = “COM__” which is found while connecting Bluetooth module.

Make sure Host IP address is correct here: h, p = "192.168.1.100", 8000 (check your server computer IP address, it’s your host IP Address).
Run the "collect_training_data.py" file in computer using pycharm.
This will start the program that collects training data from your RC car.
Open a terminal window on your Raspberry Pi.
Navigate to the directory where you have saved the file " stream_client.py "
Make sure Host IP address is correct here: client_socket.connect(('192.168.1.100', 8000))
Run the "stream_client.py " file by typing the following command in the new terminal window: python stream_client.py.
Make same changes in the ultrasonic_client.py file.
This will start the program that streams the video feed from your RC car to your Raspberry Pi.
Use the arrow keys on your keyboard to drive the RC car. Press "q" to exit.
The frames will only be saved when there is a key press action.
Once you exit the program, the data will be saved into a newly created "training_data" folder in the same directory.

Neural network training:

To train the model run model_training.py script, this contains the code for training a neural network model.
After training, model will be saved into newly created folder named as saved_model.

Self-driving in action:
Navigate to the directory in server computer where you have saved the file "rc_driver.py " 
Make sure Host IP address is correct here: h, p = "192.168.1.100", 8000
First run rc_driver.py to start the server on the computer.
For simplified no object detection version, run rc_driver_nn_only.py.
Navigate to the directory where you have saved the file " rc_driver_nn_only.py" and replace
sp = "/dev/tty.usbmodem1421" by sp = “COM__” which is found while connecting Bluetooth module.

Make sure Host IP address is correct here: h, p = "192.168.1.100", 8000
Now we have to run both stream_client.py and ultrasonic_client.py on raspberry pi simultaneously.
For that first run ultrasonic_client.py using terminal, then run stream_client.py using terminal.
Car will start driving in self-driving mode now.
To stop the car Press "q" on the computer and exit.
