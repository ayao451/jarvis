class FileNameGenerator:
    def __init__(self):
        self.counter = 0

    def generate_file_name(self):
        self.counter += 1
        return f"output_{self.counter}.wav"