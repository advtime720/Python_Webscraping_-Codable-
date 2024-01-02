import time
from cars_scrape import *
import webbrowser
import platform


if platform.system() == 'Windows':
    from plyer import notification
    def push_alarm_win(text):
        notification.notify(
            title="New Listing Found",
            message=text,
            timeout=5
                )
        return
else:
    import pync
    def push_alarm_mac(text):
        pync.notify(text, title='New Listing')



def get_vinlist(input_url):
    variables = input_url.split('/')
    make = variables[5]
    model = variables[6]

    target_site = requests.get(input_url).text
    soup = BeautifulSoup(target_site, 'lxml')
    # cars = soup.find_all("div", class_="linkable card card-shadow vehicle-card _1qd1muk")  # main block
    cars = soup.find_all("div", "vehicle-card-top")
    cars_price = soup.find_all("div", "heading-3 my-1 font-bold")
    cars_rating = soup.find_all("span", "graph-icon-title ml-1 vehicle-card-price-rating-label truncate font-bold")
    cars_url_raw = soup.find_all("a", "linkable vehicle-card-overlay order-2", href=True)
    cars_vin = []
    cars_url = []

    for i in range(len(cars_url_raw)):
        url = cars_url_raw[i]
        vin = cars_url_raw[i]['href'][28:45]

    
        cars_url.append(url)
        cars_vin.append(vin)

    return cars_vin



#####



def search_loop(url,time_hours, rep,openurl):
    count = 0
    vin_list = []
    base_message = "https://www.truecar.com/used-cars-for-sale/listing/"

    new_vin = []
    dup = []
    for i in range(0,rep):
        if i == 0:
            vin_list.append(get_vinlist(url))
        else:
            vin_list.append(get_vinlist(url))
            new_vin += get_vinlist(url)
            
            for vin in new_vin:
                for vin_rep in vin_list[:i]:                    
                    if (vin in vin_rep) and (vin in new_vin):                        
                        dup.append(vin)
            for trash in dup:
                if trash in new_vin:
                    new_vin.remove(trash)   
                                                
            for new in new_vin:
                print(f"{base_message}{new}")
                if openurl == 'True':
                            webbrowser.open(f"{base_message}{new}")
        
        time.sleep(time_hours * 3600)   


def search_loop_demo(time_hours, rep,openurl):
    count = 0
    vin_list = []
    base_message = "https://www.truecar.com/used-cars-for-sale/listing/"

    new_vin = []
    dup = []
    for i in range(0,rep):
        url = build_url()
        if i == 0:
            vin_list.append(get_vinlist(url))
        else:
            vin_list.append(get_vinlist(url))
            new_vin += get_vinlist(url)
            
            for vin in new_vin:
                for vin_rep in vin_list[:i]:                    
                    if (vin in vin_rep) and (vin in new_vin):                        
                        dup.append(vin)
            for trash in dup:
                if trash in new_vin:
                    new_vin.remove(trash)   
                                                
            for new in new_vin:
                print(f"{base_message}{new}")
                if openurl == 'True':
                            webbrowser.open(f"{base_message}{new}")
        
        time.sleep(time_hours * 3600) 
