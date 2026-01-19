from typing import List
import requests
from datetime import datetime, timezone
from core.checker_base import CheckerBase
from core.package import Package
import json

class PyPiChecker(CheckerBase):
    def check_package(self, package_name: str) -> Package:
        try:
            url = f"https://pypi.org/pypi/{package_name}/json"
            response = requests.get(url, timeout=10)
            if response.status_code == 404:
                raise Exception(f"Package '{package_name}' not found on PyPi")
            
            response.raise_for_status()
            self.data = response.json()
            
            version = self.data['info']['version']
            releases = self.data.get('releases', {})
            
            #Possibly rewrite as it just assumes its the latest release time
            date_str = releases[version][0].get('upload_time_iso_8601')
            last_updated = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            
            maintainers = self.data.get('info')
            maintainer = maintainers['author'] if maintainers else None
               
            return Package(
                name=package_name,
                source="PyPi",
                version=version,
                last_updated=last_updated,
                maintainer=maintainer,
                
            ) 
            
            
        except requests.exceptions.HTTPError as e:
            raise Exception(f"Package '{package_name}' not found on PyPi") from e
        
        except requests.exceptions.Timeout:
            raise Exception(f"Request timed out while checking '{package_name}'")
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error while checking '{package_name}': {e}")

        except KeyError as e:
            raise Exception(f"Unexpected response format from PyPi for '{package_name}'")

    def get_data(self, requests):
        requests = self.data
        if requests is not None:
            return requests
    
    
    def list_installed(self) -> List[str]:
        return []