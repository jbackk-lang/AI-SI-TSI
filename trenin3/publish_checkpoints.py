#!/usr/bin/env python3
"""Synchronize trenin3 checkpoints to GitHub every five optimizer steps.
Requires: git, authenticated git push, local repository clone.
Run from the local clone; do not place credentials in this script.
"""
import argparse, os, shutil, subprocess
from pathlib import Path

def run(*args, cwd):
    subprocess.run(args, cwd=cwd, check=True)

def publish(step, checkpoint_dir, repo):
    if step % 5:
        return
    repo=Path(repo).resolve()
    dest=repo/"trenin3"/"checkpoints"
    dest.mkdir(parents=True, exist_ok=True)
    src=Path(checkpoint_dir)
    for name in ("latest.pt", "latest.json", f"step-{step:05d}.pt"):
        source=src/name
        if not source.is_file():
            raise FileNotFoundError(source)
        temp=dest/(name+".tmp")
        shutil.copy2(source,temp)
        os.replace(temp,dest/name)
    run("git","add","trenin3/checkpoints",cwd=repo)
    run("git","commit","-m",f"trenin3: checkpoint step {step}",cwd=repo)
    run("git","push",cwd=repo)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--step",type=int,required=True)
    p.add_argument("--checkpoints",required=True)
    p.add_argument("--repo",required=True)
    a=p.parse_args()
    publish(a.step,a.checkpoints,a.repo)
