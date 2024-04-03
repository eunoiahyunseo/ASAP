import cv2
import os

def frames_to_video(input_path, output_path, fps):
    """
    이미지 프레임을 동영상으로 변환하는 함수입니다.
    
    Args:
    input_path (str): 이미지 프레임이 저장된 폴더의 경로입니다.
    output_path (str): 생성될 동영상 파일의 경로입니다.
    fps (int): 출력 비디오의 프레임레이트입니다.
    """
    image_files = [os.path.join(input_path, img) for img in os.listdir(input_path) if img.endswith(".png")]
    print(f'image_files: {image_files}')
    image_files.sort()  # 파일 이름 순서대로 정렬

    # 첫 번째 이미지로부터 비디오 해상도 가져오기
    frame = cv2.imread(image_files[0])
    height, width, layers = frame.shape

    # 비디오 writer 정의
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # mp4 포맷으로 저장
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    # print('fuck', cv2.imread(image_files[0]))
    for image_file in image_files:
        video.write(cv2.imread(image_file))

    cv2.destroyAllWindows()
    video.release()

# 함수 사용 예시
video_name = 'CaFM-downscaled-x2-Shooting002-Org.mp4'
# input_path = '/root/workspace/CaFM-Pytorch-ICCV2021/experiment/test/results-DIV2K'
input_path = '/root/workspace/dataset/UCF-CRIME/Shooting/DIV2K_train_LR_bicubic/X2'
output_path = '/root/workspace/demo/CaFM/' + video_name
fps = 30  # 초당 프레임 수

frames_to_video(input_path, output_path, fps)
