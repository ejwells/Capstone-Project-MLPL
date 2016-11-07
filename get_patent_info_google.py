# -*- coding: utf-8 -*-

from lxml import html
import requests

def get_Similar_Id(id):
    '''
    Fetch the patent number of the similar documents of google patent
    input: String Patent_id
    output: patent_id array
    '''
    page = requests.get('https://patents.google.com/patent/%s/en' % (id))
    tree = html.fromstring(page.content)
    similarIds=tree.xpath('//tr[@itemprop="similarDocuments"]//span[@itemprop="publicationNumber"]/text()')
    return similarIds
    
def get_patent_citation(id):
    '''
    Fetch the patent number of patents cited in this patent
    input: String Patent_id
    output: patent_id array
    '''
    page = requests.get('https://patents.google.com/patent/%s/en' % (id))
    tree = html.fromstring(page.content)
    citations=tree.xpath('//tr[@itemprop="backwardReferences"]//span[@itemprop="publicationNumber"]/text()')
    return citations
    
def get_patent_cited_by(id):
    '''
    Fetch the patent number of patents citing this patent
    input: String Patent_id
    output: patent_id array
    '''
    page = requests.get('https://patents.google.com/patent/%s/en' % (id))
    tree = html.fromstring(page.content)
    citations=tree.xpath('//tr[@itemprop="forwardReferences"]//span[@itemprop="publicationNumber"]/text()')
    return citations
    
    
def get_classification(id):
    '''
    Fetch the classification of the patent on google patent
    input: String Patent_id
    output: classification id array
    '''
    page = requests.get('https://patents.google.com/patent/%s/en' % (id))
    tree = html.fromstring(page.content)
    classification_id=tree.xpath('//ul[@itemprop="cpcs"]//span[@itemprop="Code"]/text()')
    classification_description=tree.xpath('//ul[@itemprop="cpcs"]//span[@itemprop="Description"]/text()')
    result={}
    for i in range(0,len(classification_id)):
        result[classification_id[i]]=classification_description[i]
    return result
    

def get_body_tab(id):
    '''
    Fetch the body of the patent
    input: patet id
    output: array of txt CAREFUL it needs to be encode in utf-8
    '''
    page = requests.get('https://patents.google.com/patent/%s/en' % (id))
    tree = html.fromstring(page.content)
    body=tree.xpath('//section[@itemprop="description"]//div[@itemprop="content"]//p/text()')
    return body

def get_body(id):
    '''fetch the body, encode it and return a string
    input: id
    output: string
    '''
    body=get_body_tab(id)
    string=''
    for elt in body:
        string=elt.encode('utf-8')+'\n'
    return string

    
    
def get_body_length(id):
    '''
    Fetch the body of the patent and return its length
    input: the patent id
    output: int nb of words in the body
    '''
    body=get_body_tab(id)
    res=0
    skipped=0
    taken=0
    for elt in body:
        try:
            res+=len(elt.encode('utf-8').split(' '))
            taken+=1
        except ValueError:
            skipped+=1
            pass
    if(taken==0):
        return res
    return res*(1+skipped/taken)
    
def get_claims_tab(id):
    '''
    Fetch the claims of the patent
    input: patet id
    output: array of txt CAREFUL it needs to be encode in utf-8
    '''
    page = requests.get('https://patents.google.com/patent/%s/en' % (id))
    tree = html.fromstring(page.content)
    claims=tree.xpath('//section[@itemprop="claims"]//div[@class="claim-text"]/text()')
    return claims

def get_claims(id):
    '''fetch the claims, encode it and return a string
    input: id
    output: string
    '''
    claims=get_claims_tab(id)
    string=''
    for elt in claims:
        string=elt.encode('utf-8')+'\n'
    return string


def get_claims_length(id):
    '''
    get how many words there are in the claims of a patent
    input: patent_id
    output: int
    '''
    claims=get_claims_tab(id)
    res=0
    skipped=0
    taken=0
    for elt in claims:
        try:
            res+=len(elt.encode('utf-8').split(' '))
            taken+=1
        except ValueError:
            skipped+=1
            pass
    if(taken==0):
        return res
    return res*(1+skipped/taken)

