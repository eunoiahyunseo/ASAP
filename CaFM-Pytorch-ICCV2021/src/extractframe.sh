#!/bin/bash

video_name=$1
category=$2
scale=$3 
TOTAL_FRAMES=$4 # 추출하고 싶은 프레임 수

ucf_dataset_path="/root/workspace/dataset/UCF-CRIME/"

video_dir="${ucf_dataset_path}video/"
hr_image_dir="${ucf_dataset_path}${category}/DIV2K_train_HR/"
prev_lr_image_dir="${ucf_dataset_path}${category}/DIV2K_train_LR_bicubic/"
lr_image_dir="${ucf_dataset_path}${category}/DIV2K_train_LR_bicubic/X${scale}/"
# fps="30"
video_path="$video_dir$video_name"

lr_video_format="%05dx$scale"
hr_video_format="%05d"

echo "${video_path}"

# category dir가 존재한다면 삭제하고 다시 만든다.
if [ -d "${ucf_dataset_path}${category}" ]; then
    rm -rf "${ucf_dataset_path}${category}"
fi

mkdir "${ucf_dataset_path}${category}"
mkdir "$hr_image_dir"
mkdir "$prev_lr_image_dir"
mkdir "$lr_image_dir"

DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $video_path)
DURATION=${DURATION%.*}  # 소수점 제거

FPS=$(echo "$TOTAL_FRAMES / $DURATION" | bc)

echo "$FPS"

# .../video/[].mp4에 있는 비디오 파일을 프레임 단위로 끊기
# .../[category]/DIV2K_train_HR에 포멧에 맞게 넣기
ffmpeg -i $video_path -vf "fps=$FPS" "$hr_image_dir$hr_video_format.png"

# .../[category]/DIV2K_train_LR_bicubic에 포맷에 맞게 변환해서 넣기
ffmpeg -i "$hr_image_dir$hr_video_format.png" -vf scale="iw/$scale:ih/$scale" -sws_flags bicubic "$lr_image_dir$lr_video_format.png"
