from graph_generator import read_csv_data, read_config, generate_graph

def main():
    config = read_config('../config/config.json')
    associations = read_csv_data(config['data']['csv_file'], config)
    generate_graph(associations, config)

if __name__ == "__main__":
    main()

