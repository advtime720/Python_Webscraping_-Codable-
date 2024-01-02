from pathlib import Path


def parse_temp():
    file_num = 0
    file_name = f"file{file_num}.csv"

    my_files = Path(f"{file_name}")
    while my_files.is_file():
        file_num += 1
        file_name = f"file{file_num}.csv"
        my_files = Path(f"{file_name}")

    with open("Web_scrape_team/scrape_history/temp.txt", "r") as src, open(f"{file_name}", "a") as dst:
        for car_data in src:
            dst.write(car_data)
