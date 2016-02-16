from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# Documentation: http://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
# http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

def fit_tSNE(X, n_components=2):
	model = TSNE(n_components=n_components, n_iter=100000)
	return model.fit_transform(X) 

def fit_PCA(X, n_components=2):
	model = PCA(n_components=n_components)
	return model.fit_transform(X) 