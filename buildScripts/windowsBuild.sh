wine ~/.wine/drive_c/users/zolduck/AppData/Local/Programs/Python/Python312/python.exe -m PyInstaller --onefile \
  --add-data "assets:assets" \
  --hidden-import=PIL \
  --hidden-import=PIL._tkinter_finder \
  memento.py
