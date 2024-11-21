import pyaudio
import wave

class Recorder:
    def __init__(self, file_name):
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.data_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 1
        self.rate = 44100  # Record at 44100 samples per second
        self.filename = file_name
        self.p = pyaudio.PyAudio()  # Create an interface to PortAudio
        self.stream = None
        self.frames = None
        self.recording = False

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.wf = wave.open(self.filename, 'wb')
            self.wf.setnchannels(self.channels)
            self.wf.setsampwidth(self.p.get_sample_size(self.data_format))
            self.wf.setframerate(self.rate)

            def callback(in_data, frame_count, time_info, status):
                    #file write should be able to keep up with audio data stream (about 1378 Kbps)
                    self.wf.writeframes(in_data) 
                    return (in_data, pyaudio.paContinue)
                
            self.stream = self.p.open(format = self.data_format,
                                    channels = self.channels,
                                    rate = self.rate,
                                    input = True,
                                    stream_callback = callback)
            self.stream.start_stream()
            self.recording = True
            print('Recording')

    
    def stop_recording(self):
        if self.recording:         
            self.stream.stop_stream()
            self.stream.close()
            self.wf.close()
            
            self.recording = False
            print('Recording Finished')


