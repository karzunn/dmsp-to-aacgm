from typing import Callable
import click
import h5py
from abc import ABC, abstractmethod

class DataSet(ABC):

    @abstractmethod
    def convert(self): ...

    @abstractmethod
    def save(self, output_path: str): ...


def data_reader_factory(file_path: str) -> Callable:
    if file_path.endswith(".hdf5"):
        return hdf5_reader
    raise Exception(f"Cannot process file type: {file_path.split(".")[-1]}")
    
def hdf5_reader(file_path: str) -> DataSet:
    contents = h5py.File(file_path, "r")
    if contents.get("Data", {}).get("Table Layout"):
        return DmspHdf5Data(file_path)


class DmspHdf5Data(DataSet):
    def __init__(self, path: str):
        self.contents = h5py.File(path, "r")
        self.data_set = self.contents["Data"]["Table Layout"]
        print(self.data_set.dtype.descr)

    def convert(self): ...

    def save(self): ...


@click.command()
@click.argument("path", type=click.Path(exists=True))
def cli(path):
    file_reader = data_reader_factory(path)
    data_set = file_reader(path)
    data_set.convert()
    data_set.save()