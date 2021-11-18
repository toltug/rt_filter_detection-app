import os
import cv2
def record_video():
    # As an extention we can use .mp4 or .avi
    filename = 'video.mp4'
    frames_per_seconds = 24.0
    my_res = '720p'

    # We can set the resolution for the video capture entering width and height. As default, we use 3 for width and 4 for height.
    def change_res(cap, width, height):
        cap.set(3, width)
        cap.set(4, height)

    # A dictionary containing width and height values for the standart resolutions. We use this file to get the right sizes for given resolution value.
    res_sizes =  {
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }

    # We use this function to get the width and height. 
    # When called; if the entered resolution is in the res_sizes file, it will resize the output video.
    def get_sizes(cap, res='480p'):
        width, height = res_sizes['480p']
        if res in res_sizes:
            width, height = res_sizes[res]
        change_res(cap, width, height)
        return width, height


    # These are 2 different video file types and the video codec(XVID). XVID video codec works well with windows and with the file types .avi and .mp4
    VIDEO_TYPE = {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    }

    # We use this function to get the vide extention name from the filename we entered. If the extention is different from mp4 or avi, function will set it as avi as default.
    def get_video_type(filename):
        filename, ext = os.path.splitext(filename)
        if ext in VIDEO_TYPE:
            return  VIDEO_TYPE[ext]
        return VIDEO_TYPE['avi']



    cap = cv2.VideoCapture(0)
    # We get the sizes by calling the get_sizes function and entering our prefferred resolution to resize the default.
    sizes = get_sizes(cap, res=my_res)
    # We will get the video type to use it in .VideoWriter() method. 
    video_type_cv2 = get_video_type(filename)
    # We define our save path for the output video
    save_path = os.path.join('C:/', filename)

    # This is the output file containing our video with the given save path, video extention, fps value and size.
    output = cv2.VideoWriter(save_path, video_type_cv2, frames_per_seconds, sizes)

    while(True):
        # We use a infinite while loop to get all the frames until we hit exit.
        ret, frame = cap.read()
        # Here we are saving every frame into the output file until we break the loop
        output.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(10) & 0xFF == ord('e'):  
            break

    # After we break the loop, we release the capture
    cap.release()
    output.release()
    cv2.destroyAllWindows()