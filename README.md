# DMSP-to-AACGM Converter CLI Tool

A command-line tool for converting geomagnetic coordinates in DMSP data files to AACGM coordinates. This tool leverages the [aacgmv2 Python library](https://github.com/aburrell/aacgmv2). The tool currently supports conversions of the following data files:

| **Source**                     | **File Type** | **Contents**                                | **Example**                   |
|--------------------------------|---------------|--------------------------------------------|--------------------------------|
| [Cedar Madrigal Database](http://cedar.openmadrigal.org)        | HDF5          | 1-second resolution for Ion Drift, Magnetometer, and Electron Density | `dms_20150410_16s1.001.hdf5`  |
| [Cedar Madrigal Database](http://cedar.openmadrigal.org)        | HDF5          | Flux/Energy values                         | `dms_20150410_16e.001.hdf5`   |

## Installation

```pip install dmsp-to-aacgm```

## Usage

```dmsp-to-aacgm <input file/directory> [<output directory>]```

If the output directory is not specified, or the output directory is the same as the input directory, the input files will be modified.

## Examples

| **Command**                                        | **Description**                                      |
|---------------------------------------------------|------------------------------------------------------|
| `dmsp-to-aacgm dms_20150410_16s1.001.hdf5`        | Convert a single file                                |
| `dmsp-to-aacgm dms_20150410_16s1.001.hdf5 aacgm_conversions` | Convert a single file, output to `aacgm_conversions` |
| `dmsp-to-aacgm dmsp_data`                         | Convert all files in `dmsp_data`                     |
| `dmsp-to-aacgm dmsp_data aacgm_conversions`       | Convert all files in `dmsp_data`, output to `aacgm_conversions` |

## Acknowledgements

This project was guided by Simon Wing. We also acknowledge the following grants:

**NASA Grants**:
- 80NSSC20K0704
- 80NSSC22K0515
- 80NSSC23K0899
- 80NSSC23K0904

**NSF CEDAR Grants**:
- 2431665

This software is distributed for free under a MIT license. If you find it useful, please acknowledge our work in your publications or projects.

## Contact Info

Simon Wing: simon.wing@jhuapl.edu

Carson O'Ffill: offill@andrews.edu