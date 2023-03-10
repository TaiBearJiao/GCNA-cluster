# GCNA-cluster: A Gene Co-expression Network Alignment to Cluster Cancer Patients Algorithm for Identifying Subtypes of Pancreatic Ductal Adenocarcinoma
First, the GCNA-cluster algorithm constructed a weighted gene co-expression network for each patient.Secondly, network alignment was performed between pairs of gene co-expression networks, and the score of alignment was the similarity between patients. By extrapolating from this, a patient-patient similarity matrix can be obtained. Finally, cluster patients according to their similarity.
## The environment of GCNA-cluster
Rstudio 4.0.2<br>
Matlab R2016a
## Code and data
### Raw data
For the cancer data used in the paper, the TCGA database (https://portal.gdc.cancer.gov/) and the GEO database (https://www.ncbi.nlm.nih.gov/geo/, GEO accession: GSE15471 and GSE17891) were used. 
### Construction of Gene Co-expression Network
The `gene expression.txt` file in the `TCGA_Network` (or GEO_Network) folder is used as input and `onePatienNet.R` is run to generate the patients' gene co-expression network.
### Network Alignment
The `geneCo-expressionNetwork_TCGA.zip` (or geneCo-expressionNetwork_GEO.zip) file in the `TCGA_Network` (or GEO_Network) folder can be extracted to obtain the generated gene co-expression network, which is the result of the previous step. Using these gene co-expression networks as input, run `network_alignment.m` to obtain the patient-patient similarity matrix.
### Cluster
Using the `similarityMatrix.txt` file in the `TCGA_Network` (or GEO_Network) folder as input, which is the result of the previous network alignment step, run the `spectralCluster.R` file to cluster the patients.
### Baseline method
The `Baseline methods` folder contains all the baseline methods compared to GCNA-cluster in the paper, the Consensus clustering and NMF clustering code in the `consensus and nmf.R` file, and the `baseline methods.py` file contains the kmeans, GMM, Birch, and GCNA-Agglomerative code.
