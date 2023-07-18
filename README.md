# image_resize

It resizes images. An example of how to get started.

-----

**Table of Contents**

- [image\_resize](#image_resize)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Development](#development)
    - [Setup](#setup)
    - [Workflow](#workflow)

## Installation

```bash
# Unix
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install git+https://github.com/JonTheBurger/image_resize
image_resize --help
```

```ps1
# Windows
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install git+https://github.com/JonTheBurger/image_resize
image_resize --help
```

## Usage

```bash
image_resize --output out/ 'images/*.png'
```

## Development

### Setup

```bash
# Dependencies for Ubuntu 22.04+
sudo apt-get update && \
  sudo apt-get install -y \
    python3 \
    python3-venv \
    pipx
pipx install hatch
```

```ps1
# Install python3.10+, e.g. (https://docs.chocolatey.org/en-us/choco/setup)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
choco install python3
refreshenv

# Open Non-Admin shell, install dependencies
python -m pip install pipx
pipx install hatch
```

### Workflow

This project is packaged using [Hatch](https://hatch.pypa.io/latest/). A few helpful
commands to get you started:

- `hatch shell`: Creates and enters a virtual environment suitable for development
- `hatch env find`: Shows the path containing `python` for the current venv.
- `hatch env show`: Lists all environments and commands
- `hatch run lint:all`: Runs all linters
- `hatch run test`: Runs (all zero) unit tests
