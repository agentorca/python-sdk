"""
Custom exceptions for the Orca SDK.
"""


class OrcaException(Exception):
    """Base exception for all Orca SDK errors."""

    pass


class AuthenticationError(OrcaException):
    """Raised when API authentication fails."""

    pass


class SandboxCreationError(OrcaException):
    """Raised when sandbox creation fails."""

    pass


class SessionError(OrcaException):
    """Raised when SSH session operations fail."""

    pass


class ConnectionError(OrcaException):
    """Raised when WebSocket connection fails."""

    pass


class SandboxNotFoundError(OrcaException):
    """Raised when sandbox doesn't exist."""

    pass


class CommandExecutionError(OrcaException):
    """Raised when command execution fails."""

    pass
