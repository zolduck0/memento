wine ./drive_c/users/zolduck/AppData/Local/Programs/Python/Python312/python.exe -m PyInstaller --onefile \
  --add-data "assets:assets" \
  --add-binary "/usr/lib/x86_64-linux-gnu/libpython3.12.so.1.0:." \
  --hidden-import=PIL._tkinter_finder \
  memento.py