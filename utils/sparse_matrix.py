import numpy as np
from scipy import sparse

def save_sparse_csr(filename, array):
    np.savez(filename, data = array.data, indices=array.indices, indptr =array.indptr, shape=array.shape)

def load_sparse_csr(npzfilename):
    loader = np.load(npzfilename)
    return sparse.csr_matrix((  loader['data'], loader['indices'], loader['indptr']),shape = loader['shape'])

if __name__ == '__main__':
    a = np.arange(12).reshape((3, 4))
    coo = sparse.csr_matrix(a)
    save_sparse_csr('tmp.npy', coo)
    coo2 = load_sparse_csr('tmp.npy.npz')
    print(coo2.toarray())
