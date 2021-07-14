import os

path='/home/abnormal_detection/VuNgocTu/dataset/subway/testing/frames/02'
for fi in os.listdir(path):
  src=os.path.join(path,fi)
  fi_new=int(fi[:-4])
  fi_new=fi_new-50001

  des=os.path.join(path,str(fi_new).zfill(7)+'.jpg')
  os.rename(src, des) 