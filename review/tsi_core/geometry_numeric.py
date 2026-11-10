"""Numerically stable, scale-independent cosine for finite vector inputs."""
import torch


def safe_cosine(left, right):
    if left.shape != right.shape or left.ndim < 1 or left.shape[-1] == 0:
        raise ValueError('Vectors must have equal nonempty final dimensions')
    if not torch.is_floating_point(left) or not torch.is_floating_point(right):
        raise TypeError('Floating point vectors required')
    if not torch.isfinite(left).all() or not torch.isfinite(right).all():
        raise ValueError('Nonfinite vector')
    la = left.abs().amax(dim=-1, keepdim=True)
    ra = right.abs().amax(dim=-1, keepdim=True)
    valid = (la > 0) & (ra > 0)
    lu = left / torch.where(la > 0, la, torch.ones_like(la))
    ru = right / torch.where(ra > 0, ra, torch.ones_like(ra))
    lu = lu / torch.linalg.vector_norm(lu, dim=-1, keepdim=True).clamp_min(torch.finfo(left.dtype).tiny)
    ru = ru / torch.linalg.vector_norm(ru, dim=-1, keepdim=True).clamp_min(torch.finfo(right.dtype).tiny)
    cosine = (lu * ru).sum(dim=-1, keepdim=True).clamp(-1., 1.)
    return torch.where(valid, cosine, torch.zeros_like(cosine)), valid
