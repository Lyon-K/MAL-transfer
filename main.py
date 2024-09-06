from bs4 import BeautifulSoup
from googlesearch import search
import webbrowser
from time import sleep

batch_size = 1
num_skips = 254
search_interval = 0.15


def fetch_website(query, limit=1):
    try:
        # Perform the Google search
        return next(search(query, num_results=limit, sleep_interval=5, advanced=False))
    except Exception as e:
        print("An error occurred when searching for :", query)
        # print("An error occurred:", str(e))
        raise e


def create_tab(link):
    return webbrowser.get(
        "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    ).open(link)


if __name__ == "__main__":
    html_doc = None
    with open("mylist.html", "r") as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, "html.parser")

    my_list = soup.find("div", {"class": "watchlist"}).find_all(
        "div", {"class": "item"}
    )

    my_folders = {}
    for item in my_list:
        folder_name = item.find("span", {"class": "folder-name"}).get_text()
        title = item.find("a", {"class": "d-title"})
        try:
            ep = (
                item.find("div", {"class": "ep"})
                .find("span", {"class": "current"})
                .get_text()
                .strip()
            )
        except:
            ep = None

        if my_folders.get(folder_name) == None:
            my_folders[folder_name] = []
        my_folders.get(folder_name).append(
            {
                "title": title["data-jp"] or title.get_text(),
                "ep": ep,
            }
        )

    current = 0
    for folder in my_folders:
        print(f"FOLDER: {folder}")
        counter = batch_size
        for anime in my_folders[folder]:
            current += 1
            if current < num_skips:
                print(f"Skipped: {anime['title']}")
                continue
            query = f"myanimelist.net/anime {anime['title']}"
            print(f"{current}:")
            print("title:", anime["title"])
            print("ep:", anime["ep"])
            try:
                website = fetch_website(query=query)
                print("Opening:", website, "\n")
                create_tab(website)
            except:
                print("Instead Googling:", query, "\n")
                create_tab("https://www.google.com/search?q=" + query)
                sleep(search_interval)
            counter -= 1
            if counter == 0:
                input(f"Press Enter for next {batch_size}.\n\n")
                counter = batch_size
        if current < num_skips:
            continue
        input("Press Enter for next folder.\n\n")
    print("No more folders\nExiting...")
