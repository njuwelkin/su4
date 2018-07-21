import numpy as np
from scipy import sparse 

import os, sys

assert(len(sys.argv) == 3)
in_path = sys.argv[1]
out_path = sys.argv[2]

utils_path = os.path.dirname(os.path.abspath(__file__)) + "/../utils"
sys.path.append(utils_path)
import sparse_matrix

# mat: N * M
#coo = sparse_matrix.load_sparse_csr("./output/w_c.npy.npz")
coo = sparse_matrix.load_sparse_csr(in_path)
mat = coo.toarray()

# ww: N * N
ww = coo.dot(coo.T).toarray()
#np.save('./output/ww_tmp.npy', ww)

# v2: N * 1
v2 = np.sqrt((mat**2).sum(axis = 1)+0.0001)

for i in range(len(v2)):
    ww[i] /= v2[i]

for j in range(len(v2)):
    ww[:, j] /= v2[j]

tmp = 1-np.eye(ww.shape[0])
ww *= tmp


#np.save('./output/w_w.npy', ww)
coo = sparse.csr_matrix(ww)
#sparse_matrix.save_sparse_csr('./output/w_w.npy', coo)
sparse_matrix.save_sparse_csr(out_path, coo)
