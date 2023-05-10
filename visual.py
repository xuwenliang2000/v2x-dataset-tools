"""Visualize the dataset."""

from simple_parsing import ArgumentParser

from v2x_datasets_tools.utils.datasets_arguments import DatasetsArguments

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_arguments(DatasetsArguments, dest="datasets_arguments")

    args = parser.parse_args()

    print(args.datasets_arguments)
