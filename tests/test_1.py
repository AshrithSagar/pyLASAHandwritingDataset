# tests/test_1.py

import pyLASAHandwritingDataset as lasa

print(lasa.DataSet)

data = lasa.DataSet["GShape"]  # Auto-downloads (all shapes) on first access
print(data)
print(data.demos[0].pos.shape)

print(lasa.DataSet.handwriting_motions())
