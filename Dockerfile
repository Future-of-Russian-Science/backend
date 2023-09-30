FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

# Test Nvidia-smi works
RUN nvidia-smi

WORKDIR /backend
COPY . .

RUN apt update && apt install -y build-essential wget

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility,graphics
ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV CUDA_HOME=/usr/local/cuda

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "server.py"]