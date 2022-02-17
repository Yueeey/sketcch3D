from pathlib import Path

 p = Path('/vol/research/zy/dataSets/shapeMVD/Chair/hires/03001627')
folder_list = [x for x in p.iterdir() if x.is_dir()]