import os
import shutil


folder_to_delete = 'C:/Users/Konrad/AppData/Local/Temp/.tensorboard-info'

if os.path.exists(folder_to_delete):
    shutil.rmtree(folder_to_delete)
    print(f'{folder_to_delete} deleted')