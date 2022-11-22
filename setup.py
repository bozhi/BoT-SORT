#!/usr/bin/env python

import setuptools
import torch

torch_ver = [int(x) for x in torch.__version__.split(".")[:2]]
assert torch_ver >= [1, 3], "Requires PyTorch >= 1.3"


setuptools.setup(
    name="Botsort",
    version="0.1.6",
    python_requires=">=3.6",
    packages=["tracker", "tracker.tracking_utils", "fast_reid"],
    package_dir={
        "tracker": "tracker",
        "tracker.tracking_utils": "tracker/tracking_utils",
        "fast_reid": "fast_reid",
    }
)
