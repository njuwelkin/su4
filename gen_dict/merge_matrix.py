import numpy as np
from scipy import sparse
import sys
import os

utils_path = os.path.dirname(os.path.abspath(__file__)) + "/../utils"
sys.path.append(utils_path)
import sparse_matrix

MATRIX_W1 = 0.3
MATRIX_W2 = 0.4
MATRIX_W3 = 1.0 - MATRIX_W1 - MATRIX_W2

ww1 = sparse_matrix.load_sparse_csr("./output/w_w1.npy.npz").toarray()
ww2 = sparse_matrix.load_sparse_csr("./output/w_w2.npy.npz").toarray()
ww3 = sparse_matrix.load_sparse_csr("./output/w_w3.npy.npz").toarray()

print(ww1.shape)
print(ww2.shape)
assert(ww1.shape == ww2.shape == ww3.shape)

ww = MATRIX_W1* ww1 + MATRIX_W2* ww2 + MATRIX_W3* ww3
coo = sparse.csr_matrix(ww)
sparse_matrix.save_sparse_csr("./output/w_w.npy", coo)
