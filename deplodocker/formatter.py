try:
    import orjson as json
except ImportError:
    import json

import toml
import yaml


def format_requirements(data: dict) -> str:
    result = []
    for group, values in data.items():
        result.append(f"### {group.upper()}\n")
        for extras, version in values.items():
            result.append(f"{extras}=={version}\n")
    return "".join(result)


def formatter(data: dict, format: str) -> str:
    if format == "json":
        proxy = json.dumps(data)
        if isinstance(proxy, bytes):
            proxy = proxy.decode()
        return proxy
    elif format == "toml":
        return toml.dumps(data)
    elif format == "yaml":
        return yaml.dump(data)
    elif format == "requirements.txt":
        return format_requirements(data)
    else:
        raise TypeError(f"Invalid format {format}")
