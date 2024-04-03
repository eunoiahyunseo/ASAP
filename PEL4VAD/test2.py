import numpy as np

# res = np.load('/root/workspace/PEL4VAD/list/ucf/single_gt/Explosion036_x264__9_gt.npy')
# res2 = np.load('/root/workspace/dataset/UCF-CRIME/video/feat/ucf-i3d/Shooting005_x264.npy')
# print(res, res.shape)
# print(res2, res2.shape)

# res3 = np.load('./Shooting005_x264_gt.npy')
# print(res, res.shape)

a = np.zeros(1199)
a = np.concatenate((a, [1]))
print(a.shape)
np.save('./Shooting002_x264__gt_9', a)