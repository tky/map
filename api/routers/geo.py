from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.geo as schema
from api.db import get_db

router = APIRouter()


@router.get("/geojson/{key_code}", response_model=schema.GeoJson)
async def geo(key_code: str, db: AsyncSession = Depends(get_db)):
    ret = await db.execute(
            """select
            id
            , ST_AsText(geo_polygon) as polygon
            from geometries where id = :key_code""", {'key_code': key_code})
    row = ret.fetchone()

    def _conv(v: str):
        lng, lat = v.split(' ')
        return (float(lng), float(lat))

    coordinates = [_conv(x) for x in row['polygon'][9:-2].split(',')]

    geometry = schema.Geometry(type='Polygon', coordinates=coordinates)
    properties = {"key_code": row['id']}
    feature = schema.Feature(type='Feature', geometry=geometry, properties=properties) # noqa

    return schema.GeoJson(type='FeatureCollection', features=[feature])
