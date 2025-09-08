from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from house_rental.config import PROCESSED_DATA_DIR, RAW_DATA_DIR
import os
os.system('poetry update')
os.system('poetry install')
os.system('poetry lock')



# Get the absolute path to the project root
project_root = Path(__file__).resolve().parent.parent
processed_dir = project_root / 'data' / 'processed'
processed_dir.mkdir(parents=True, exist_ok=True)


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    import subprocess

    logger.info("Starting download of rental datasets to raw folder...")
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    files = [
        {
            "name": "rental_testing.csv",
            "id": "1aX6PkriH79qc88RHuJXeCulDfQniv8Wc"
        },
        {
            "name": "rental_training.csv",
            "id": "1bfoxO2SgYhs2660T3bI4kiU32HFwoMbj"
        },
        {
            "name": "rental_validation.csv",
            "id": "1RH7JOfa-N8Jz0udyeDBtNI4DHELdRwhu"
        }
    ]

    try:
        import gdown
    except ImportError:
        logger.info("gdown not found, installing...")
        subprocess.check_call(["pip", "install", "gdown"])
        import gdown

    for file in files:
        dest_path = RAW_DATA_DIR / file["name"]
        url = f"https://drive.google.com/uc?id={file['id']}"
        logger.info(f"Downloading {file['name']} from Google Drive...")
        try:
            gdown.download(url, str(dest_path), quiet=False)
            logger.success(f"Downloaded {file['name']} to {dest_path}")
        except Exception as e:
            logger.error(f"Failed to download {file['name']}: {e}")

    logger.success("All files downloaded to raw folder.")


if __name__ == "__main__":
    app()
