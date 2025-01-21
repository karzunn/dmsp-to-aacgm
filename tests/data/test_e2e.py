from typing import List
import unittest
from click.testing import CliRunner
from dmsp_to_aacgm import cli

class TestCli(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    def run_tool(self, args: List[str] = []):
        return self.runner.invoke(cli, args)

    def test_single_file(self):
        result = self.run_tool(['"data\\dms_20150410_16s1.001.hdf5"'])
        print(result.output)
        assert False
