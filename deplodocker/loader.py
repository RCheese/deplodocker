def load_poetry_lock(data: dict):
    pkgs = {p["name"]: p for p in data["package"]}

    result = {}
    result["main"] = {
        k: v["version"] for k, v in pkgs.items() if ((v["category"] == "main") and (v["optional"] == False))
    }
    if not result["main"]:
        del result["main"]
    result["dev"] = {k: v["version"] for k, v in pkgs.items() if v["category"] == "dev"}
    if not result["dev"]:
        del result["dev"]
    if data.get("extras"):
        for k, v in data["extras"].items():
            result[k] = {}
            for e in v:
                result[k][e] = pkgs[e]["version"]
    return result


def loader(data: dict, format: str) -> dict:
    if format == "poetry":
        return load_poetry_lock(data)
    elif format == "pipfile":
        raise NotImplemented
    elif format == "pipenv":
        raise NotImplemented
    elif format == "requirements.txt":
        raise NotImplemented
    else:
        raise TypeError(f"Invalid format {format}")
