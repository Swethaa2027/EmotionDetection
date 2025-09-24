from src import download_data, data_processing, split, visualize


def main():
    # Step 1: Download dataset
    competition = "challenges-in-representation-learning-facial-expression-recognition-challenge"
    download_dir = "./facial_expression_dataset"
    download_data.pipeline(competition, download_dir)

    # Step 2: Process dataset (resize, normalize, rotate)
    processed_dir = "./processed_dataset"
    data_processing.process_images(download_dir, processed_dir, img_size=(48, 48))

    # Step 3: Split dataset
    split.split_dataset(processed_dir, output_dir="./dataset_splits")

    # Step 4: Visualize data distribution
    visualize.plot_emotion_histogram("./dataset_splits/train")


if __name__ == "__main__":
    main()

