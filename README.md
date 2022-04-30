## Accelerating Large Network Data Analytics using Graph Neural Networks (GNNs)

Analysis of large network data analytics has as high theoretical and practical significance. Centrality measures are one of the most common schemes that is employed currently for large-scale network analysis. However, existing deterministic algorithms for computing this for individual node takes a lot of time and are computationally super-expensive. This problem elevates when the analysis is done for very large graphs. Getting an approximate estimates of these centrality measures with much lower time would be of great significance in network analytics. In this project, I aim to do the same using Graph Neural Networks (GNNs). In this project, I aim to do the same using Graph Neural Networks (GNNs). I train a GNN based model on a synthetically generated dataset consisting of variety of networks to approximate these centrality values. The tests on complex real networks datasets shows that GNN gives promising results in predicting these values along with a huge speed-up of nearly $80$-times when compared to the currently used deterministic algorithms when computed over a CPU. Furthermore, the gap in the speedup of GNN-based approach over conventional methods seems to be more massive when a GPU is harnessed.



### Dependencies

* PyTorch (Above 1.4 recommended)

* NetworkX (Loading Graphs)

* Networkit (Sparse Matrix Conversion)

* Other: Scipy, numpy & pickle



### Data

You can get the data as follows: 

* Download Graphs from [here](https://drive.google.com/drive/folders/1EAb4GFIUoFJi50vtWfuJl0yhx2vs1Ijc?usp=sharing).
* Download different types of networks from [here](https://drive.google.com/drive/folders/1oWFLLRMcucU5Copc7LhWBN_MBHvMx7Kt?usp=sharing). The exact training and test sets are also available in the same folder.      

Download the above files and move it to the `./data` directory.

### Quick Look

`./data`: Data Directory

`./data/data_generation.py`: Sample file used for generating the synthetic data.

`betweenness.py`: Train GNN on betweenness centrality.

`degree.py`: Train GNN on Degree centrality.

`Closeness.py`: Train GNN on closeness centrality.

`GNN_layers.py`: Embedding Layer and GNN layer defined.

`model.py` : GNN model defined.

`criterion.py`: Margin-Rank Loss defined.

`utils.py` : Helper function including Adjacency, Sparse, Torch Tensor conversion. 

## Key Results

Obtained Hit Rates along with its margin of error on the test data.

| Centrality Measure      | Top 5%     | Top 10% |Top 20%  |
| :---                    |    :---:   | :---:   |    ---: |
| Degree      | 89.05  $\pm$ 1.57  | 93.14 $\pm$ 1.20  |  99.11 $\pm$ 0.68  |
| Betweenness | 83.20  $\pm$ 1.64      | 90.58 $\pm$ 1.47  | 98.25 $\pm$ 2.40   |
| Closeness   | 78.92  $\pm$ 4.16      | 85.07 $\pm$ 3.84  | 89.25 $\pm$ 4.62   |

Other key results can be found in the directory `./Figures`