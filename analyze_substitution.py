import os
import sys
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

def analyze_substitution_cipher(file_path, output_folder):
    """Analyzes a substitution cipher file and generates character frequency statistics."""
    with open(file_path, "r", encoding="latin1") as file:
        text = file.read()

    # Count character frequency
    char_counts = Counter(text)
    total_chars = sum(char_counts.values())

    # Sort by frequency
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    # Generate histogram
    plt.figure(figsize=(12, 6))
    plt.bar([char for char, _ in sorted_chars], [count for _, count in sorted_chars])
    plt.xlabel("Character")
    plt.ylabel("Frequency")
    plt.title(f"Character Frequency in {os.path.basename(file_path)}")
    plt.xticks(rotation=90)
    
    # Save histogram
    histogram_path = os.path.join(output_folder, f"{os.path.basename(file_path)}_histogram.png")
    plt.savefig(histogram_path)
    plt.close()

    # Generate report
    report_path = os.path.join(output_folder, f"{os.path.basename(file_path)}_report.txt")
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(f"Character Frequency Analysis for {os.path.basename(file_path)}\n")
        report_file.write("=" * 50 + "\n")
        report_file.write(f"Total Characters: {total_chars}\n\n")
        report_file.write("Character | Count | Percentage\n")
        report_file.write("-" * 30 + "\n")
        for char, count in sorted_chars:
            percentage = (count / total_chars) * 100
            report_file.write(f"  {repr(char)}  |  {count}  |  {percentage:.2f}%\n")

    print(f"📊 Analysis completed for {file_path}. Histogram and report saved in {output_folder}.")

def process_folder(input_folder):
    """Processes all text files in the given folder and analyzes them."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_folder = os.path.join("logs", "sub", timestamp)
    os.makedirs(output_folder, exist_ok=True)

    files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

    if not files:
        print("❌ No text files found in the specified folder.")
        return

    for filename in files:
        file_path = os.path.join(input_folder, filename)
        analyze_substitution_cipher(file_path, output_folder)

    print(f"\n✅ All analyses completed. Reports and histograms saved in {output_folder}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_substitution.py <input_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    if not os.path.exists(input_folder):
        print(f"❌ Error: Folder '{input_folder}' does not exist.")
        sys.exit(1)

    process_folder(input_folder)
