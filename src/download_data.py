import os
import zipfile
import subprocess


def install_kaggle():
    """Ensure Kaggle API is installed."""
    try:
        import kaggle  # noqa: F401
    except ImportError:
        raise ImportError("Please install Kaggle API with 'pip install kaggle'")


def download_dataset(competition: str, download_dir: str):
    """Download dataset from Kaggle competition."""
    os.makedirs(download_dir, exist_ok=True)

    # Use subprocess so we can capture errors
    result = subprocess.run(
        ["kaggle", "competitions", "download", "-c", competition, "-p", download_dir],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Error downloading dataset: {result.stderr}")

    print(f"✅ Download complete. Files saved in {download_dir}")


def extract_files(download_dir: str):
    """Extract any zip files inside the download directory."""
    for file in os.listdir(download_dir):
        if file.endswith(".zip"):
            file_path = os.path.join(download_dir, file)
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(download_dir)
            print(f"📂 Extracted {file}")


def main():
    """Run the download + extraction pipeline."""
    install_kaggle()

    competition = "challenges-in-representation-learning-facial-expression-recognition-challenge"
    download_dir = "./facial_expression_dataset"

    download_dataset(competition, download_dir)
    extract_files(download_dir)


if __name__ == "__main__":
    main()

