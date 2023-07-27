FROM docker.io/fnndsc/pl-bestsurfreg-surface-resample:base-1

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="Surface Data Registration" \
      org.opencontainers.image.description="ChRIS plugin wrapper for bestsurfreg.pl and surface-resample"

COPY ./fetal-template-29 $MNI_DATAPATH/fetal-template-29

COPY . /usr/local/src/pl-bestsurfreg-surface-resample
ARG extras_require=none
RUN pip install "/usr/local/src/pl-bestsurfreg-surface-resample[${extras_require}]" \
    && rm -rf /usr/local/src/pl-bestsurfreg-surface-resample

CMD ["bsrr"]
