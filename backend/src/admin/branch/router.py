from bson import BSON
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from starlette import status
from core.database_mongodb import mongodb
from .schemas import CreateNewBranch, NewBranchCreated, create_new_branch_responses
from .service import insert_new_branch

branch_router = APIRouter(
    prefix='/branch'
)


@branch_router.get(
    path='/',
    tags=['admin', 'branch'],
    description='GET cabang'
)
async def get_branch():
    return 'OK'


@branch_router.post(
    path='/',
    tags=['admin', 'branch'],
    response_model=NewBranchCreated,
    responses=create_new_branch_responses
)
async def create_new_branch(branch_data: CreateNewBranch):
    _id = await insert_new_branch(branch_data.dict())

    response_data: dict = {}

    if _id is not None:
        response_data['status'] = status.HTTP_201_CREATED
        response_data['message'] = "Branch Created"
        return JSONResponse(
            content=response_data,
            status_code=status.HTTP_201_CREATED
        )
    else:
        response_data['status'] = status.HTTP_400_BAD_REQUEST
        response_data['message'] = "Branch Already Exists"
        return JSONResponse(
            content=response_data,
            status_code=status.HTTP_400_BAD_REQUEST
        )


@branch_router.get(
    path='/wilayah',
    tags=['admin', 'wilayah']
)
async def get_list_provinsi(
        provinsi: str = None,
        kabupaten: str = None,
        kota: str = None,
        kecamatan: str = None,
        kelurahan: str = None,
        desa: str = None
):
    wilayah_collection = await mongodb.get_collection('wilayah')
    search_query_construct: str = ''

    if provinsi is None \
            and (kabupaten is None or kota is None) \
            and kecamatan is None \
            and (kelurahan is None or desa is None):
        cursor = wilayah_collection.find(
            {
                'kode': {
                    '$regex': '^[0-9].$'
                },
            },
            {
                '_id': 0
            }
        )
    else:
        if provinsi is not None:
            search_query_construct = '^'
            search_query_construct = search_query_construct + provinsi
            search_query_construct = search_query_construct + '\\.[0-9].$'

        if kabupaten is not None or kota is not None:
            search_query_construct = '^'
            if kabupaten is not None:
                search_query_construct = search_query_construct + kabupaten
            else:
                search_query_construct = search_query_construct + kota
            search_query_construct = search_query_construct + '\\.[0-9].$'

        if kecamatan is not None:
            search_query_construct = '^'
            search_query_construct = search_query_construct + kecamatan
            search_query_construct = search_query_construct + '.+$'

        if kelurahan is not None or desa is not None:
            search_query_construct = '^'
            if kelurahan is not None:
                search_query_construct = search_query_construct + kelurahan
            else:
                search_query_construct = search_query_construct + desa

        cursor = wilayah_collection.find(
            {
                'kode': {
                    '$regex': search_query_construct
                },
            },
            {
                '_id': 0
            }
        )
    result = await cursor.to_list(length=None)
    return result
