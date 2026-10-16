"""Open-source live-trading hook for this Jesse fork.

The MIT dashboard enables the Live tab when `import jesse_live` succeeds.
This package is our adapter, not the commercial plugin. Do not run
`jesse install-live` and do not set LICENSE_API_TOKEN.
"""

from jesse_live.version import __version__

__all__ = ["__version__"]
