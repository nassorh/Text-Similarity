from File import *
from TextSimilarity import *

if __name__ == "__main__":
    doc1 = File("doc1","doc1.txt")
    doc2 = File("doc2","doc2.txt")
    ts = TextSimilarity()
    similarity_score = ts.get_similarity_score(doc1,doc2)
    print("Similiary between {} and {} is {}".format(doc1.get_name(),doc2.get_name(),similarity_score))