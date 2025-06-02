# Merge Tags CLI Tool

A command-line interface (CLI) tool to merge tags stored in multiple text files within a directory into a single output file. Tags in each input file are expected to be comma-separated (e.g., `tag1, tag2, tag3`).

## Features

- Reads all `.txt` files from a specified directory.
- Merges tags from all files, ensuring uniqueness.
- Outputs the merged tags to a specified file (defaults to `merged_tags.txt` in the input directory).
- Customizable output file name.
- Output tags are sorted alphabetically and comma-separated (e.g., `alpha, beta, gamma`).

## Installation

You can install the `merge-tags-cli` tool directly from its Git repository using pip:

```bash
pip install git+https://github.com/ShinChven/merge-tags-cli.git
```

```bash
pip install --upgrade git+https://github.com/ShinChven/merge-tags-cli.git
```

## Usage

To use the tool, run the `mergetags` command followed by the path to the directory containing your tag files.

```bash
merge-tags <directory_path> [options]
```

**Arguments:**

- `directory_path`: (Required) The path to the directory containing the `.txt` files with tags.

**Options:**

- `-o <output_file_path>`, `--output <output_file_path>`:
  Specifies the path for the output file. If not provided, the output will be saved as `merged_tags.txt` in the `<directory_path>`.

**Examples:**

1.  Merge tags from files in the `my_tags` directory and save to the default `my_tags/merged_tags.txt`:
    ```bash
    merge-tags ./my_tags
    ```

2.  Merge tags from files in the `project_tags` directory and save to a custom file named `all_project_tags.txt` in the current directory:
    ```bash
    merge-tags ./project_tags -o ./all_project_tags.txt
    ```

## Development

This project is managed with `pyproject.toml`.

- Author: ShinChven
- Email: shinchven@gmail.com
- Repository: https://github.com/ShinChven/merge-tags-cli
