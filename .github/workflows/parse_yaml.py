import sys
import yaml


def get_first_key(file_path):
    """
    Returns the first key of a YAML file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        str: The first key of the YAML file.
    """
    with open(file_path, 'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
        if not isinstance(content, dict):
            raise ValueError("Invalid YAML file.")
        if not content:
            raise ValueError("Empty YAML file.")
        first_key = next(iter(content))
        return first_key


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_first_key.py <yaml_file_path>")
        sys.exit(1)
    yaml_file_path = sys.argv[1]
    try:
        first_key = get_first_key(yaml_file_path)
        print(first_key)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
