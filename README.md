# Query Uploader

Query Uploader is a Python script designed to read SQL query files from a specified directory, process them, and update a database table with the query information.

## Usage:

### Prerequisites

- Python 3.x
- MySQL server
- PyYaml

### Installation

1. Clone this repository to your local machine:

    ```
    git clone <repository-url>
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

### Configuration

Before running the script, make sure to configure the database connection and other settings in the `config.yml` file located in the `config` directory.

### Running the Script

To run the script, execute the following command in your terminal:

    python main.py <config_file_path> <directory_path>

Replace `<config_file_path>` with the path to your configuration file (e.g., `C:\path\to\config.yml`) and `<directory_path>` with the path to the directory containing your SQL query files.
