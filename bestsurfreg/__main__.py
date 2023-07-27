#!/usr/bin/env python
import itertools
import os
import sys
import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from chris_plugin import chris_plugin, PathMapper, curry_name_mapper

from bestsurfreg import DISPLAY_TITLE
from bestsurfreg.cmd import register_surface_data
from bestsurfreg.find_template import find_template
from bestsurfreg.params import parser


@chris_plugin(
    parser=parser,
    title='Surface Data Registration',
    category='MRI',  # ref. https://chrisstore.co/plugins
    min_memory_limit='1Gi',  # supported units: Mi, Gi
    min_cpu_limit='1000m',  # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0  # set min_gpu_limit=1 to enable GPU
)
def main(options, inputdir: Path, outputdir: Path):
    print(DISPLAY_TITLE, flush=True)
    if options.copy:
        shutil.copytree(inputdir, outputdir)

    try:
        template_surface = find_template(options.target, inputdir)
        file_to_register = find_template(options.data, inputdir)
    except FileNotFoundError as e:
        logger.error(str(e))
        sys.exit(1)

    proc = len(os.sched_getaffinity(0))
    print(f'Using {proc} threads', flush=True)

    mapper = PathMapper.file_mapper(inputdir, outputdir, glob=options.pattern,
                                    name_mapper=curry_name_mapper(options.output_fname))

    with ThreadPoolExecutor(max_workers=proc) as pool:
        results = pool.map(
            call_register_surface_data,
            mapper,
            itertools.repeat(template_surface),
            itertools.repeat(file_to_register),
            itertools.repeat(options)
        )

    rc = next(filter(lambda r: r != 0, results), 0)
    sys.exit(rc)


def call_register_surface_data(t: tuple[Path, Path], template_surface: Path, file_to_register: Path, options) -> int:
    input_surface, output_registered_data = t
    sm_file = output_registered_data.with_suffix('.sm')

    return register_surface_data(
        input_surface, template_surface, file_to_register, sm_file, output_registered_data,
        options.min_control_mesh, options.max_control_mesh, options.blur_coef,
        options.neighbourhood_radius, options.maximum_blur,
        output_registered_data.with_suffix('.bestsurfreg.log'),
        output_registered_data.with_suffix('.surface-resample.log')
    )


if __name__ == '__main__':
    main()
