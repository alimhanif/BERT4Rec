import argparse

import pandas as pd
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    "--data_dir", default=None, help="Directory containing sequence data."
)
parser.add_argument(
    "--output_file", default=None, help="Output_file."
)

def write_row(row, file):
    for item in row["product_sequence"]:
        r = str(row["customer_id"]) + " " + str(item)
        file.write(r + os.linesep)

def write_file(input_file, output_file):
    df = pd.read_csv(input_file)
    df["product_sequence"] = df["product_sequence"].apply(lambda x : x.split(","))
    with open(output_file, "a") as f:
        for index, row in df.iterrows():
            write_row(row, f)

def write_all(input_pattern, output_file):
    input_paths = glob.glob(input_pattern)
    for i, file in enumerate(input_paths):
        write_file(file, output_file)
        print("File %d done!" % (i+1))

def main():
    args = parser.parse_args()

    DATA_DIR = args.data_dir
    OUTPUT_FILE = args.output_file
    
    if os.path.isfile(OUTPUT_FILE):
        print("WARNING : Output file exist! Will be replaced!")
        os.remove(OUTPUT_FILE)
    
    input_pattern = os.path.join(DATA_DIR, "*.csv")
    print("start!")
    write_all(input_pattern, OUTPUT_FILE)
    print("done!")

if __name__ == "__main__":
    main()