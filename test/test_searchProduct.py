import pytest
from src.pages.searchProduct_page import SearchProduct
from utils.config import CONFIG
from utils.data_reader import read_excel_data


# @pytest.mark.parametrize(
#     "search_box, category, price_range",  # The parameter names
#     zip(  # Combine the columns from the sheet into one tuple per test run
#         *[read_excel_data(CONFIG["test_data_file"], "SearchItem1", col) for col in ["search_box", "category", "price_range"]]
#     )
# )

@pytest.mark.parametrize("search_box", read_excel_data(CONFIG["test_data_file"], "SearchItem1", "search_box"))
def test_searchProduct(setup, search_box):
    driver = setup
    searchProduct_page = SearchProduct(driver)
    searchProduct_page.open_page(CONFIG["base_url"])
    # Method call Here
    searchProduct_page.search(search_box)



