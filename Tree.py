import numpy as np
import get_patent_info_google as gg
from lxml import html
import requests


class Tree(object):
    """docstring for Tree."""
    def __init__(self, root_list, all_patents_text_file=None,):
        self.all_patents = []
        if not (all_patents_text_file is None):
            patents = open(all_patents_text_file, 'r')
            content = patents.readlines()
            for line in content:
                self.all_patents.append(int(line))
            patents.close()
        self.all_patents = np.array(self.all_patents)

        self.root_list = root_list

        self.tree = np.array(root_list)

        self.similarIds_root = {}
        self.citation_root = {}
        self.cited_by_root = {}
        self.docs = [self.similarIds_root, self.citation_root,
                     self.cited_by_root]

        self.to_proc = []

    def get_branch(self, root, is_root=False):
        '''
        return the next branch for the tree ONLY US PAT
        input: patent number int
        output: list
        '''
        address = 'https://patents.google.com/patent/US%s/en' % (root)
        page = requests.get(address)
        tree = html.fromstring(page.content)
        similar_id = tree.xpath('//tr[@itemprop="similarDocuments"]//span[@' +
                                'itemprop="publicationNumber"]/text()')
        citation = tree.xpath('//tr[@itemprop="backwardReferences"]//span[@' +
                              'itemprop="publicationNumber"]/text()')
        cited_by = tree.xpath('//tr[@itemprop="forwardReferences"]//span[@' +
                              'itemprop="publicationNumber"]/text()')
        tab = [similar_id, citation, cited_by]
        for l in tab:
            for string in l:
                self._add_patent_from_string(string)
        if is_root:
            for i in range(3):
                self.docs[i][root] = np.array([])
                for string in tab[i]:
                    self._add_doc(string, root, i)

    def _add_doc(self, string, root, i):
        if(string[0:2] == 'US' and len(string) <= 11):
            try:
                pat_n = int(string[2:9])
                if pat_n in self.all_patents:
                    self.docs[i][root] = np.append(self.docs[i][root], pat_n)
            except ValueError:
                pass

    def _add_patent_from_string(self, string):
        if(string[0:2] == 'US' and len(string) <= 11):
            try:
                pat_n = int(string[2:9])
                if pat_n in self.all_patents and not (pat_n in self.tree):
                    self.tree = np.append(self.tree, pat_n)
                    self.to_proc.append(pat_n)
            except ValueError:
                pass

    def copy(self):
        result = Tree(self.root_list)
        result.tree = np.copy(self.tree)
        result.all_patents = np.copy(self.all_patents)
        return result

    def build_tree(self, size):
        total_size = size*len(root_list)
        for root in self.root_list:
            self.get_branch(root, True)
        while(len(self.tree) < total_size and len(self.to_proc) > 0):
            root = self.to_proc[0]
            self.to_proc = self.to_proc[1:]
            self.get_branch(root)

    def txt_output(self):
        outputs = ['tree_similarIds.txt', 'tree_citations.txt',
                   'tree_cited_by.txt', 'tree_Trees.txt']
        for i in range(4):
            out = open(outputs[i], 'w')
            if i < 3:
                string = ''
                for key in self.docs[i]:
                    string += '%s,' % (key)
                    for pat_n in self.docs[i][key]:
                        string += '%s,' % (str(int(pat_n)))
                    string = string[:-1] + '\n'
                out.write(string)
                out.close()
            else:
                string = ''
                for pat_n in self.tree:
                    string += '%s\n' % (pat_n)
                out.write(string)
                out.close
