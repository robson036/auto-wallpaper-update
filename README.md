# AUTO WALLPAPER UPDATER FOR LINUX

Created with the purpose of helping me with my laziness to change my PC wallpaper

## USAGE

- git clone this repo
- bash `crontab -e`
- create a crontab config to run the python script as you wish
  - Ex: 0 10 \* \* \* python3 /home/USER/repo/wallpapers.py (will download and define a new wallpaper every day at 10am)
