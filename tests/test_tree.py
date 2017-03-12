import unittest
import sys
import os
from Tree import Tree
import numpy as np
# add source directory to path
sys.path.append(os.path.abspath('..'))


class TestEvaluation(unittest.TestCase):
    def setUp(self):
        self.t = Tree([8111141], 'all_patent_nums_in_db.txt')
        self.root = 8111141
        self.similarIds = np.array([7511604, 7733218, 7030731])
        self.cited_by = np.array([9042914])
        self.citation = np.array([6940392, 7248883, 7751957])
        self.docs = [self.similarIds, self.citation, self.cited_by]
        self.branch = np.array([self.root])
        self.branch = np.append(self.branch, self.similarIds)
        self.branch = np.append(self.branch, self.citation)
        self.branch = np.append(self.branch, self.cited_by)

    def test_add_patent_from_string(self):
        tree_copy = self.t.copy()
        tree_copy._add_patent_from_string('US6838918A')
        exp_result = np.array([self.root, 6838918])
        result = np.copy(tree_copy.tree)
        np.testing.assert_array_almost_equal(result, exp_result)

    def test_get_branch(self):
        tree_copy = self.t.copy()
        tree_copy.get_branch(self.root)
        result = np.copy(tree_copy.tree)
        np.testing.assert_array_almost_equal(result, self.branch)

    def test_add_doc(self):
        tree_copy = self.t.copy()
        tree_copy.get_branch(self.root, True)
        for i in range(3):
            exp_result = self.docs[i]
            result = tree_copy.docs[i][self.root]
            np.testing.assert_array_almost_equal(exp_result, result)

    def test_build_tree(self):
        self.t.build_tree(20)
        print self.t.tree
        self.t.txt_output()
