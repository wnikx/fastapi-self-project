from src.services.division import check_ceo_exist


async def test_check_ceo_exist(add_ceo_position, delete_ceo_position):
    ceo = await check_ceo_exist()

    assert ceo == False

    await add_ceo_position()
    assert ceo is not None

    await delete_ceo_position()
