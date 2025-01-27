from typing import List
import h5py
import numpy as np
import os
from .dataset_model import DataSet


def get_files(path: str) -> List[str]:
    """
    Takes a file path or directory path and returns a list of files.
    If the path refers to a file, returns a list with that file.
    If the path refers to a directory, returns a list of files within that directory (non-recursive).

    Args:
        path (str): The file or directory path.

    Returns:
        List[str]: A list of file paths.
    """
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return []


def build_output_path(file_path: str, output_dir: str) -> str:
    """
    Constructs a new file path using the specified output directory and the filename of the original file path.

    Args:
        file_path (str): The original file path.
        output_dir (str): The directory where the new file path should reside.

    Returns:
        str: The new file path in the output directory.
    """
    filename = os.path.basename(file_path)
    return os.path.join(output_dir, filename)


def minimal_h5_file(
        data_set: DataSet,
        file_name: str,
        output_dir: str = "",
    ):
    """
    Creates an h5 file containing time data and AACGM coordinates.

    Args:
        data_set (DataSet): The data set to use.
        file_name (str): The h5 file name.
        output_dir (str): The output directory of the h5 file.
    """

    dtype = np.dtype([
        ('year', 'u2'), ('month', 'u1'), ('day', 'u1'),
        ('hour', 'u1'), ('min', 'u1'), ('sec', 'u1'),
        ('mlat', 'f8'), ('mlon', 'f8'), ('mlt', 'f8')
    ])
    
    data = []
    for timestamp, mlat, mlon, mlt in data_set.get_aacgm_data():
        data.append((
            timestamp.year, timestamp.month, timestamp.day,
            timestamp.hour, timestamp.minute, timestamp.second,
            mlat, mlon, mlt
        ))
    
    data = np.array(data, dtype=dtype)
    output_path = os.path.join(output_dir, file_name + ".hdf5")
    with h5py.File(output_path, "w") as h5f:
        h5f.create_dataset("/Data", data=data)




    