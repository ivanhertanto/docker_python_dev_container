# Dockerfile for a Python dev container (with interactive terminal) 


## Usage

### Build:

```
docker build -t ivanhertanto/pydev:latest .
```

### Run an interactive terminal:

```
docker run --rm -it -v "$PWD":/workspace -w /workspace ivanhertanto/pydev:latest bash
```

### On Windows:
```
docker run --rm -it -v ${PWD}:/workspace -w /workspace ivanhertanto/pydev:latest bash
```

This mounts your project folder into /workspace and drops you into a bash shell inside the container where the virtualenv is active.


> ✅ **Note:** 
> * Uncomment and use COPY requirements.txt if you want dependencies baked into the image.
> * Adjust Python version, tools, and user IDs to match your environment.
> * For VS Code Remote Containers or other editors, add a devcontainer.json or appropriate config