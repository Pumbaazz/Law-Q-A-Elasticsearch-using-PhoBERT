import time
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from pyvi.ViTokenizer import tokenize
from model import Model

def load_es():
    model_embedding = SentenceTransformer(
        'VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')
    client = Elasticsearch()
    return model_embedding, client


def search(query):

    def embed_text(text):
        text_embedding = model_embedding.encode(text)
        return text_embedding.tolist()

    model_embedding, client = load_es()
    time_embed = time.time()
    query_vector = embed_text([tokenize(query)])[0]
    print(len(query_vector))
    print('TIME EMBEDDING ', time.time() - time_embed)
    script_query = {
        "script_score": {
            "query": {
                "match_all": {}
            },
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'title_vector') + 1.0",
                "params": {"query_vector": query_vector}
            }
        }
    }



    response = client.search(
        index='demo_simcsejson',
        body={
            "size": 10,
            "query": script_query,
            "_source": {
                "includes": ["id", "question", "answer"]
            },
        },
        ignore=[400]
    )

    # Get 10 result by elasticsearch with model 'VoVanPhuc/sup-SimCSE-VietNamese-phobert-base'
    resultelastics = []
    for hit in response["hits"]["hits"]:
        resultelastics.append([hit["_source"]['question'],
                      hit["_source"]['answer']])

    id_rs = 0
    result= []
    # Sort 2nd with self model
    resultbyselfmodels = sortbyselfmodel(query,resultelastics)
    for resultbyselfmodel in resultbyselfmodels:
        id_rs+=1
        #resultbyselfmodel[1] is Question
        #resultbyselfmodel[1] is Answer
        result.append([id_rs, resultbyselfmodel[1], resultbyselfmodel[2]])
    return result

def sortbyselfmodel(query, inputs):
    # Mota vao day cho dep 
    model = Model('./PhoBERT_Trained/Model')
    euclideans = [] # List of euclideans for each sentence
    resulttmp = []  # List of euclideans and sentence
    arrsort= []     # List of euclideans and sentence with sorted
    for input in inputs:
        # Get Distance 
        cosine, manhattan, euclidean = model.measure_distance((query, input[0]))
        euclideans= [euclidean, input[0], input[1]]
        resulttmp.append(euclideans)
    #Sorted
    arrsort = sorted(resulttmp, key = lambda x: x[0])
    return arrsort

