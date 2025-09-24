import os
import matplotlib.pyplot as plt
from collections import Counter


def plot_emotion_histogram(data_dir: str):
    """
    Plot histogram of emotion counts in dataset.
    Assumes structure: data_dir/class_name/*.jpg
    """
    counts = Counter()

    for class_name in os.listdir(data_dir):
        class_dir = os.path.join(data_dir, class_name)
        if os.path.isdir(class_dir):
            n_files = len(os.listdir(class_dir))
            counts[class_name] += n_files

    plt.figure(figsize=(8, 6))
    plt.bar(counts.keys(), counts.values(), color="skyblue", edgecolor="black")
    plt.xlabel("Emotion")
    plt.ylabel("Count")
    plt.title("Emotion Distribution")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
