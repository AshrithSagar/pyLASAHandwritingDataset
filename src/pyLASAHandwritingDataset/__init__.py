"""
LASA Handwriting Dataset
"""
# src/pyLASAHandwritingDataset/__init__.py

from pyLASAHandwritingDataset.dataset import DataSet, Demo, Pattern, ShapeName
from pyLASAHandwritingDataset.shapes import ALL_SHAPES

__version__ = "0.1.0"
__all__ = [
    "__version__",
    "DataSet",
    "Pattern",
    "Demo",
    "ShapeName",
    "ALL_SHAPES",
]
