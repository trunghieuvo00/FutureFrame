import numpy as np
from scipy.io import savemat

arr=np.zeros((2,), dtype=np.object)
arr[0]=  np.array([[27912, 29728 ,39465],[27991, 29760 ,39510]],dtype=np.uint32)
arr[1]= np.array([[67695  ,67830 ,69234  ,69600  , 69700   ,73003   ,73689   ,73710  ,83430   ,
84330  , 85767  ,86384  ,88498  ,89623 ,95285  ,
96698 , 100096  ,115458  ,115655  ,117566 ,117716  ,
118225 , 118655  ,119269  ,124666  ,128010 ,130414 ],
[67768  ,67910 ,69320  ,69956  , 70018   ,73070   ,73867   ,74042  ,83515   ,
84407  , 85877  ,86554  ,88650  ,89806 ,95389  ,
96754 , 100396  ,115490  ,115697  ,117613 ,117901  ,
118268 , 119089  ,119302  ,124820  ,128099 ,130665 ]],dtype=np.uint32)
print(arr[1].shape)
for i in range(len(arr[0])):
  arr[0][i]=arr[0][i]-20000

for i in range(len(arr[1])):
  arr[1][i]=arr[1][i]-50000

savemat("subway.mat", mdict={'gt':arr})
from scipy.io import loadmat
annots = loadmat('subway.mat')
print(annots)