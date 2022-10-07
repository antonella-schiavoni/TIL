from pathlib import path


readme = Path("README.md").resolve()

print(f"Absolute path": {readme.absolute()})
print(f"File name: {readme.name}")
print(f"Path root: {readme.root}")
print(f"Parent directory: {readme.parent}")
print(f"File extension: {readme.suffix}")
print(f"Is it absolute: {readme.is_absolute()}")

# Operators:
etc = Path('/etc')
joined = etc / "cron.d" / "anacron"
print(f"Exists? - {joined.exists()}")
