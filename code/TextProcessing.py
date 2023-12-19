from AudioFile import AudioFile
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

class TextProcessing:
    def __init__(self):
        pass

    # Store word with its counts in dict 
    def count_word_frequencies(self, transcription):
        word_counts = {}
        words = transcription.lower().split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        return word_counts

    # use cosine and TF-IDF method to vectorize and compare the files and their words
    def calculate_similarity(self, transcriptions):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(transcriptions)
        cosine_sim = cosine_similarity(tfidf_matrix)
        return cosine_sim
    
    # heatmap generation. The darker the color (lower the number), the less similar. Note the 1s diagonal is comparison of file with itself.
    def generate_heatmap(self, similarity_matrix, labels):
        plt.figure(figsize=(12, 10))  # Increase the figure size (width, height)
        sns.heatmap(similarity_matrix, annot=True, xticklabels=labels, yticklabels=labels)
        plt.xticks(rotation=45)  # Adjust rotation if needed
        plt.yticks(rotation=45)

        plt.tight_layout()  # Adjust layout
        plt.subplots_adjust(bottom=0.2, left=0.2)  # Adjust margins if needed

        plt.savefig('../output_files/heatmap.png')
