import unittest
import torch
from geometry_numeric import safe_cosine
from language_vector_geometry import relation_features

class NumericGeometryTests(unittest.TestCase):
 def test_orthogonal(self):
  c,v=safe_cosine(torch.tensor([[1.,0.]]),torch.tensor([[0.,1.]]))
  self.assertAlmostEqual(c.item(),0.);self.assertTrue(v.item())
 def test_parallel_and_antiparallel(self):
  for sign in (-1.,1.):
   c,v=safe_cosine(torch.tensor([[1e-40,0.]],dtype=torch.float64),torch.tensor([[sign*1e-40,0.]],dtype=torch.float64))
   self.assertAlmostEqual(c.item(),sign);self.assertTrue(v.item())
 def test_zero_undefined(self):
  c,v=safe_cosine(torch.tensor([[0.,0.]]),torch.tensor([[1.,0.]]))
  self.assertEqual(c.item(),0.);self.assertFalse(v.item())
 def test_scale_invariance(self):
  a=torch.tensor([[3.,4.]],dtype=torch.float64);b=torch.tensor([[5.,-2.]],dtype=torch.float64)
  x,_=safe_cosine(a,b)
  for scale in (1e-200,1e200):
   y,_=safe_cosine(a*scale,b*scale)
   self.assertTrue(torch.allclose(x,y,atol=1e-14))
 def test_bad_input(self):
  with self.assertRaises(ValueError):safe_cosine(torch.tensor([[float('nan')]]),torch.tensor([[1.]]))
  with self.assertRaises(ValueError):safe_cosine(torch.tensor([[1.]]),torch.tensor([[1.,2.]]))
 def test_relation_features(self):
  f=relation_features(torch.tensor([[1e-30,0.]],dtype=torch.float64),torch.tensor([[1e-30,0.]],dtype=torch.float64))
  self.assertEqual(f['cosine'].item(),1.)
  self.assertTrue(f['cosine_valid'].item())

class PreviousRegressionTests(unittest.TestCase):
 def test_huge_equal_lengths(self):
  a=torch.tensor([[1e200,0.]],dtype=torch.float64)
  f=relation_features(a,a)
  self.assertTrue(torch.isfinite(f['relative_length']).all())
  self.assertEqual(f['relative_length'].item(),0.)
 def test_tiny_direction(self):
  from language_vector_geometry import direction,project_role
  a=torch.tensor([[1e-200,0.]],dtype=torch.float64)
  self.assertTrue(torch.allclose(direction(a),torch.tensor([[1.,0.]],dtype=torch.float64)))
  self.assertTrue(torch.allclose(project_role(torch.tensor([[3.,4.]],dtype=torch.float64),a),torch.tensor([[3.,0.]],dtype=torch.float64)))
 def test_unequal_large_lengths(self):
  a=torch.tensor([[1e200,0.]],dtype=torch.float64)
  b=torch.tensor([[5e199,0.]],dtype=torch.float64)
  self.assertAlmostEqual(relation_features(a,b)['relative_length'].item(),1/3)

if __name__=='__main__':unittest.main()
