"""
LASA Handwriting Dataset, version 2.0\n
See https://bitbucket.org/khansari/lasahandwritingdataset/src/master/Readme.txt

This module provides classes to load and interact with the LASA Handwriting Dataset in Python3.

References:
S. M. Khansari-Zadeh and A. Billard, "Learning Stable Non-Linear Dynamical
    Systems with Gaussian Mixture Models", IEEE Transaction on Robotics, 2011.
"""
# src/pyLASAHandwritingDataset/__init__.py

from pyLASAHandwritingDataset.dataset import (
    DataSet,
    LASADemonstration,
    LASAMotionPattern,
    is_handwriting_motion,
)
from pyLASAHandwritingDataset.motions import (
    ALL_HANDWRITING_MOTIONS,
    ALL_MULTI_MODEL_MOTIONS,
    ALL_SINGLE_PATTERN_MOTIONS,
    HandwritingMotion,
    MultiModelMotion,
    SinglePatternMotion,
)

__version__ = "0.1.2"
__all__ = [
    "__version__",
    #
    "DataSet",
    "LASADemonstration",
    "LASAMotionPattern",
    "is_handwriting_motion",
    #
    "ALL_HANDWRITING_MOTIONS",
    "ALL_MULTI_MODEL_MOTIONS",
    "ALL_SINGLE_PATTERN_MOTIONS",
    "HandwritingMotion",
    "MultiModelMotion",
    "SinglePatternMotion",
]
