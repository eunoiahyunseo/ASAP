import cv2
import os

def frames_to_video(input_folder, output_video, fps):
    # Get the list of image files in the input folder
    frame_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    frame_files.sort()
    # print(frame_files)
    # Get the dimensions of the first image to set up the video writer
    img = cv2.imread(os.path.join(input_folder, frame_files[0]))
    height, width, _ = img.shape

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec as per your requirement
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    # Iterate through each frame and write to the video
    for frame_file in frame_files:
        frame_path = os.path.join(input_folder, frame_file)
        img = cv2.imread(frame_path)
        out.write(img)

    # Release the video writer
    out.release()
    print("Video created successfully!")

# Example usage
input_folder = "FastLLVE_SMID_Shooting7/images/output"
output_video = "FastLLVE_SMID_Shooting7.mp4"
fps = 30  # Frames per second
frames_to_video(input_folder, output_video, fps)
