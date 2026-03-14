# tests/test_1.py

from pyLASAHandwritingDataset import DataSet

data = DataSet.GShape  # Auto-downloads on first access
print(data)
print(data.demos[0].pos.shape)

print(DataSet.shapes())
