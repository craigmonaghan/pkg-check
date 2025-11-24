from typing import List
import requests
from datetime import datetime
from core.checker_base import CheckerBase
from core.package import Package

class NPMChecker(CheckerBase):
    def check_package(self, package_name: str) -> Package:
        try:
            url = f"https://registry.npmjs.org/{package_name}"
            response = requests.get(url, timeout=10)
            if response.status_code == 404:
                raise Exception(f"Package '{package_name}' not found on NPM")
            
            response.raise_for_status()
            data = response.json()
            
            date_str = data['time']['modified']
            last_updated = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            
            version = data['dist-tags']['latest']
            
            maintainers = data.get('maintainers', [])
            maintainer = maintainers[0]['name'] if maintainers else None
            
            return Package(
                name=package_name,
                source="npm",
                version=version,
                last_updated=last_updated,
                maintainer=maintainer
            )
            
        except requests.exceptions.HTTPError as e:
            raise Exception(f"Package '{package_name}' not found on NPM") from e
        
        except requests.exceptions.Timeout:
            raise Exception(f"Request timed out while checking '{package_name}'")
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error while checking '{package_name}': {e}")

        except KeyError as e:
            raise Exception(f"Unexpected response format from NPM for '{package_name}'")
    
    def list_installed(self) -> List[str]:
        return []