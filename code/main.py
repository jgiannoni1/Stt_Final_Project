import glob
from FileProcessing import FileProcessing

if __name__ == '__main__':
    audio_folder_path = '../audio/*'
    import glob

    # covers a wide range of audio file types 
    file_list = glob.glob('../audio/*.wav') + \
                glob.glob('../audio/*.mp3') + \
                glob.glob('../audio/*.aac') + \
                glob.glob('../audio/*.flac') + \
                glob.glob('../audio/*.ogg') + \
                glob.glob('../audio/*.m4a') + \
                glob.glob('../audio/*.wma') + \
                glob.glob('../audio/*.opus') + \
                glob.glob('../audio/*.amr') + \
                glob.glob('../audio/*.aiff') + \
                glob.glob('../audio/*.aif')

    processor = FileProcessing(file_list)
    processor.process_files()
