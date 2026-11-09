# Security Policy

## Supported versions

Only the latest release on [PyPI](https://pypi.org/project/vibesequence/) receives security fixes.

## Reporting a vulnerability

Please **do not open a public issue** for security problems.

Report privately through GitHub:
[Security → Report a vulnerability](https://github.com/monkeymars/vibesequence/security/advisories/new).

Include what you found, how to reproduce it, and the affected version. You will get a reply within
7 days. Once a fix is released, the advisory is published and you are credited unless you ask otherwise.

## Verifying releases

Release artifacts carry signed build provenance:

```bash
gh attestation verify <file> --repo monkeymars/vibesequence
```
