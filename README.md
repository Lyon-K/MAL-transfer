# Aniwave to MAL Transfer Tool

This Python program helps you transfer your anime watchlist from Aniwave.to to MyAnimeList (MAL). With Aniwave being shut down, this script extracts your saved anime titles and episodes from the HTML of your watch list on Aniwave and searches for the corresponding MAL pages. You can then manually save the entries on MAL to preserve your watchlist. This project does not condone using non-legal services, but rather assists in transferring your list to a legal platform.

## Features
- Parses the Aniwave watch-list HTML for anime titles and episodes.
- Automatically searches Google for the MyAnimeList (MAL) page of each anime.
- Opens the MAL page for easy saving.

## Setup

### 1. Create a Python environment
First, create a virtual environment for the project:
```bash
python -m venv venv
```

Activate the virtual environment:
- On macOS/Linux:
```bash
source venv/bin/activate
```
- On Windows:
```bash
venv\Scripts\activate
```

### 2. Install the requirements
Install the necessary Python packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Run the program
Run the main script to extract your watch-list data and open the corresponding MAL pages:
```bash
python main.py
```

The script will prompt you for the folder location of your saved Aniwave HTML watch list file. Once provided, it will extract the anime titles and episode numbers and then search and open the appropriate MAL pages.

## Usage Instructions
1. Save your watch-list page from [Aniwave.to](https://aniwave.to/user/watch-list) as 'mylist.html' in the project directory.
2. The program will display the anime titles and episodes from your watch-list.
3. It will automatically search and open the MyAnimeList (MAL) page for each anime, where you can save it to your MAL account.

## Disclaimer
This tool is meant to assist with the migration of watchlists from Aniwave to MyAnimeList due to Aniwave’s shutdown. We encourage users to use legal streaming services and platforms like MyAnimeList to manage their anime libraries.