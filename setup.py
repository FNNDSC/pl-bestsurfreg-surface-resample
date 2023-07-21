from setuptools import setup
import re

_version_re = re.compile(r"(?<=^__version__ = (\"|'))(.+)(?=\"|')")

def get_version(rel_path: str) -> str:
    """
    Searches for the ``__version__ = `` line in a source code file.

    https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
    """
    with open(rel_path, 'r') as f:
        matches = map(_version_re.search, f)
        filtered = filter(lambda m: m is not None, matches)
        version = next(filtered, None)
        if version is None:
            raise RuntimeError(f'Could not find __version__ in {rel_path}')
        return version.group(0)


setup(
    name='bestsurfreg-surface-resample',
    version=get_version('bsr2.py'),
    description='ChRIS plugin wrapper for bestsurfreg.pl and surface-resample',
    author='FNNDSC',
    author_email='dev@babyMRI.org',
    url='https://github.com/FNNDSC/pl-bestsurfreg-surface-resample',
    py_modules=['bsr2'],
    install_requires=['chris_plugin'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'bsr2 = bsr2:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require={
        'none': [],
        'dev': [
            'pytest~=7.1'
        ]
    }
)
