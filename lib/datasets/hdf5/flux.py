from ..model import DataSet
import h5py



class FluxHdf5(DataSet):

    def __init__(self, hdf5_file: h5py.File): ...

    @staticmethod
    def match(hdf5_file: h5py.File) -> bool:
        return False

    def convert(self): ...

    def save(self, output_path: str): ...