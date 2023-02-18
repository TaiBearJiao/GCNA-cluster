from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics
from sklearn.cluster import KMeans
import sklearn.cluster as sc
from sklearn.mixture import GaussianMixture
import pandas as pd

def purity_score(y_true, y_pred):
    """Purity score
        Args:
            y_true(np.ndarray): n*1 matrix Ground truth labels
            y_pred(np.ndarray): n*1 matrix Predicted clusters

        Returns:
            float: Purity score
    """
    # matrix which will hold the majority-voted labels
    y_voted_labels = np.zeros(y_true.shape)
    # Ordering labels
    ## Labels might be missing e.g with set like 0,2 where 1 is missing
    ## First find the unique labels, then map the labels to an ordered set
    ## 0,2 should become 0,1
    labels = np.unique(y_true)
    ordered_labels = np.arange(labels.shape[0])
    for k in range(labels.shape[0]):
        y_true[y_true==labels[k]] = ordered_labels[k]
    # Update unique labels
    labels = np.unique(y_true)
    # We set the number of bins to be n_classes+2 so that
    # we count the actual occurence of classes between two consecutive bins
    # the bigger being excluded [bin_i, bin_i+1[
    bins = np.concatenate((labels, [np.max(labels)+1]), axis=0)

    for cluster in np.unique(y_pred):
        hist, _ = np.histogram(y_true[y_pred==cluster], bins=bins)
        # Find the most present label in the cluster
        winner = np.argmax(hist)
        y_voted_labels[y_pred==cluster] = winner

    return accuracy_score(y_true, y_voted_labels)


#True label
y_true = np.array([2,2,2,1,2,2,2,2,2,2,2,1,1,2,1,2,3,3,1,1,1,3,2,3,1,2,3,1,1,2,2,2,2,2,1,3,1,1,2,3,1,3,1,3,3,3,3,2,3,1,1,2,3,1,2,2,2,3,2,3,3,1,2,1,3,3])

#GCNA-Agglomerative
# 
# X2= np.loadtxt(r"Score1_8domianMAX_1_DAOSHU.txt",dtype=np.float64)
# model = AgglomerativeClustering(
#   affinity='precomputed',
#   n_clusters=3,
#   linkage='complete'
# ).fit(X2)

# y_pre=model.labels_
# print("GCNA-Agglomerative纯度为:",purity_score(y_true,y_pre))


#Baseline methods
data = np.loadtxt(r"finaldata2.txt",dtype=np.float64)
t_data = np.transpose(data)

kmeans = KMeans(n_clusters=3, random_state=1).fit(t_data)
y_pre = kmeans.labels_
print("kmeans纯度为:",purity_score(y_true,y_pre))

birch = sc.Birch(n_clusters=3).fit(t_data)
y_pre = birch.labels_
print("birch纯度为:",purity_score(y_true,y_pre))

scores = []
for i in range(100):
    gmm = GaussianMixture(n_components=3).fit_predict(t_data)
    score = purity_score(y_true,gmm)
    scores.append(score)
    # print(gmm)
    print("gmm纯度为:",score)
