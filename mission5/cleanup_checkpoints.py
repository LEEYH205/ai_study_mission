import glob, re, os
import argparse

parser = argparse.ArgumentParser(
    description="Delete checkpoint files, keeping only the one with lowest validation loss"
)
parser.add_argument(
    "prefix",
    help="Checkpoint filename prefix (e.g., 'convAE_best_model_epoch')"
)
args = parser.parse_args()

# 1) 체크포인트 목록 가져오기
files = glob.glob(f"{args.prefix}*.pth")

# 2) 파일명에서 val 값(손실) 추출하고, 가장 작은 값 파일 찾기
best_file = min(
    files,
    key=lambda f: float(re.search(r'val([0-9]+\.[0-9]+)', f).group(1))
)

print("Keeping:", best_file)

# 3) 나머지 파일 삭제
for f in files:
    if f != best_file:
        os.remove(f)
        print("Deleted:", f)