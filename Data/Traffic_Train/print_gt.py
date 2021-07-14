from scipy.io import loadmat
annots = loadmat('subway.mat', squeeze_me=True)['gt']

print(annots)
print(annots.shape)