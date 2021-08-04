# model.py
# Get distance of 2 vector

import numpy as np
from typing import Tuple
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import pairwise_distances
from sentence_transformers import SentenceTransformer

class Model(object):
  def __init__(self, model_path):
    super(Model, self).__init__()
    self.sbert = SentenceTransformer(model_path)

  def measure_distance(self, sents: Tuple[str, str]):
    # compute embeddings
    corpus_embeddings = self.sbert.encode(sents)
    # compute distance
    distances = (
        pairwise_distances(
        corpus_embeddings[0].reshape(1, -1),
        corpus_embeddings[1].reshape(1, -1),
        metric)[0][0] for metric in ["cosine", "manhattan", "euclidean"]
        )
    return distances
