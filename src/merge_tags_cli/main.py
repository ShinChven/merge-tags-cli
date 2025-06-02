import argparse
import os
from pathlib import Path
import sys

def read_tags_from_file(file_path: Path) -> set[str]:
    """Reads tags from a single text file."""
    tags = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                # Split by comma, strip whitespace from each tag, and filter out empty tags
                tags.update(tag.strip() for tag in content.split(',') if tag.strip())
    except IOError as e:
        print(f"Warning: Could not read file {file_path}: {e}", file=sys.stderr)
    return tags

def merge_tags_in_directory(directory_path: Path, output_file_path: Path) -> None:
    """
    Reads all .txt files in a directory, merges unique tags,
    and writes them sorted to an output file.
    """
    all_tags = set()

    if not directory_path.is_dir():
        print(f"Error: Input directory not found: {directory_path}", file=sys.stderr)
        sys.exit(1)

    processed_any_txt_files = False
    for item in directory_path.iterdir():
        if item.is_file() and item.suffix.lower() == '.txt':
            processed_any_txt_files = True
            print(f"Processing file: {item}")
            file_tags = read_tags_from_file(item)
            all_tags.update(file_tags)

    if not processed_any_txt_files:
        print(f"No .txt files found in directory: {directory_path}", file=sys.stderr)

    if not all_tags and processed_any_txt_files:
        print("No tags found in the processed .txt files.", file=sys.stderr)
    elif not all_tags and not processed_any_txt_files:
        # This case is already handled by "No .txt files found..."
        pass

    try:
        # Ensure the output directory exists
        output_file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(", ".join(sorted(list(all_tags)))) # Sort for consistent output
        print(f"Successfully merged tags into: {output_file_path}")
    except IOError as e:
        print(f"Error: Could not write to output file {output_file_path}: {e}", file=sys.stderr)
        sys.exit(1)

def main_cli():
    parser = argparse.ArgumentParser(description="Merge tags from .txt files in a directory.")
    parser.add_argument("directory", type=str, help="The directory containing .txt files with tags.")
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="The output file path for merged tags. Defaults to 'merged_tags.txt' in the input directory."
    )
    args = parser.parse_args()
    input_dir = Path(args.directory).resolve() # Resolve to an absolute path
    output_file = Path(args.output).resolve() if args.output else input_dir / "merged_tags.txt"
    merge_tags_in_directory(input_dir, output_file)

if __name__ == "__main__":
    main_cli()
