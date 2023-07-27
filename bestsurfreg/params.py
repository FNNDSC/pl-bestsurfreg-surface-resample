from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from bestsurfreg import __version__
from bestsurfreg.find_template import FILE_RESOLUTION_DESCRIPTION

parser = ArgumentParser(description='ChRIS plugin wrapper for bestsurfreg.pl and surface-resample',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-c', '--copy', action='store_true',
                    help='Copy all input files to output dir.')
parser.add_argument('-p', '--pattern', default='**/*.obj', type=str,
                    help='input surface file filter glob')
parser.add_argument('-o', '--output_fname', type=str,
                    default='{}.to_individual.txt',
                    help='Name for output registered surface data. '
                         '{} represents the basename of the input file.')
parser.add_argument('-t', '--target', type=str,
                    default='fetal-template-29/bh.smoothwm.mni.obj',
                    help=f'Registration target. {FILE_RESOLUTION_DESCRIPTION}')
parser.add_argument('-d', '--data', type=str,
                    default='fetal-template-29/bh.mask.1D.dset',
                    help='Vertex-wise data (which can be a mask) to be registered from the target '
                         f'to each input surface. {FILE_RESOLUTION_DESCRIPTION}')
parser.add_argument('--min_control_mesh', type=int, default=80,
                    help='control mesh must be no less than X nodes...')
parser.add_argument('--max_control_mesh', type=int, default=81920,
                    help='control mesh must be no greater than X nodes...')
parser.add_argument('-blur_coef', type=float, default=1.25,
                    help='factor to increase/decrease blurring')
parser.add_argument('--neighbourhood_radius', type=float, default=2.8,
                    help='neighbourhood radius')
parser.add_argument('--maximum_blur', type=float, default=1.9,
                    help='specify target spacing')

parser.add_argument('-V', '--version', action='version',
                    version=f'%(prog)s {__version__}')
