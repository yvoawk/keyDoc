from utils.utils import *
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Keyword Detection in PDF and Word Documents')
    parser.add_argument('keywords_file', type=str, help='Path to the text file containing keywords')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing PDF and Word documents')
    parser.add_argument('output_csv', type=str, help='Path to save the output CSV file')
    
    args = parser.parse_args()
    
    # Run the keyword detection function
    find_keywords_in_documents(args.keywords_file, args.folder_path, args.output_csv)

if __name__ == "__main__":
    main()