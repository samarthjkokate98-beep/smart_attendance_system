"""
Script to download OpenCV YuNet (Face Detection) and SFace (Face Recognition) ONNX models.
"""
import os
import sys
import urllib.request

MODELS_DIR = os.path.dirname(os.path.abspath(__file__))

MODELS = {
    "face_detection_yunet_2023mar.onnx": "https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx",
    "face_recognition_sface_2021dec.onnx": "https://github.com/opencv/opencv_zoo/raw/main/models/face_recognition_sface/face_recognition_sface_2021dec.onnx",
}

def download_file(url: str, dest_path: str):
    print(f"Downloading {os.path.basename(dest_path)} from {url}...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as response, open(dest_path, "wb") as out_file:
        total_size = response.getheader("Content-Length")
        total_size = int(total_size) if total_size else None
        downloaded = 0
        chunk_size = 65536
        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break
            out_file.write(chunk)
            downloaded += len(chunk)
            if total_size:
                percent = downloaded * 100 / total_size
                sys.stdout.write(f"\r  Progress: {downloaded / (1024 * 1024):.2f}MB / {total_size / (1024 * 1024):.2f}MB ({percent:.1f}%)")
                sys.stdout.flush()
            else:
                sys.stdout.write(f"\r  Progress: {downloaded / (1024 * 1024):.2f}MB")
                sys.stdout.flush()
    print("\nDownload completed successfully.")

def ensure_models():
    os.makedirs(MODELS_DIR, exist_ok=True)
    all_ok = True
    for filename, url in MODELS.items():
        dest = os.path.join(MODELS_DIR, filename)
        if not os.path.exists(dest) or os.path.getsize(dest) < 1000:
            try:
                download_file(url, dest)
            except Exception as e:
                print(f"Warning: Failed to download {filename}: {e}")
                all_ok = False
        else:
            print(f"Model already present: {filename} ({os.path.getsize(dest) / (1024*1024):.2f} MB)")
    return all_ok

if __name__ == "__main__":
    ensure_models()
