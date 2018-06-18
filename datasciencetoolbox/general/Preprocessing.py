"""
Preprocessing module

"""


from sklearn.neighbors import NearestNeighbors
import pandas as pd


def remove_outliers(data_table: pd.DataFrame, strategy: str):
    """Method for removing outliers in a data table based on different
    strategies

    More complete descriptions of the strategies below will be provided

    Strategies:
        'normal' remove points outside the 95% confidence interval
        'knn-avg-distance' remove points with a

    """

    if strategy == 'normal':
        # TODO: Implement
        pass
    elif strategy == 'knn-avg-distance':
        # TODO: Implement
        # Find avg knn distances
        # data_table = remove_outliers(knn_distances,strategy='normal')

        nbrs = NearestNeighbors(
            n_neighbors=5, algorithm='ball_tree', metric='euclidean').fit(points)
        distances, indices = nbrs.kneighbors(points)

    return NotImplemented
