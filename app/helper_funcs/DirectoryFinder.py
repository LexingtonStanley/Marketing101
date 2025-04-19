from pathlib import Path
import os

class DirectoryFinder:
    @staticmethod
    def find_project_root(start_path=None, markers=None):
        """
        Find the project root by searching for marker files or directories.

        Args:
            start_path (Path, optional): Path to start searching from. Defaults to current working directory.
            markers (list, optional): List of marker files/directories to identify the project root.

        Returns:
            Path: Project root path
        """
        if start_path is None:
            start_path = Path(os.getcwd()).resolve()

        if markers is None:
            markers = ['.git', 'pyproject.toml', 'LakeAPI_DataCollectionManagers.py', '.env', '.yml', 'requirements.txt']

        check_path = start_path
        while check_path != check_path.parent:  # Stop at filesystem root
            for marker in markers:
                if (check_path / marker).exists():
                    return check_path
            check_path = check_path.parent

        # If no marker found, return the starting path
        return start_path

    def get_data_dir(self, data_dir='data', project_markers=None, create_if_missing=False):
        """
        Returns the path to the data directory relative to the project root,
        regardless of which script calls this function.

        Args:
            data_dir (str): Name of the data directory (default: 'data')
            project_markers (list, optional): List of files/directories that mark the project root.
            create_if_missing (bool): Create the data directory if it doesn't exist (default: False)

        Returns:
            Path: Path object pointing to the data directory
        """
        # Find the project root
        project_root = self.find_project_root(markers=project_markers)

        # Get the data directory path
        data_path = project_root / data_dir

        # Create the directory if it doesn't exist and create_if_missing is True
        if create_if_missing and not data_path.exists():
            data_path.mkdir(parents=True, exist_ok=True)

        return data_path