from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Package():
    name: str
    source: str
    version: str
    last_updated: datetime
    
    maintainer: Optional[str] = None
    url: Optional[str] = None
    votes: Optional[int] = None
    is_orphaned: bool = False
    is_deprecated: bool = False
    
    


