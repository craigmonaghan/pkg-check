from typing import List
import requests
from datetime import datetime, timezone
from core.checker_base import CheckerBase
from core.package import Package
from parsers import exporter


class AURChecker(CheckerBase):
    def check_package(self, package_name: str) -> Package:
        self.package_name = package_name
        try:
            url = f"https://aur.archlinux.org/rpc/v5/info?arg[]={package_name}"
            response = requests.get(url, timeout=10)
            if response.status_code == 404:
                raise Exception(f"Package '{package_name}' not found on the AUR")
            
            response.raise_for_status()
            self.data = response.json()
            
            result = self.data['results'][0]
            version = result.get('Version', {})
            

            last_modified = result.get('LastModified')
            last_updated = datetime.fromtimestamp(last_modified, tz=timezone.utc) if last_modified else None
            
            
            package_url = f"https://aur.archlinux.org/packages/{package_name}"
            maintainer = result.get('Maintainer')

            return Package(
                name=package_name,
                source="AUR",
                version=version,
                last_updated=last_updated,
                maintainer=maintainer,
                url=package_url
            ) 
            
            
        except requests.exceptions.HTTPError as e:
            raise Exception(f"Package '{package_name}' not found on AUR") from e
        
        except requests.exceptions.Timeout:
            raise Exception(f"Request timed out while checking '{package_name}'")
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error while checking '{package_name}': {e}")

        except KeyError as e:
            raise Exception(f"Unexpected response format from AUR for '{package_name}'")

    def get_data(self, package_name):
        if self.data is not None:
            return self.data
    
    def get_parse(self, package_name):
        return exporter.export(package_name, AURChecker(), None)

    def list_installed(self) -> List[str]:
        return []