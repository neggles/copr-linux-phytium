#!/usr/bin/env python3
from pathlib import Path

script_dir = Path(__file__).parent
patches_dir = script_dir

source_base = 6000
patch_base = 6000

# get patch file list
patch_files = [x for x in sorted(patches_dir.iterdir(), key=lambda x: x.stem) if x.suffix == ".patch" and x.stem.startswith("0")]
print(f"# {len(patch_files)} Phytium kernel patches")
patch_paths = [x.relative_to(script_dir) for x in patch_files]

# print the Source lines
for idx, ppath in enumerate(patch_paths):
    print(f"Patch{patch_base + idx:04d}: {ppath}")

print("Done.")
