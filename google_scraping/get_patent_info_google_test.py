# -*- coding: utf-8 -*-

import get_patent_info_google
id='US2437382A'

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