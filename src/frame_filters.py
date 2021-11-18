import numpy as np
import cv2


def verify_alpha_channel(frame):
    try:
        frame.shape[3]  # Checking if the alpha channel exists
    except IndexError:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  # Adding the alpha channel
    return frame


def apply_hue_saturation():
    capture = cv2.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)
        s.fill(199)
        v.fill(255)
        hsv_image = cv2.merge([h, s, v])
        out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
        frame = verify_alpha_channel(frame)
        out = verify_alpha_channel(out)
        cv2.addWeighted(out, 0.25, frame, 1.0, .23, frame)
        cv2.imshow('Hue Saturation',frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def apply_color_overlay(intensity=0.5, blue=0, green=0, red=0):
    capture = cv2.VideoCapture(0)
    while (True):
       ret, frame = capture.read()
       frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
       frame = verify_alpha_channel(frame)
       frame_h, frame_w, frame_c = frame.shape
       sepia_bgra = (blue, green, red, 1)
       overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
       cv2.addWeighted(overlay, intensity, frame, 1.0, 0,frame)  # Blending the overlay and frame.
       cv2.imshow('Color Overlay', frame)
       if cv2.waitKey(10) & 0xFF == ord('q'):
           break
    capture.release()
    cv2.destroyAllWindows()


def apply_sepia_filter(intensity=0.6):
    capture = cv2.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        frame = verify_alpha_channel(frame)
        frame_h, frame_w, frame_c = frame.shape
        sepia_bgra = (30, 64, 108, 1) # Sepia color values
        overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
        cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)
        cv2.imshow('sepia', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()



def alpha_blend(frame_1, frame_2, mask):
    alpha = mask / 255.0
    blended = cv2.convertScaleAbs(frame_1 * (1 - alpha) + frame_2 * alpha)
    return blended

def apply_circle_focus_blur_filter(intensity=0.2):  # To make the center part not blurry, we use a circle mask and blend it with the fully blurred frame
    capture = cv2.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        frame = verify_alpha_channel(frame)
        frame_h, frame_w, frame_c = frame.shape  # frame height-frame width-frame channel
        y = int(frame_h / 2)
        x = int(frame_w / 2)
        mask = np.zeros((frame_h, frame_w, 4), dtype='uint8') 
        cv2.circle(mask, (x, y), int(y / 2), (255, 255, 255), -1, cv2.LINE_AA)  # (x, y) = center of the circle also called radius
        mask = cv2.GaussianBlur(mask, (21, 21), 11)
        blurred = cv2.GaussianBlur(frame, (21, 21), 11)
        blended = alpha_blend(frame, blurred, 255 - mask)
        frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)  # returning alpha channel to normal BGR channel as original
        cv2.imshow('Circle Focus Blur Filter',frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def apply_portrait_mode():
    capture = cv2.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
        blurred = cv2.GaussianBlur(frame, (21, 21), 11)
        blended = alpha_blend(frame, blurred, mask)
        frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
        cv2.imshow('Portrait Mode',frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()



def apply_threshold_mode():
    capture = cv2.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 120, 83, cv2.THRESH_BINARY)
        cv2.imshow('Threshold', mask)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()


def apply_invert():
   capture = cv2.VideoCapture(0)
   while (True):
     ret, frame = capture.read()
     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
     cv2.imshow('Invert Filter',cv2.bitwise_not(frame))
     if cv2.waitKey(10) & 0xFF == ord('q'):
        break
   capture.release()
   cv2.destroyAllWindows()
