from dataclasses import dataclass
from datetime import datetime, timezone
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
    
    


    def updated_display(self) -> str:
        if not self.last_updated:
            return "Unknown"

        now = datetime.now(timezone.utc)
        delta = now - self.last_updated
        days = delta.days

        if days >= 365:
            relative = f"{days // 365} years ago"
        elif days >= 30:
            relative = f"{days // 30} months ago"
        elif days >= 1:
            relative = f"{days} days ago"
        elif delta.seconds >= 3600:
            relative = f"{delta.seconds // 3600} hours ago"
        elif delta.seconds >= 60:
            relative = f"{delta.seconds // 60} minutes ago"
        else:
            relative = "just now"

        absolute = self.last_updated.strftime("%Y-%m-%d")
        return f"{relative} ({absolute})"

