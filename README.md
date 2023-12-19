# README for STT Final Project

## Overview
This Project is designed to handle speech-to-text (STT) processing and text analysis in Python. Some data structures used include: dictionary (hash map), queue, and list. As a disclaimer, I should say that this will differ quite a bit from my proposal as I began with the intent to do the project in C++... I struggled with that, especially with getting API calls setup (tried 3 different STT products), and so I ended up switching to Python since whisper is just too easy to use.  

- Executing the main file takes all of the audio files from the audio folder and: 
    - Transcribes them using whisper
    - Extracts metadata using pydub
    - Stores word counts in a dictionary
        - Outputs all of that into a csv file so that the data associated with each audio file can be seen.
        - Outputs a heatmap as a png to show the similarities between the files in a matrix.

## Getting Started
- Python versions supported: 3.8 up to but not including 3.12.
- pip install `openai-whisper` and `pydub`. Whisper is the STT model I ended up going with because it doesn't require working with tokens, curl, or anything like that. Pydub is what's being used for the metadata extraction.
- Make sure you also have things like matplotlib, seaborn, ffmpeg, and sklearn installed. They were already available to me through VScode in JupyterHub. 
- Run main.py from within the code folder to generate the csv and png files into the output_files folder. I used the "tiny" whisper model which is the least accurate, but quickest. It took a little over 2min for my machine to complete the process. A big factor here is obviously the file sizes, so the audio examples I used in the audio folder are very short.
    - If for some reason you're having trouble with whisper, try deleting the 'fp16=false' from the `transcribe_audio()` in `AudioFile.py`. Also, in general, their documentation was really easy to understand: https://github.com/openai/whisper 

## Project Structure
- `Stt_Final_Project`: Root directory of the project.
  - `code`: Contains all the Python script files.
    - `AudioFile.py`
    - `TextProcessing.py`
    - `FileProcessing.py`
    - `main.py`
  - `audio`: Directory for storing audio files.
  - `output_files`: Directory for storing output files like transcriptions, metadata, and analysis results.

## File Description
### `AudioFile.py`
Handles audio file loading and processing.
- `AudioFile` class:
  - Initialization with the audio file's address.
  - Loading the audio file and extracting metadata.
  - Transcribing the audio using the Whisper model.
  
### `TextProcessing.py`
Handles text processing and analysis.
- `TextProcessing` class:
  - `count_word_frequencies`: Counts frequency of each word in the transcription.
  - `calculate_similarity`: Computes TF-IDF and cosine similarity between transcriptions.
  - `generate_heatmap`: Generates a heatmap from the similarity matrix.

### `FileProcessing.py`
Manages file processing workflow.
- `FileProcessing` class:
  - Initialization with a list of audio file paths.
  - Processes each file: metadata extraction, transcription, word count, and similarity analysis.
  - Outputs results to CSV files and generates heatmaps.

### `main.py`
The main script to run the project.
- Collects audio files from the `audio` folder.
- Initializes `FileProcessing` with the collected audio file paths.
- Executes the processing of files.