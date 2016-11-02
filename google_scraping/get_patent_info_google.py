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