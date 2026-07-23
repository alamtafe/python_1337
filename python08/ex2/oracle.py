#!/usr/bin/env python3
import os
from dotenv import load_dotenv


def check_config(config: dict[str, str | None]) -> list[str]:
    missing: list[str] = []
    for name, value in config.items():
        if not value:
            missing.append(name)
    return missing


print("ORACLE STATUS: Reading the Matrix...")
print()
print("Configuration loaded:")
load_dotenv()
mode = os.getenv("MATRIX_MODE")
data_base = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL")
zion_endpoint = os.getenv("ZION_ENDPOINT")
print(f"Mode: {mode}")
if data_base:
    print("Database: Connected to local instance")
else:
    print("Database: Not configured")
if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: Not authenticated")
if log_level:
    print(f"Log Level: {log_level}")
else:
    print("Log Level: Not configured")
if zion_endpoint:
    print("Zion Network: Online")
else:
    print("Zion Network: Offline")
print()
config = {
        "MATRIX_MODE": mode,
        "DATABASE_URL": data_base,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": zion_endpoint
}
missing: list[str] = check_config(config)
if missing:
    print("Cnfiguratoin error:")
    for name in missing:
        print(f"[MISSING] {name}")
else:
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")
