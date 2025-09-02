import os
import sys
import platform
import subprocess
import urllib.request
import tarfile
from pathlib import Path

TRIVY_VERSION = "0.56.2"  # pin the version here
CACHE_DIR = Path.home() / ".cache" / "trivy-wrapper" / TRIVY_VERSION
TRIVY_BIN = CACHE_DIR / "trivy"


def ensure_trivy_installed():
    if TRIVY_BIN.exists():
        return

    system = platform.system()
    arch = platform.machine().lower()

    if system == "Linux":
        os_name = "Linux"
    elif system == "Darwin":
        os_name = "macOS"
    elif system == "Windows":
        os_name = "Windows"
    else:
        raise RuntimeError(f"Unsupported OS: {system}")

    if arch in ("x86_64", "amd64"):
        arch_name = "64bit"
    elif arch in ("arm64", "aarch64"):
        arch_name = "ARM64"
    else:
        raise RuntimeError(f"Unsupported architecture: {arch}")

    url = f"https://github.com/aquasecurity/trivy/releases/download/v{TRIVY_VERSION}/trivy_{TRIVY_VERSION}_{os_name}-{arch_name}.tar.gz"

    print(f"[trivy-wrapper] Downloading Trivy {TRIVY_VERSION} from {url}", file=sys.stderr)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    tar_path = CACHE_DIR / "trivy.tar.gz"
    urllib.request.urlretrieve(url, tar_path)

    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extracta
