from tkinter import *
from frame_filters import *
from Real_Time_Face_Detection import Real_Time_Face_Detection
from record_video import record_video
from image_face_detection import image_face_detection

root = Tk()
root.title("Real Time Face Detection and Real Time Image Filters")

title = Label(root, text="Please Select a Filter to apply!        (PRESS 'Q' TO EXIT SELECTED FILTER)", fg="red")
title.grid(row=0, column=0, columnspan=4)

space = Label(root, text="                  ")
space.grid(row=1, column=0)

sepia_button = Button(root, text="Sepia Filter", padx=30, pady=10, command=lambda : apply_sepia_filter(intensity=0.6))
color_overlay_button = Button(root, text="Color Overlay Filter", padx=30, pady=10,command=lambda :apply_color_overlay(intensity=0.7,red=200,green=155,blue=34) )
hue_sat_button = Button(root, text="Hue Saturation Filter", padx=30, pady=10,command=apply_hue_saturation)
Threshold_button = Button(root, text="Threshold Mode", padx=30, pady=10,command=apply_threshold_mode)
Invert_button = Button(root, text="Invert Mode", padx=30, pady=10,command=apply_invert)
Blur_mask_button = Button(root, text="Circle Focus Blur Filter", padx=30, pady=10,command=lambda :apply_circle_focus_blur_filter(intensity=0.4))
Portrait_button = Button(root, text="Portrait Mode", padx=30, pady=10,command=apply_portrait_mode)
Real_Time_Face_Detection_Button = Button(root, text="Real Time Face Detection",padx=30 , pady=10,command=Real_Time_Face_Detection)
Record_video_button = Button(root, text="Record Video",padx=30 , pady=10,command=record_video)
Image_face_detection_button = Button(root, text="Image Face Detection",padx=30 , pady=10,command=image_face_detection)

space = Label(root, text="                  ")
space.grid(row=1, column=0)

sepia_button.grid(row=2, column=0)
color_overlay_button.grid(row=2, column=1)
hue_sat_button.grid(row=2, column=2)
Portrait_button.grid(row=2, column=3)


space_2 = Label(root, text="                  ")
space_2.grid(row=3, column=0)

Invert_button.grid(row=4, column=0)
Threshold_button.grid(row=4, column=1)
Blur_mask_button.grid(row=4, column=2)
Real_Time_Face_Detection_Button.grid(row=4 , column=3)

space_3 = Label(root, text="                  ")
space_3.grid(row=5, column=0)

Record_video_button.grid(row=6, column=0)
Image_face_detection_button.grid(row=6, column=1)
root.mainloop()