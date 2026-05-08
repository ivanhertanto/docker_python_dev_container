# Base image with Python 3.11 (change tag as needed)
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set a non-root user for safer dev
ARG USER=dev
ARG UID=1000
ARG GID=1000

# Install OS packages needed for development & common tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    wget \
    ca-certificates \
    vim \
    less \
    procps \
    net-tools \
    iproute2 \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create user and workspace
RUN groupadd -g ${GID} ${USER} || true \
    && useradd -m -u ${UID} -g ${GID} -s /bin/bash ${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USER} \
    && chmod 0440 /etc/sudoers.d/${USER}

WORKDIR /workspace
RUN chown ${USER}:${USER} /workspace

# Configure git global defaults for the non-root user
RUN sudo -u ${USER} git config --global --add safe.directory /workspace \
 && sudo -u ${USER} git config --global user.name "Bernardus Ivan Hertanto" \
 && sudo -u ${USER} git config --global user.email "ivan.bernardus@gmail.com"

# Switch to non-root user
USER ${USER}

# Create and activate virtualenv at /home/dev/venv (optional)
ENV VENV_PATH=/home/${USER}/venv
RUN python -m venv ${VENV_PATH}
ENV PATH="${VENV_PATH}/bin:${PATH}"

# Upgrade pip and install common dev tooling
RUN pip install --upgrade pip setuptools wheel

# Copy requirements file if you have one (optional)
# COPY --chown=${USER}:${USER} requirements.txt /workspace/
# RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Expose a port if you plan to run a dev server (optional)
EXPOSE 8000

# Default entry: keep a shell for interactive terminal use
CMD [ "bash" ]