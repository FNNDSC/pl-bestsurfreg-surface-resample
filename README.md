# Surface Data Registration

[![Version](https://img.shields.io/docker/v/fnndsc/pl-bestsurfreg-surface-resample?sort=semver)](https://hub.docker.com/r/fnndsc/pl-bestsurfreg-surface-resample)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-bestsurfreg-surface-resample)](https://github.com/FNNDSC/pl-bestsurfreg-surface-resample/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-bestsurfreg-surface-resample/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-bestsurfreg-surface-resample/actions/workflows/ci.yml)

`pl-bestsurfreg-surface-resample` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin which does surface registration using MNI/CIVET tools.
The inputs are MNI `.obj` surfaces of either the left or right brain hemisphere.
For each surface, the registered vertex-wise data is produced as a `.txt` file,
as well as the intermediate `.sm` registration map file.

In its default configuration, it uses the average 29 gestational age
fetal brain template of the [Im Lab](https://research.childrenshospital.org/neuroim/)
to register a mask of the medial cut.

![before](img/before.png)
![after](img/after.png)

Figure: (Left) mask does not cover medial cut. (Right) mask is registered to cover the medial cut.

## Installation

`pl-bestsurfreg-surface-resample` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://raw.githubusercontent.com/FNNDSC/ChRIS_store_ui/963938c241636e4c3dc4753ee1327f56cb82d8b5/src/assets/public/badges/light.svg)](https://chrisstore.co/plugin/pl-bestsurfreg-surface-resample)

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `pl-bestsurfreg-surface-resample` as a container:

```shell
apptainer exec docker://fnndsc/pl-bestsurfreg-surface-resample bsrr [--args values...] input/ output/
```

To print its available options, run:

```shell
apptainer exec docker://fnndsc/pl-bestsurfreg-surface-resample bsrr --help
```
