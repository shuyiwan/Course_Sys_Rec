import os
import sys

PROJECT_PATH = os.getcwd()

SEARCH_PATH = os.path.join(
    PROJECT_PATH, "backend\search"
)
sys.path.append(SEARCH_PATH)

SHOPPINGCART_PATH = os.path.join(
    PROJECT_PATH, "backend\shoppingCart"
)
sys.path.append(SHOPPINGCART_PATH)
