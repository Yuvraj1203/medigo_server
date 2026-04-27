from medigo_server.schemas import Category_Dto, ResponseModel

async def add_category(category_model:Category_Dto) -> ResponseModel:
    return ResponseModel(
        result={"please add to db"},
        message="rn you are doing tp"
    )
