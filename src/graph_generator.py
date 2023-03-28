import csv
import json
import logging
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

def read_config(file_path):
    with open(file_path) as config_file:
        config = json.load(config_file)
    return config

def read_csv_data(file_path, config):
    log_level = getattr(logging, config['logging']['log_level'])
    log_file = config['logging']['log_file']
    logging.basicConfig(filename=log_file, level=log_level, format='%(asctime)s [%(levelname)s]: %(message)s')
    
    associations = []
    with open(file_path, mode='r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row

        for row_number, row in enumerate(csvreader, start=2):  # Start counting from 2 because we skipped the header row
            if len(row) != 2:
                error_msg = f"Row {row_number} must have exactly 2 values (Name, Project)"
                logging.error(error_msg)
                continue

            name, project = row
            associations.append((name, project))

    return associations

def generate_graph(associations, config):
    G = nx.Graph()

    for entity1, entity2 in associations:
        G.add_edge(entity1, entity2)

    names = [name for name, _ in associations]
    pos = nx.bipartite_layout(G, names)

    project_associations_count = {}
    for name, project in associations:
        project_associations_count[project] = project_associations_count.get(project, 0) + 1

    project_labels = {}
    for project, count in project_associations_count.items():
        project_labels[project] = f'{project}\n({count})'

    name_labels = {name: name for name in names}

    # Merge the name_labels and project_labels dictionaries
    all_labels = {**name_labels, **project_labels}

    label_font_size = 8  # Change this value to set the desired font size for the labels

    nx.draw(G, pos, with_labels=False, node_color=config['graph']['node_color'], font_size=8, font_weight='bold')
    nx.draw_networkx_labels(G, pos, labels=all_labels, font_size=label_font_size, font_weight='bold')
    plt.show()

