
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

STEPS = [
    "extract.py",
    "transform.py",
    "load.py",
    "analysis.py",
]


def run_pipeline():
    print("Starting SA Employment Insights pipeline...")

    for script in STEPS:
        script_path = BASE_DIR / "src" / script

        print(f"\nRunning {script}...", flush=True)

        subprocess.run(
            [sys.executable, str(script_path)],
            cwd=BASE_DIR,
            check=True,
        )

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
