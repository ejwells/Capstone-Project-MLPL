#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:57:58 2016

@author: jiandiwei
"""
import get_patent_info_google as gg

def citation_cited_similarDoc_evaluate(output,patent_id):
    '''
    compare  the similar document, citation and cited patent from google with resulte of doc2vec
    
    
    input:  Patent_id, the output list of tupe from doc2vec 
            for example: 
                
            patent_id='7716768'
                
            output=[('7716897', 0.5852824449539185),
              ('9161524', 0.5318326950073242),
              ('7717122', 0.5268031358718872),
              ('7721391', 0.5242995023727417),
              ('7716835', 0.5070189833641052),
              ('7717017', 0.4986177086830139),
              ('4899482', 0.49395477771759033),]
    
    
    output: print out the fraction  (citation found by doc2vec) / (number of citation) 
                                    (cited patent found by doc2vec)/(number of cited patent)
                                    (simialr document found by doc2vec)/ (number of similar document)
    '''                  
    
    output_id=['US'+i for (i,j) in output]      # get the patent id from list of tupe
    patent_id=str(patent_id)                    # make sure it is a sting 
    us_patent='US'+patent_id                     # add prefix US to patent_id 
    
    
    gg_citation_id=gg.get_patent_citation(us_patent)    # get citation , cited patent and similar doc from google 
    gg_cited_id=gg.get_patent_cited_by(us_patent)
    gg_similar=gg.get_Similar_Id(us_patent)
    
    copy_citation=list(gg_citation_id)                  # make a copy of list before loop itself 
    copy_cited=list(gg_cited_id)
    copy_similar=list(gg_similar)
    
    gg_citation_compare=[i[0:9] for i in copy_citation]   # get rid of 'US' prefix to do comparasion 
    gg_cited_compare=[i[0:9] for i in copy_cited]
    gg_similar_compare=[i[0:9] for i in copy_similar]
    
    citation_counter=0                                  # set the counter and calculate the fraction 
    cited_counter=0
    similar_counter=0
    
    for patent in gg_citation_compare:
        if patent in output_id:
            citation_counter+=1
    for patent in gg_cited_compare:
        if patent in output_id:
            cited_counter+=1
    for patent in gg_similar_compare :
        if patent in output_id:
            similar_counter+=1
            
            
            
    print  str(citation_counter)+'/'+str(len(gg_citation_compare))+' citation patent id has been found in the doc2vec output of patent '+patent_id
    print  str(cited_counter)+'/'+str(len(gg_cited_compare))+' citated patent id has been found in the doc2vec output of patent '+patent_id
    print  str(similar_counter)+'/'+str(len(gg_similar_compare))+' similar documents id has been found in the doc2vec output of patent '+patent_id
    
    return None 

