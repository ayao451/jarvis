from pynput import keyboard
from input_processing.record_audio.recorder import Recorder

class listener(keyboard.Listener):
    def __init__(self, recorder):
        super().__init__(on_press = self.on_press)
        self.recorder = recorder
    
    def on_press(self, key):
        if key is None: #unknown event
            pass
        elif isinstance(key, keyboard.Key): #special key event
            if key.ctrl:
                if not self.recorder.recording:
                    self.recorder.start_recording()
                else:
                    self.recorder.stop_recording()
                    return False

class Recording:
    def __init__(self, file_name):
        self.r = Recorder("./input_processing/record_audio/recordings/" + file_name)
        self.l = listener(self.r)

    def start(self):
        print('press ctrl to record')
        self.l.start() #keyboard listener is a thread so we start it here
        self.l.join() #wait for the tread to terminate so the program doesn't instantly close

                