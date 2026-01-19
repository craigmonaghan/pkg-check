from core.package import Package
from datetime import datetime

# Create a test package
pkg = Package(
    name="neovim",
    source="aur",
    version="0.10.0",
    last_updated=datetime.now(),
    maintainer="some_user",
    votes=1234
    
)

# Print it
print(pkg)
print(f"\nPackage name: {pkg.name}")
print(f"From: {pkg.source}")
print(f"Votes: {pkg.votes}")
print(datetime.now())