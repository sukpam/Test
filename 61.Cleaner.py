import os
from datetime import datetime, timedelta

# 현재 스크립트가 실행되는 폴더의 상위 경로를 확인
current_folder = os.path.dirname(os.path.abspath(__file__))

# 로그 파일이 저장된 폴더 경로 설정 (상대 경로)
log_folder = os.path.join(current_folder, '00.Log')

# 이미지 파일이 저장된 폴더 경로 설정 (상대 경로)
image_folder = os.path.join(current_folder, '..', '07.Post', '00.IMG')

# 현재 날짜에서 14일 전 날짜 계산
cutoff_date = datetime.now() - timedelta(days=14)

# 로그 파일 처리
if os.path.exists(log_folder):
    for filename in os.listdir(log_folder):
        if filename.endswith("_log.txt"):  # 로그 파일에만 적용
            try:
                # 파일명에서 날짜와 시간을 추출 (예: 2024-09-03)
                date_str = filename.split("_")[0]
                file_date = datetime.strptime(date_str, "%Y-%m-%d")
                
                # 파일이 14일 이전이면 삭제
                if file_date < cutoff_date:
                    file_path = os.path.join(log_folder, filename)
                    os.remove(file_path)
                    print(f"삭제됨: {file_path}")
            except Exception as e:
                print(f"파일 처리 중 오류 발생 {filename}: {e}")
else:
    print(f"로그 폴더가 존재하지 않음: {log_folder}")

# 이미지 파일 처리
if os.path.exists(image_folder):
    for filename in os.listdir(image_folder):
        if filename.endswith((".png", ".jpg", ".jpeg", ".webp")):  # 이미지 파일에만 적용
            try:
                # 파일명에서 날짜를 추출 (예: 240908.webp)
                date_str = filename.split(".")[0]
                # 날짜 형식 변환
                file_date = datetime.strptime(date_str, "%y%m%d")
                
                # 파일이 14일 이전이면 삭제
                if file_date < cutoff_date:
                    file_path = os.path.join(image_folder, filename)
                    os.remove(file_path)
                    print(f"삭제됨: {file_path}")
            except Exception as e:
                print(f"파일 처리 중 오류 발생 {filename}: {e}")
else:
    print(f"이미지 폴더가 존재하지 않음: {image_folder}")
