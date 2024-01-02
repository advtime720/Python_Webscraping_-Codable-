from bs4 import BeautifulSoup
import requests

def build_url():
    default_address = "https://www.truecar.com/used-cars-for-sale/listings/"

    # Listing Options
    print("Best Match / Newly Listed / Best Deal / Lowest Price / Highest Price")
    list_option = (input("Enter listing option: ")).lower().replace(" ", "")
    print(" ")

    # Maker
    make = input("Enter Maker: ").lower().replace(" ", "-")
    print(" ")

    while(not valid_url(default_address, make)):
        make = input("Please enter a valid maker: ")
        print(" ")

    # Print available models
    soup = BeautifulSoup(requests.get(default_address + make + "/").text, 'lxml')
    options = soup.find("ul", "space-y-2 _j1kt73").find_all("li")

    model_options = []
    model_string = ""

    for option in options:
        model = option.find_next("a", href=True)['href'].split('/')[4]
        model_options.append(model)

    for i in range(len(model_options)):
        model_string += model_options[i]
        if i != len(model_options) - 1:
            model_string += ", "

    print("Popular models for " + make + ": " + model_string)

    model = input("Enter Model: ").lower().replace(" ", "-")
    print(" ")

    while (not valid_url(default_address + "/" + make + "/", model)):
        model = input("Please enter a valid model: ")
        print(" ")

    # Search Years
    yr_min = input("Enter years minimum: ")
    yr_max = input("Enter years maximum: ")
    print(" ")

    # Body Type
    body_type = input("Enter Body Style: ").lower().replace(" ", "")
    body_type_url_input = "body-" + body_type if body_type != "" else ""

    # Input validation
    yr_min_empty = yr_min == ""
    yr_max_empty = yr_max == ""

    if yr_min == yr_max:
        if yr_min == "":
            yr_max = ""
        yr_min = ""


    sort_options = {
        "bestmatch": "",
        "newlylisted": "?sort[]=created_date_desc",
        "bestdeal": "?sort[]=best_deal_desc_script",
        "lowestprice": "?sort[]=price_asc",
        "highestprice": "?sort[]=price_desc",
        "distance": "?sort[]=distance_asc_script",
        "lowestmileage": "?sort[]=mileage_asc",
        "highestmileage": "?sort[]=mileage_desc",
        "": ""
    }


    if yr_min_empty: return f"{default_address}{make}/{model}/year-min-{yr_max}/{body_type_url_input }/{sort_options[list_option]}"
    elif yr_max_empty: return f"{default_address}{make}/{model}/year-{yr_min}-max/{body_type_url_input }/{sort_options[list_option]}"

    return f"{default_address}{make}/{model}/year-{yr_min}-{yr_max}/{body_type_url_input}/{sort_options[list_option]}"


def valid_url(url, to_check):
    soup = BeautifulSoup(requests.get(url + to_check + "/").text, 'lxml')
    found = soup.find("span", "hidden md:block")

    return found == None
