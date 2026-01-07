from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Package():
    name: Optional[str] = None
    source: Optional[str] = None
    version: Optional[str] = None
    last_updated: Optional[datetime] = None
    
    maintainer: Optional[str] = None
    url: Optional[str] = None
    votes: Optional[int] = None
    is_orphaned: bool = False
    is_deprecated: bool = False
    
    


