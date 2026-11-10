"""Language-only geometric features. No word dictionary, operator/truth/answer decoder."""
import torch
from geometry_numeric import safe_cosine

def finite(v):
 if not torch.isfinite(v).all():raise ValueError('Nonfinite language vector')
 return v

def length(v):
 v=finite(v)
 scale=v.abs().amax(dim=-1,keepdim=True)
 normalized=v/torch.where(scale>0,scale,torch.ones_like(scale))
 return scale*torch.linalg.vector_norm(normalized,dim=-1,keepdim=True)

def direction(v,eps=1e-6):
 v=finite(v)
 scale=v.abs().amax(dim=-1,keepdim=True)
 unit=v/torch.where(scale>0,scale,torch.ones_like(scale))
 norm=torch.linalg.vector_norm(unit,dim=-1,keepdim=True)
 return unit/torch.where(norm>0,norm,torch.ones_like(norm))

def scale_degree(v,degree):
 degree=torch.as_tensor(degree,dtype=v.dtype,device=v.device)
 if not torch.isfinite(degree).all() or (degree<0).any():raise ValueError('Degree must be finite nonnegative')
 while degree.ndim<v.ndim:degree=degree.unsqueeze(-1)
 return finite(v)*degree

def relation_features(left,right,eps=1e-6):
 if left.shape!=right.shape:raise ValueError('Language vectors must have same shape')
 l=length(left);r=length(right)
 cosine,valid=safe_cosine(left,right)
 # Compute the signed relative difference without overflowing l+r.
 max_length=torch.maximum(l,r)
 scaled_l=l/torch.where(max_length>0,max_length,torch.ones_like(max_length))
 scaled_r=r/torch.where(max_length>0,max_length,torch.ones_like(max_length))
 relative=(scaled_l-scaled_r)/(scaled_l+scaled_r).clamp_min(torch.finfo(l.dtype).tiny)
 return dict(left_length=l,right_length=r,relative_length=relative,
             cosine=cosine,
             cosine_valid=valid,
             difference=finite(left)-finite(right),midpoint=(finite(left)+finite(right))/2)

def project_role(v,role_direction,eps=1e-6):
 axis=direction(role_direction,eps)
 return finite(v).mul(axis).sum(-1,keepdim=True)*axis

def learned_transform(v,matrix,bias=None):
 out=finite(v)@finite(matrix).transpose(-1,-2)
 return finite(out if bias is None else out+finite(bias))
