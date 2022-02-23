from pydantic import BaseModel
from typing import List, Tuple, Dict


class Geometry(BaseModel):
    type: str
    coordinates: List[Tuple[float, float]]


class Feature(BaseModel):
    type: str
    properties: Dict[str, str]
    geometry: Geometry


class GeoJson(BaseModel):
    type: str
    features: list[Feature]
