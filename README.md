# Team-Project Mapping

This project generates a bipartite graph that represents the associations between teams and projects based on the data in a CSV file.

## Requirements

- Python 3.7 or higher
- NetworkX
- Matplotlib

## Setup

1. Install the required packages:

```bash
pip install networkx matplotlib


Update the config.json file with the desired settings for the data file, graph display, and logging.

Update the teams_projects.csv file in the data folder with your team, project, and subproject associations.

## Running the Project

Run the main.py script inside the src folder:

```bash
python main.py

The script will read the associations from the CSV file, generate a bipartite graph, and display the graph. If any errors are encountered while reading the CSV file, the errors will be logged in the specified log file.

## Configuration

You can modify the settings in the config.json file to customize the behavior of the project:

- `data.csv_file`: The path to the CSV file containing the team, project, and subproject associations
- `graph.node_color`: The color of the nodes in the generated graph
- `logging.log_level`: The log level for the logging module (e.g., "ERROR", "WARNING", "INFO", "DEBUG")
- `logging.log_file`: The file where errors and other log messages will be saved

