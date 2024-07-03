create schema if not exists minio.raw
with (location = 's3a://raw/')


create table if not exists minio.raw.testeV1(
	Name VARCHAR, 
	Age Int 
)
with(
	external_location = 's3a://raw/testev2.parquet',
	format = 'PARQUET'
)


select * from minio.raw.testeV1

