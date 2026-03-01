from typing import List
import requests
from datetime import datetime
from core.checker_base import CheckerBase
from core.package import Package
from parsers import exporter

class NPMChecker(CheckerBase):
    def check_package(self, package_name: str) -> Package:
        self.package_name = package_name
        try:
            url = f"https://registry.npmjs.org/{package_name}"
            response = requests.get(url, timeout=10)
            if response.status_code == 404:
                raise Exception(f"Package '{package_name}' not found on NPM")
            
            response.raise_for_status()
            self.data = response.json()
            
            date_str = self.data['time']['modified']
            last_updated = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            
            version = self.data['dist-tags']['latest']
            
            maintainers = self.data.get('maintainers', [])
            maintainer = maintainers[0]['name'] if maintainers else None

            package_url = f"https://www.npmjs.com/package/{package_name}"

            return Package(
                name=package_name,
                source="npm",
                version=version,
                last_updated=last_updated,
                maintainer=maintainer,
                url=package_url
            )
            
        except requests.exceptions.HTTPError as e:
            raise Exception(f"Package '{package_name}' not found on NPM") from e
        
        except requests.exceptions.Timeout:
            raise Exception(f"Request timed out while checking '{package_name}'")
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error while checking '{package_name}': {e}")

        except KeyError as e:
            raise Exception(f"Unexpected response format from NPM for '{package_name}'")
    
    def get_data(self, package_name):
        if self.data is not None:
            return self.data
    
    def get_parse(self, package_name):
        return exporter.export(package_name, NPMChecker(), None)
    
    def list_installed(self) -> List[str]:
        return []