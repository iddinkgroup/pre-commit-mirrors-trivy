# pre-commit-mirrors-trivy
pre-commit hook that mirrors the trivy for usage as pre-commit language

## Usage

```yaml
- repo: https://github.com/GaukeT/pre-commit-mirrors-trivy
  rev: v0.0.5
  hooks:
    - id: trivy-fs
      args: [./tf]
```
