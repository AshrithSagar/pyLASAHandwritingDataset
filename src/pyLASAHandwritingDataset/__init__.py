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
)
from pyLASAHandwritingDataset.motions import (
    ALL_HANDWRITING_MOTIONS,
    ALL_MULTI_MODEL_MOTIONS,
    ALL_SINGLE_PATTERN_MOTIONS,
    HandwritingMotion,
    MultiModelMotion,
    SinglePatternMotion,
    is_handwriting_motion,
    is_multi_model_motion,
    is_single_pattern_motion,
)

__version__ = "0.2.0"
__all__ = [
    "__version__",
    #
    "DataSet",
    "LASADemonstration",
    "LASAMotionPattern",
    #
    "ALL_HANDWRITING_MOTIONS",
    "ALL_MULTI_MODEL_MOTIONS",
    "ALL_SINGLE_PATTERN_MOTIONS",
    "HandwritingMotion",
    "MultiModelMotion",
    "SinglePatternMotion",
    "is_handwriting_motion",
    "is_multi_model_motion",
    "is_single_pattern_motion",
]
