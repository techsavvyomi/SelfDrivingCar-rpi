import cv2
import mediapipe as mp
from gtts import gTTS
import os
import playsound
import threading
import serial
import pygame
from pygame.locals import *

width = 640
height = 480

# Initialize Pygame
pygame.init()
pygame.display.set_mode((250, 250))
#ser=serial.Serial('/dev/cu.HC-05-DevB',9600)
# Initialize the video capture object
cam = cv2.VideoCapture(0)

# Set the resolution of the video capture
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Initialize FaceMesh from Mediapipe
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

count = 0
closed = False
global sound_playing
sound_playing = False
sound_lock = threading.Lock()


# Function to play the sound
def play_sound():
    global sound_playing
    with sound_lock:
        sound_playing = True

    # Load the audio file
    pygame.mixer.music.load('sleep.mp3')

    # Play the audio file
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    with sound_lock:
        sound_playing = False


# Main loop
while True:
    # Check for Pygame events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            key_input = pygame.key.get_pressed()

            # complex orders
            if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                print("Forward Right")
                #ser.write(b'6')

            elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                print("Forward Left")
                #ser.write(b'7')

            elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                print("Reverse Right")
                #ser.write(b'8')

            elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                print("Reverse Left")
                #ser.write(b'9')

            # simple orders
            elif key_input[pygame.K_UP]:
                print("Forward")
                #ser.write(b'1')

            elif key_input[pygame.K_DOWN]:
                print("Reverse")
                #ser.write(b'2')

            elif key_input[pygame.K_RIGHT]:
                print("Right")
                #ser.write(b'3')

            elif key_input[pygame.K_LEFT]:
                print("Left")
                #ser.write(b'4')

            elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                print("exit")
                #ser.write(b'0')
                #ser.close()
                break
        elif event.type == pygame.KEYUP:
            print("stop")
            #ser.write(b'0')

    # Capture a frame from the camera
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with FaceMesh
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        right = [landmarks[374], landmarks[386]]
        for landmark in right:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
            # print(right[1].y)
        # cv2.putText(frame,"Active",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),5,cv2.LINE_AA)

        if (right[0].y - right[1].y) < 0.004 and (left[0].y - left[1].y) < 0.004:
            count += 1
            if count >= 15:
                closed = True
                #ser.write(b'0')
                cv2.putText(frame, "Sleep", (70, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0),5, cv2.LINE_AA)
                # Generate voice text
                with sound_lock:
                    if not sound_playing:
                        sound_thread = threading.Thread(target=play_sound)
                        sound_thread.start()
        else:
            count = 0
            closed = False

            # Print duration of eye closure if closed
        if closed:
            cv2.putText(frame, f"Closure: {count}", (70, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 5, cv2.LINE_AA)
        '''''
        if count > 20:
            with sound_lock:
                if not sound_playing:
                    # Create a new thread to play sound
                    sound_thread = threading.Thread(target=play_sound)
                    sound_thread.start()
        '''
    cv2.imshow('Sleep detection camera', frame)
    cv2.waitKey(1)
