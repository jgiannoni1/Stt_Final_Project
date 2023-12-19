from AudioFile import AudioFile
from TextProcessing import TextProcessing
import queue
import os
import csv

class FileProcessing:
    def __init__(self, file_list):
        self.file_list = file_list
        self.text_processor = TextProcessing()

    # Queue is used so that we can upload multiple files at once
    def process_files(self):
        q = queue.Queue()
        for file_path in self.file_list:
            audio_file = AudioFile(file_path)
            audio_file.load_audio()
            audio_file.get_metadata()
            q.put(audio_file)
        
        # Get file names to be used in heat map
        file_names = [os.path.basename(file_path) for file_path in self.file_list]

        # csv output
        transcriptions = []
        with open('../output_files/metadata_output.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['File', 'Metadata', 'Transcription', 'Word Counts'])

            # just getting files the order in which they are listed 
            while not q.empty():
                audio_file = q.get()
                audio_file.transcribe_audio()
                transcriptions.append(audio_file.transcription)

                # Prepare data for CSV
                metadata_str = ', '.join([f'{key}: {value}' for key, value in audio_file.metadata.items()])
                word_counts_str = ', '.join([f'{word}: {count}' for word, count in self.text_processor.count_word_frequencies(audio_file.transcription).items()])
                
                # Write to CSV
                writer.writerow([audio_file.address, metadata_str, audio_file.transcription, word_counts_str])

        # Similarity analysis and heatmap generation
        similarity_matrix = self.text_processor.calculate_similarity(transcriptions)
        self.text_processor.generate_heatmap(similarity_matrix, file_names)
