from pydub import AudioSegment
import whisper

class AudioFile:
    # constructor initialization
    def __init__(self, file_address):
        self.address = file_address
        self.metadata = {}
        self.audio = None
        self.word_counts = {}
        self.transcription = ''
        self.model = whisper.load_model("tiny") #smallest but quickest whisper model

    def load_audio(self):
        # Load the audio file
        self.audio = AudioSegment.from_file(self.address)

    def get_metadata(self):
        # Extract metadata
        self.metadata['frame rate (samples/second)'] = self.audio.frame_rate
        self.metadata['duration (seconds)'] = len(self.audio) / 1000.0  # Duration in seconds
        self.metadata['channels'] = self.audio.channels
        self.metadata['sample width (bits)'] = self.audio.sample_width * 8
        # Add more metadata extraction as needed


    def transcribe_audio(self):
        try:
            result = self.model.transcribe(self.address, fp16=False)
            self.transcription = result["text"]
        except Exception as e:
            print(f"An error occurred during transcription: {e}")
