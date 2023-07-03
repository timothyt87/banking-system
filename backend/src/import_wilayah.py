import csv
from core.database_mongodb import mongodb
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from configurations.settings import Settings
import re


async def get_collection(collection_name: str):
    conn: AsyncIOMotorClient = mongodb.get_connection()
    database: AsyncIOMotorDatabase = conn[Settings.DATABASE_NAME]
    collections = database[collection_name]
    return collections


async def insert_data_to_db():
    wilayah_collections = await get_collection('wilayah')
    with open('/home/banana/Projects/banking-system/backend/src/wilayah.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        wilayah = []

        for row in reader:
            _wilayah = {
                'kode': row['kode'],
                'nama': row['nama']
            }
            wilayah.append(_wilayah)

        data_wilayah = []

        for wil in wilayah:
            # Search Provinsi
            re_search_provinsi = re.compile(r'^[0-9].$')
            if re_search_provinsi.match(wil['kode']):
                data_wilayah.append(wil)

        for prov in data_wilayah:
            kode_prov = prov['kode']
            re_search_kab_kota = re.compile(fr'^{kode_prov}\.[0-9].$')

            kab_kota = []

            # Search Kabupaten / Kota
            for wil in wilayah:
                if re_search_kab_kota.match(wil['kode']):
                    kab_kota.append(wil)

            # input data kab/kota ke data_wilayah
            prov['kabupaten_kota'] = kab_kota

        for prov in data_wilayah:
            for _kab_kota in prov['kabupaten_kota']:
                kode_kab_kota: str = _kab_kota['kode']
                kode_kab_kota = kode_kab_kota.replace('.', '\\.')
                re_search_kecamatan = re.compile(fr'^{kode_kab_kota}.\.[0-9].$')

                for wil in wilayah:
                    # print(wil['kode'])
                    if re_search_kecamatan.match(wil['kode']):
                        print(_kab_kota)
    # print(data_wilayah)


async def main():
    await asyncio.create_task(insert_data_to_db())


if __name__ == '__main__':
    asyncio.run(main())
