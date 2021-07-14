import os

path='/home/abnormal_detection/Hieu_Toan/ano_pred_cvpr2018/Data/traffic-train/testing/frames/04/'
for fi in os.listdir(path):
  src=os.path.join(path,fi)
  fi_new=int(fi[:-4])
  #fi_new=fi_new - 4645
  #fi_new=fi_new - 5529
  #fi_new=fi_new - 12788
  fi_new=fi_new - 15868

  des=os.path.join(path,str(fi_new)+'.jpg')
  os.rename(src, des) 