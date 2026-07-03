# Update Trivy Version

Use this skill to update the Trivy version used by this repository.

## Inputs
- If the user provides a specific version, use that version.
- Otherwise, use the latest release from https://github.com/aquasecurity/trivy/releases.

## Process
1. Check the Trivy releases page and identify the target release.
2. Read the release notes for that release and look for suspicious commits or anything unusual.
3. If anything looks suspicious, stop and ask the user for confirmation before making changes. Include the suspicious commits or notes in the prompt so the user can decide.
4. Download the `trivy_<version>_checksums.txt` asset for the chosen release.
5. Use that checksum file to update the sha256 values for every platform entry in `setup.cfg`.
6. Update every Trivy download URL in `setup.cfg` to the chosen version.
7. Update the README example so the pre-commit `rev` matches the new Trivy version.

## Files to update
- `setup.cfg`
- `README.md`

## Notes
- Keep the repository formatting and existing file layout intact.
- Make sure the version string stays consistent everywhere it appears.
