from dataclasses import dataclass

@dataclass
class AudioConfig:
  ENABLED: bool
  DEMO: bool
  VOLUME: int
  MEDIA: str