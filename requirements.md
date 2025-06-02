# Requirements for Tag Merger CLI Tool

This is a cli tool to merge tags stored in txt files inside a directory in to a single file.

Tags are stored as `tag1, tag2, tag3` in each file.

The tool will read a directory, read all the files, and merge the tags into a single file.

By default, the output file will be `merged_tags.txt` in the same directory.

User can specify the output file name using the `-o` or `--output` option.

Please init the current directory as pyproject.toml project. put files in the `src` directory.

Generated a README.md file on how to use the tool, install it through pip from git repository.

The repository is https://github.com/ShinChven/merge-tags-cli.git, author is ShinChven, email is shinchven@gmail.com
