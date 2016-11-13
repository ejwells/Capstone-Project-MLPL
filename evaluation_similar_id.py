# -*- coding: utf-8 -*-

import get_patent_info_google as gg
from gensim import models


def similar_inclusion (document, model):
    """
    compute the percentage of inclusion on similar ids in the most similar
    documents of the model
    input: document id in the model, doc2vec model
    output: score of inclusion
    """
    gg_similar_ids=gg.get_Similar_Id(document)
    model_similar_ids=model.most_similar(positive=[document], negative=[], topn=len(gg_similar_ids), clip_start=0, clip_end=None, indexer=None)
    score=0.0    
    for id in gg_similar_ids:
        if id in model_similar_ids:
            score+=1
    return score/len(gg_similar_ids)
    

def score (document,model):
    """
    get a document from the doc2vec file, fetch the similar documents from
    google patent and return the scores of those documents.
    input: document id in the model, doc2vec model
    output: list of scores of similar document to the input document in the model
    """
    similar_ids=gg.get_Similar_Id(document)
    result={}
    for id in similar_ids:
        distance=model.similarity(document,id)
        result[id]=distance
    return result