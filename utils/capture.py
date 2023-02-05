import cv2
import numpy as np
from PIL import ImageGrab


class ScreenCapture(object):

    def __init__(self, region, fps, filename) -> None:
        self.region = region
        self.width =  self.region[2] - self.region[0]
        self.height =  self.region[3] - self.region[1]
        self.filename = filename
        self.fps = fps
        self.stop_record = False
        self.images = []

    def start(self, play_btn):
        print("Screen capture turned on")
        
        while 'pause' in play_btn.get_attribute('class'):
            self.images.append(ImageGrab.grab(bbox=self.region))

        print("Screen capture turned off\nSaving video...")
        self.stop_record = True
        video_path = self.filename
        if '.mp4' not in video_path:
            video_path += ".mp4"
        fourcc = cv2.VideoWriter_fourcc(*"MP4V")
        video_writer = cv2.VideoWriter(
            video_path, 
            fourcc, 
            self.fps, 
            (self.width, self.height)
        )

        for img in self.images:
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            video_writer.write(frame)
            
        video_writer.release()
        print("Video saved :", video_path)
