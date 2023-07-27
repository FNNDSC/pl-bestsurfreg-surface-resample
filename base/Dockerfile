FROM docker.io/fnndsc/microminc-builder:latest as builder

RUN microminc.sh -p '&do_cmd' bestsurfreg.pl surface-resample \
    surftracc surface-stats measure_surface_area print_n_polygons \
    /microminc

FROM python:3.11.2-slim-bullseye

RUN apt-get update && apt-get install -y perl \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /microminc /opt/microminc
ENV PATH=/opt/microminc/bin:$PATH \
    LD_LIBRARY_PATH=/opt/microminc/lib:$LD_LIBRARY_PATH \
    MINC_FORCE_V2=1 MINC_COMPRESS=4 VOLUME_CACHE_THRESHOLD=-1 \
    CIVET_JOB_SCHEDULER=DEFAULT \
    MNIBASEPATH=/opt/microminc \
    MNI_DATAPATH=/opt/microminc/share \
    PERL5LIB=/opt/microminc/perl
