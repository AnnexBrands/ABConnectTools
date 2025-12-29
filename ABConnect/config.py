"""Configuration management for ABConnect.

This module provides centralized configuration handling with support
for different environments (production, staging, testing).
"""

import os
from typing import Optional, Dict, Any
from dotenv import load_dotenv, dotenv_values, find_dotenv


class Config:
    """Configuration manager for ABConnect."""

    _instance: Optional["Config"] = None
    _env_values: Dict[str, Any] = {}
    _loaded: bool = False
    _env: str = "production"  # Current environment type
    _env_file: str = ".env"   # Current env file path

    def __new__(cls):
        """Singleton pattern to ensure single config instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def load(cls, env: Optional[str] = None, force_reload: bool = False) -> "Config":
        """Load configuration from environment file.

        Args:
            env: Environment name ('staging', 'production', or None for default)
            force_reload: Force reload even if already loaded

        Returns:
            Config instance
        """
        instance = cls()

        # Determine env file from env parameter
        if env == "staging":
            env_file = ".env.staging"
            env_type = "staging"
        elif env == "production":
            env_file = ".env"
            env_type = "production"
        elif env is None:
            # Keep current or use default
            env_file = cls._env_file if cls._loaded else ".env"
            env_type = cls._env if cls._loaded else "production"
        else:
            # Custom env file path
            env_file = env if env.startswith(".env") else f".env.{env}"
            env_type = env

        if force_reload or not cls._loaded or cls._env_file != env_file:
            cls._env = env_type
            cls._env_file = env_file
            cls._env_values = {}

            # First load from environment file
            if os.path.exists(env_file):
                cls._env_values = dotenv_values(env_file)
                # Also load into os.environ for backward compatibility
                load_dotenv(env_file, override=True)

            cls._loaded = True

        return instance

    @classmethod
    def get(cls, key: str, default: Optional[str] = None) -> Optional[str]:
        """Get configuration value.

        Args:
            key: Configuration key
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        if not cls._loaded:
            cls.load()

        # Check loaded env values first
        if key in cls._env_values:
            return cls._env_values[key]

        # Fall back to os.environ
        return os.getenv(key, default)

    @classmethod
    def get_env(cls) -> str:
        """Get current environment (staging/production).

        Returns:
            Environment name (defaults to 'production')
        """
        # Use class variable if set, otherwise check environment
        if cls._loaded:
            return cls._env
        env = cls.get("ABC_ENVIRONMENT", "production")
        return "staging" if env.lower() == "staging" else "production"

    @classmethod
    def get_api_base_url(cls) -> str:
        """Get base API URL for current environment.

        Returns:
            Base API URL
        """
        if cls.get_env() == "staging":
            return "https://portal.staging.abconnect.co/api/api"
        return "https://portal.abconnect.co/api/api"

    @classmethod
    def get_catalog_base_url(cls) -> str:
        """Get base API URL for current environment.

        Returns:
            Base API URL
        """
        if cls.get_env() == "staging":
            return "https://catalog-api.staging.abconnect.co/api"
        return "https://catalog-api.abconnect.co/api"

    @classmethod
    def get_identity_url(cls) -> str:
        """Get identity server URL for current environment.

        Returns:
            Identity server URL
        """
        if cls.get_env() == "staging":
            return "https://login.staging.abconnect.co/connect/token"
        return "https://login.abconnect.co/connect/token"

    @classmethod
    def get_swagger_url(cls) -> str:
        """Get swagger API URL for current environment.

        Returns:
            Swagger API URL
        """
        # Allow override via environment variable
        custom_url = cls.get("ABC_SWAGGER_URL")
        if custom_url:
            return custom_url

        if cls.get_env() == "staging":
            return "https://portal.staging.abconnect.co/swagger/v1/swagger.json"
        return "https://portal.abconnect.co/swagger/v1/swagger.json"

    @classmethod
    def reset(cls):
        """Reset configuration (useful for testing)."""
        cls._loaded = False
        cls._env_values = {}
        cls._env_file = ".env"

    def __repr__(self):
        """Return string representation of Config instance."""
        return (
            f"<Config(env_file='{self._env_file}', "
            f"environment='{self.get_env()}', "
            f"loaded={self._loaded})>"
        )


# Convenience functions
def get_config(key: str, default: Optional[str] = None) -> Optional[str]:
    """Get configuration value.

    Args:
        key: Configuration key
        default: Default value if key not found

    Returns:
        Configuration value or default
    """
    return Config.get(key, default)


def load_config(env: Optional[str] = None, force_reload: bool = False) -> Config:
    """Load configuration from environment.

    Args:
        env: Environment name ('staging', 'production', or None)
        force_reload: Force reload even if already loaded

    Returns:
        Config instance
    """
    return Config.load(env, force_reload)
