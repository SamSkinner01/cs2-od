import keyboard
import threading
import os
import time
from PIL import ImageGrab

class ScreenGrabber:
    def __init__(self, seconds, start_key="i", quit_key="o"):
        self.seconds = seconds
        self.start_key = start_key
        self.quit_key = quit_key
        self.recording = False
        self.create_folder()

    def start(self):
        print(f"Press '{self.start_key}' to start recording screenshots")
        keyboard.on_press_key(self.start_key, self.start_recording)
        keyboard.on_press_key(self.quit_key, self.stop_recording)
        keyboard.wait(self.quit_key)

    def start_recording(self, event):
        if not self.recording:
            print("Recording screenshots...")
            self.recording = True
            self.start_threads()

    def stop_recording(self, event):
        if self.recording:
            print("Quitting...")
            self.recording = False
            os._exit(0)

    def start_threads(self):
        threading.Thread(target=self.record_screenshots).start()

    def record_screenshots(self):
        count = 0
        while self.recording:
            start_time = time.time()
            screenshot = ImageGrab.grab()
            screenshot.save(f"{self.output_folder}/screenshot_{count}.png")
            count += 1
            elapsed_time = time.time() - start_time
            sleep_time = max(0, self.seconds - elapsed_time)
            time.sleep(sleep_time)

    def create_folder(self):
        name = "1"
        while os.path.exists(name):
            name = str(int(name) + 1)
        os.makedirs(name)
        self.output_folder = name

recorder = ScreenGrabber(seconds=0.2)
recorder.start()