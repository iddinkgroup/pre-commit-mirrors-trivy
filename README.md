[![build status](https://github.com/GaukeT/pre-commit-mirrors-trivy/actions/workflows/main.yml/badge.svg)](https://github.com/GaukeT/pre-commit-mirrors-trivy/actions/workflows/main.yml)

# pre-commit-mirrors-trivy

pre-commit hook that mirrors the trivy for usage as pre-commit language

Internally this package provides a convenient way to download the pre-built
trivy binary for your particular platform.

### As a pre-commit hook

See [pre-commit] for instructions

Sample `.pre-commit-config.yaml`:
```yaml
- repo: https://github.com/GaukeT/pre-commit-mirrors-trivy
  rev: v0.66.0
  hooks:
    - id: trivy-fs
      args:
        - --exit-code=1 # Example: set exit with code 1
        - --debug # Example: enable debug output
        - . # Example: scan current directory (provide DIR as last argument if `args` are used)
    - id: trivy-config
```

[trivy]: https://trivy.dev/
[pre-commit]: https://pre-commit.com
