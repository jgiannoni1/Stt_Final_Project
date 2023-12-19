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
- pip install 'openai-whisper' and 'pydub'. Whisper is the STT model I ended up going with because it doesn't require working with tokens, curl, or anything like that. Pydub is what's being used for the metadata extraction.
- Make sure you also have things like matplotlib, seaborn, and sklearn installed. They were already available to me through VScode in JupyterHub. 
- Run main.py from within the code folder to generate the csv and png files into the output_files folder. I used the "tiny" whisper model which is the least accurate, but quickest. It took a little over 2min for my machine to complete the process. A big factor here is obviously the file sizes, so the audio examples I used in the audio folder are very short.
    - If for some reason you're having trouble with whisper, try deleting the 'fp16=false' from the 'transcribe_audio()' in 'AudioFile.py'. Also, in general, their documentation was really easy to understand: https://github.com/openai/whisper 

## Project Structure
- `Stt_Final_Project`: Root directory of the project.
  - `code`: Contains all the Python script files.
    - `AudioFile.py`
    - `TextProcessing.py`
    - `FileProcessing.py`
    - `main.py`
  - `audio`: Directory for storing audio files.
  - `output_files`: Directory for storing output files like transcriptions, metadata, and analysis results.

## Dependencies
- `pydub`: To handle audio file operations.
- `whisper`: For audio transcription.
- `sklearn`: For text analysis (TF-IDF and cosine similarity).
- `matplotlib` and `seaborn`: For generating heatmaps of similarity analysis.

## Scripts Description
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

## Running the Project
1. Ensure all dependencies are installed.
2. Place audio files in the `audio` folder.
3. Run `main.py` from the `code` directory.
4. Check the `output_files` folder for results.

## Output
- Transcribed text, metadata, and word counts are saved in `metadata_output.csv`.
- Heatmaps representing the similarity between audio file transcriptions are saved as images in the `output_files` directory.