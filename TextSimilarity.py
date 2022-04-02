from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class TextSimilarity():
    def get_similarity_score(self,file1,file2):
        similarity_vector = self.get_similarity_vector(file1,file2)
        similarity_score = similarity_vector[0][1]
        return similarity_score

    def get_similarity_vector(self,file1,file2):
        wordfreq_dataFrame = self.get_wordfreq_dataFrame(file1,file2)
        similarity_vector = cosine_similarity(wordfreq_dataFrame, wordfreq_dataFrame)
        return similarity_vector

    def get_wordfreq_dataFrame(self,file1,file2):
        count_vectorizer = CountVectorizer(stop_words="english")
        count_vectorizer = CountVectorizer()

        files_text_array = [file1.get_text(),file2.get_text()]
        document_term_sparseMatrix = count_vectorizer.fit_transform(files_text_array)
        document_term_denseMatrix = document_term_sparseMatrix.todense()

        words_in_allText = count_vectorizer.get_feature_names_out()
        wordfreq_dataFrame = pd.DataFrame(document_term_denseMatrix,columns=words_in_allText,index=[file1.get_name(),file2.get_name()])
        return wordfreq_dataFrame