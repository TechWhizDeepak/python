from pathlib import Path
import os 

filename = Path("D:\\test\\1\\wqdataid61238874.biasnew.err")

print(filename.name)
# prints "raw_data.txt"

print(filename.suffix)
# prints "txt"

print(filename.stem)
# prints "raw_data"

if not filename.exists():
    print("Oops, file doesn't exist!")
else:
    print("Yay, the file exists!")



for f_name in os.listdir('D:\\test\\1\\'):
 if f_name.endswith('.biasnew.err'):
    print(f_name)