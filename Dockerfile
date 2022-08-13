#container name : plotly_demo
#build : docker build -t plotly_demo .
#run : docker run --gpus all -d -p 8050:8050 plotly_demo
#run : docker run -it --gpus all -p 8050:8050 plotly_demo
#access dash app : http://localhost:8050

ARG CUDA_VERSION=11.5
ARG LINUX_VERSION=ubuntu20.04
ARG PYTHON_VERSION=3.8
#ARG CUDA_VERSION=10.2
#ARG LINUX_VERSION=ubuntu16.04
FROM rapidsai/rapidsai:22.06-cuda${CUDA_VERSION}-runtime-${LINUX_VERSION}-py${PYTHON_VERSION}

WORKDIR /rapids/
RUN mkdir census_demo

WORKDIR /rapids/census_demo
RUN mkdir data
WORKDIR /rapids/census_demo/data
RUN curl https://s3.us-east-2.amazonaws.com/rapidsai-data/viz-data/census_data.parquet.tar.gz -o census_data.parquet.tar.gz
RUN tar -xvzf census_data.parquet.tar.gz


WORKDIR /rapids/census_demo

COPY . .

#disabled to run docker build faster
#enable the following command for the real build
RUN source activate rapids \
    && conda install -y -c conda-forge -c anaconda --file environment_for_docker.yml \
#    && pip install Werkzeug==2.0.0 \
    && pip install dash-dangerously-set-inner-html 

ENTRYPOINT ["bash","./entrypoint.sh"]
