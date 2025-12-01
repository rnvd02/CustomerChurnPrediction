FROM python:-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY Requirements.txt /workspace/Requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r /workspace/Requirements.txt

CMD ["bash"]