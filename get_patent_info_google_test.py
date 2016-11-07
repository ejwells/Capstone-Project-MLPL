# -*- coding: utf-8 -*-

import get_patent_info_google
id='US8111141'
'''
out=open('similar_id.txt','w')
result=get_patent_info_google.get_Similar_Id(id)
for elt in result:
    out.write('%s\n'%(elt))
out.close()

out=open('classification_id.txt','w')
result=get_patent_info_google.get_classification(id)
for elt in result:
    out.write('%s %s\n'%(elt,result[elt]))
out.close() 

out=open('body.txt','w')
body=get_patent_info_google.get_body_top(id)
for elt in body:
    out.write('%s\n'%(elt))
body=get_patent_info_google.get_body_bot(id)
for elt in body:
    out.write('%s\n'%(elt))
out.close

inp=open('body.txt','r')
cpt=0
for line in inp:
    cpt+=len(line.split())
print cpt

print get_patent_info_google.get_body_length(id)


cpt=0
tot=0
inputfile=open('input_bodycount.txt','r')
for line in inputfile:
    line=line.strip()
    cpt+=get_body_length(line)
    tot+=1
print cpt/tot

cpt=0
tot=0
inputfile=open('input_bodycount.txt','r')
for line in inputfile:
    if(tot%10==0):
        print tot
    line=line.strip()
    cpt+=get_claims_length(line)
    tot+=1
print cpt/tot

'''

out=open('citation.txt','w')
result=get_patent_info_google.get_patent_citation(id)
for elt in result:
    out.write('%s\n'%(elt))
out.close()

out=open('cited_by.txt','w')
result=get_patent_info_google.get_patent_cited_by(id)
for elt in result:
    out.write('%s\n'%(elt))
out.close()