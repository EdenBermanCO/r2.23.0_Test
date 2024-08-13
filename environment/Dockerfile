# hash:sha256:abea52080ed84b12da3355696f584a42c1327b749bff88a065fe5b43171a82a1
FROM registry.useast1.r2230.aws.codeocean.dev/codeocean/py-r:python3.10.12-R4.2.3-IRkernel-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip install -U --no-cache-dir \
    setuptools==70.3.0
RUN pip install -U --no-cache-dir \
    mlflow==2.15.1 \
    pandas==2.2.2 \
    scikit-learn==1.5.1 \
    xgboost==2.1.1
