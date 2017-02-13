
import get_patent_info_google as gg

def evaluation_citation(root,ranked_list):
    '''Take the root return each of those associated with their rank in the ranked list
    input: root of the tree, ranked list of the most similar patents to that root
    output: list of tuples patent no, rank
    '''
    citations=gg.get_patent_citation(root)
    output=[]
    for patent in citations:
        try:
            idx=ranked_list.index(patent)
            output.append([patent,idx])
        except:
            output.append([patent,-1])
    return output
