#!/bin/bash

SCALE=2
FPS=30
CUDA_VISIBLE_DEVICES=0 python main.py --data_test DIV2K --scale $SCALE --model EDSR --test_only --save_results --pre_train /root/workspace/CaFM-Pytorch-ICCV2021/experiment/EDSR_X4_explosion_45s_1_M1-n/model/model_best.pt  --data_range 1-1005 --is45s --cafm  --dir_data /root/workspace/dataset/UCF-CRIME/Shooting --use_cafm --segnum 9
# ffmpeg -framerate ${FPS} -i "/root/workspace/CaFM-Pytorch-ICCV2021/experiment/test/results-DIV2K/%05d_x${SCALE}_SR.png" -c:v mpeg4 -pix_fmt yuv420p /root/workspace/CaFM-Pytorch-ICCV2021/experiment/test/output_video.mp4
# /root/workspace/dataset/UCF-CRIME/explosion_v2/DIV2K_train_HR