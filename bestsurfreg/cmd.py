"""
Wrapper functions for external commands.
"""
import shlex
from pathlib import Path
import subprocess as sp
from colorama import Fore, Style
from datetime import datetime

FAILED = Style.BRIGHT + Fore.RED + 'FAILED' + Fore.RESET + Style.RESET_ALL


def register_surface_data(
        surface: Path,
        template_surface: Path,
        file_to_register: Path,
        sm_file: Path,
        registered_data: Path,
        min_control_mesh,
        max_control_mesh,
        blur_coef,
        neighborhood_radius,
        maximum_blur,
        bestsurfreg_log_file: Path,
        surface_resample_log_file: Path
) -> int:
    cmds: list[tuple[list[str | Path], Path]] = [
        (
            bestsurfreg(
                surface, template_surface, sm_file,
                min_control_mesh, max_control_mesh,
                blur_coef, neighborhood_radius, maximum_blur,
            ),
            bestsurfreg_log_file,
        ),
        (
            surface_resample(surface, template_surface, file_to_register, sm_file, registered_data),
            surface_resample_log_file
        )
    ]
    subject = _subj_log_name(surface)
    for cmd, log_file in cmds:
        str_cmd = shlex.join(map(str, cmd))
        print(f'{log_prefix(subject)}$> {str_cmd}', flush=True)
        with log_file.open('wb') as f:
            proc = sp.run(cmd, stdout=f, stderr=sp.STDOUT)
            if proc.returncode != 0:
                print(f'{log_prefix(subject)} {FAILED}, see {log_file}', flush=True)
                return proc.returncode
    return 0


def log_prefix(subj) -> str:
    now = datetime.now().isoformat()
    return f'{Style.DIM }[{now}{Style.RESET_ALL} {subj}{Style.DIM}]{Style.RESET_ALL}'


def bestsurfreg(
        surface: Path,
        target: Path,
        sm_file: Path,
        min_control_mesh,
        max_control_mesh,
        blur_coef,
        neighborhood_radius,
        maximum_blur,
):
    return [
        'bestsurfreg.pl',
        '-clobber',
        '-min_control_mesh', str(min_control_mesh),
        '-max_control_mesh', str(max_control_mesh),
        '-blur_coef', str(blur_coef),
        '-neighbourhood_radius', str(neighborhood_radius),
        '-maximum_blur', str(maximum_blur),
        surface,
        target,
        sm_file
    ]


def surface_resample(
        surface: Path,
        target: Path,
        data: Path,
        sm_file: Path,
        registered_data: Path,
):
    return ['surface-resample', '-nearest', surface, target, data, sm_file, registered_data]


def _subj_log_name(surface: Path) -> str:
    """Color coding of a subject identifier for terminal log output."""
    s = f'{surface.parent.name}/{surface.name}'
    color = _COLORS[hash(s) % len(_COLORS)]
    return color + s + Fore.RESET


_COLORS = (
    Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX,
)
