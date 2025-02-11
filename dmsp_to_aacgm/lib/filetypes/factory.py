from ..dataset_model import DataSet
from .hdf5.factory import hdf5_dataset_factory


def dataset_factory(file_path: str) -> DataSet:
    extension = file_path.split(".")[-1]

    factory_mapping = {
        "hdf5": hdf5_dataset_factory
    }

    if factory := factory_mapping.get(extension):
        return factory(file_path)
    
    raise Exception(f"Cannot process file type: {extension}")