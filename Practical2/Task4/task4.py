import json
import pickle

def update_price(product, price_info):
    method = price_info["method"]
    if method == "sum":
        product["price"] += price_info["param"]
    elif method == "sub":
        product["price"] -= price_info["param"]
    elif method == "percent+":
        product["price"] *= (1 + price_info["param"])
    elif method == "percent-":
        product["price"] *= (1 - price_info["param"])
    # округлим цены до двух знаков
    product["price"] = round(product["price"], 2)


with open("products_77.pkl", "rb") as f:
    products = pickle.load(f)

with open("price_info_77.json") as f:
    price_info = json.load(f)

price_info_dict = dict()

for item in price_info:
    price_info_dict[item["name"]] = item

for product in products:
    current_price_info = price_info_dict[product["name"]]
    update_price(product, current_price_info)

with open("products_updated.pkl", "wb") as f:
    f.write(pickle.dumps(products))
