FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

WORKDIR /backend
COPY . .

RUN apt update && apt install -y build-essential wget unzip apt-utils && apt install -y --no-install-recommends \
    pkg-config \
    libglvnd0 \
    libgl1 \
    libglx0 \
    libegl1 \
    libgles2 \
    libglvnd-dev \
    libgl1-mesa-dev \
    libegl1-mesa-dev \
    libgles2-mesa-dev \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev && rm -rf /var/lib/apt/lists/*

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility,graphics
ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV CUDA_HOME=/usr/local/cuda

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "server.py"]