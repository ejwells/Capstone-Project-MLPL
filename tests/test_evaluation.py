import unittest
import sys, os
# add source directory to path
sys.path.append( os.path.abspath( '..' ))
import evaluation
import numpy as np

class TestEvaluation( unittest.TestCase ):

    def test_input_evaluation(self):
        root=8111141
        ranked_list=[5170172, 5631642, 5977913, 6542114, 6720888, 6765484, 6940392, 7248883, 7751957, 2007027]
        str_list=[str(root)]
        self.assertRaises(TypeError,evaluation.evaluation_citation,str(root),ranked_list)
        self.assertRaises(TypeError,evaluation.evaluation_citation,root,str_list)
        self.assertRaises(ValueError,evaluation.evaluation_citation,1,ranked_list)
        self.assertRaises(ValueError,evaluation.evaluation_citation,root,[1])

    def test_patent_absent(self):
        root=8111141
        ranked_list=[8111141]
        true_res=[5170172, 5631642, 5977913, 6542114, 6720888, 6765484, 6940392, 7248883, 7751957, 2007027]
        exp_result=[]
        for elt in true_res:
            exp_result.append((elt,-1))
        a=np.array(evaluation.evaluation_citation(root,ranked_list))
        b=np.array(exp_result)
        np.testing.assert_array_almost_equal(a, b, decimal=6)
        pass

    def test_evaluation(self):
        root=8111141
        ranked_list=[5170172, 5631642, 5977913, 6542114, 6720888, 6765484, 6940392, 7248883, 7751957, 2007027]
        exp_result=[]
        for elt in ranked_list:
            exp_result.append((elt,ranked_list.index(elt)))
        a=np.array(evaluation.evaluation_citation(root,ranked_list))
        b=np.array(exp_result)
        np.testing.assert_array_almost_equal(a, b, decimal=6)
