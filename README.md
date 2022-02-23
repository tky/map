docker-compose build

http://localhost:8000/docs


$ psql -h localhost -Upostgres -p25432

postgres=# create database maps;
maps=# \c maps;
maps=# create extension postgis;
CREATE EXTENSION
maps=# create extension postgis_topology;
CREATE EXTENSION

CREATE TABLE geometries (
    id character varying NOT NULL,
    geo_point geometry(Point,4326),
    geo_polygon geometry(Polygon,4326)
);

CREATE INDEX geometries_geo_point on geometries USING Gist (geo_point);
CREATE INDEX geometries_geo_polygon on geometries USING Gist (geo_polygon);
CREATE INDEX geometries_geography ON geometries USING gist( (geo_polygon::geography) );
