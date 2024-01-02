import os
import re
from url import  *


def get_info(input_url):
    # Retrieving variables from the url
    open("Web_scrape_team/scrape_history/temp.txt", "w") 
    print(input_url)
    variables = input_url.split('/')
    make = variables[5]
    modified_make = make.replace('-', ' ')
    model = variables[6]
    modified_model = model.replace('-', ' ')

    target_site = requests.get(input_url).text
    soup = BeautifulSoup(target_site, 'lxml')
    cars = soup.find_all("div", "vehicle-card-top")
    cars_url_raw = soup.find_all("a", "linkable vehicle-card-overlay order-2", href=True)
    cars_vin = []
    cars_url = []

    for i in range(len(cars_url_raw)):
        url = cars_url_raw[i]
        vin = cars_url_raw[i]['href'][28:45]

        if vin not in cars_vin:
            cars_url.append(url)
            cars_vin.append(vin)

    # Return how many listings were found
    count = 0
    found_count = 0
    listing = soup.find("span", class_="hidden-sm-down")

    if listing is not None:
        num_list = re.findall(r'\b\d+\b', listing.text)
        found_count = num_list[len(num_list) - 1]
        print("Found " + found_count + " listings")

    # Print the founding
    for index in range(len(cars)):
        # URL making
        url = "https://truecar.com/used-cars-for-sale/listing/" + cars_vin[index]

        base_show_condition = cars[index].text.lower().find(modified_make) != -1 and cars[index].text.lower().find(
            modified_model) != -1 and listing is not None

        if base_show_condition:
            scrape_data = (str(index+1) + ".\t" + cars_url[index]['aria-label'][17:] + "\t" + url)
            print(str(index+1) + ".\t" + cars_url[index]['aria-label'][17:] + "\t" + url)
            count += 1
           
        ### file saver ###
            with open("Web_scrape_team/scrape_history/temp.txt", "a") as f:
                f.write(scrape_data)
                f.write("\n")
        ### file saver ###

    if count < int(found_count):
        print("Getting next page")
        get_info_next_page(input_url, count, 2)

    if count == 0: print("Listing not found")


def get_info_next_page(input_url, start_count, page):
    # Retrieving variables from the url
    # print(input_url + "?page=" + str(page))
    variables = input_url.split('/')
    make = variables[5]
    model = variables[6]
    modified_make = make.replace('-', ' ')
    modified_model = model.replace('-', ' ')

    target_site = requests.get(input_url + "?page=" + str(page)).text
    soup = BeautifulSoup(target_site, 'lxml')
    cars = soup.find_all("div", "vehicle-card-top")
    cars_url_raw = soup.find_all("a", "linkable vehicle-card-overlay order-2", href=True)
    cars_vin = []
    cars_url = []

    for i in range(len(cars_url_raw)):
        url = cars_url_raw[i]
        vin = cars_url_raw[i]['href'][28:45]

        if vin not in cars_vin:
            cars_url.append(url)
            cars_vin.append(vin)

    # Return how many listings were found
    count = start_count + 1
    count_to_pass = 0
    listing = soup.find("span", class_="hidden-sm-down")
    found_count = 0

    if listing is not None:
        num_list = re.findall(r'\b\d+\b', listing.text)
        found_count = num_list[len(num_list) - 1]

    # Print the founding
    for index in range(len(cars)):
        # URL making
        url = "https://truecar.com/used-cars-for-sale/listing/" + cars_vin[index]

        base_show_condition = cars[index].text.lower().find(modified_make) != -1 and cars[index].text.lower().find(
            modified_model) != -1 and listing is not None

        if base_show_condition:
            scrape_data = (str(index+count) + ".\t" + cars_url[index]['aria-label'][17:] + "\t" + url)
            print(str(index+count) + ".\t" + cars_url[index]['aria-label'][17:] + "\t" + url)
            count_to_pass = index+count
        
        ### file saver ###
            with open("Web_scrape_team/scrape_history/temp.txt", "a") as f:
                f.write(scrape_data)
                f.write("\n")
        ### file saver ###


    if count_to_pass < int(found_count):
        print("Getting page " + str(page+1))
        get_info_next_page(input_url, count_to_pass, page + 1)

    if count == 0: print("Listing not found")
