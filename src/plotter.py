import json
from collections import defaultdict
from matplotlib import pyplot as plt
from utils import seconds_to_milliseconds


CHART_TITLE = 'Sorting algorithms comparison'
XLABEL = 'dataset size'
YLABEL = 'computation time [ms]'
FIGSIZE = (10, 7.2)

ALGO_COLORS = {
    'bubble_sort': 'red',
    'selection_sort': 'orange',
    'insertion_sort': 'purple',
    'merge_sort': 'blue',
    'quick_sort': 'green'
}


def preprocess_data(json_data):
    data = defaultdict(dict)

    for benchmark in json_data['benchmarks']:
        name = benchmark['extra_info']['name']
        sample_size = benchmark['extra_info']['sample_size']
        mean = seconds_to_milliseconds(benchmark['stats']['mean'])
        data[name][sample_size] = mean

    return data


def plot_separate(data):
    fig,  ax = plt.subplots(nrows=len(data), ncols=1, figsize=FIGSIZE)
    idx = 0
    for algorithm_name, algorithm_data in data.items():
        ax[idx].plot(algorithm_data.keys(), algorithm_data.values(),
                     color=ALGO_COLORS[algorithm_name],
                     marker='o', linestyle='dashed',
                     linewidth=2, markersize=5, label=algorithm_name)

        ax[idx].legend()
        idx += 1

    fig.supxlabel(XLABEL)
    fig.supylabel(YLABEL)
    fig.suptitle(CHART_TITLE)


def plot_together(data):
    plt.figure(figsize=FIGSIZE)

    for algorithm_name, algorithm_data in data.items():
        plt.plot(algorithm_data.keys(), algorithm_data.values(),
                 color=ALGO_COLORS[algorithm_name],
                 marker='o', linestyle='dashed',
                 linewidth=2, markersize=5, label=algorithm_name)

    plt.title(CHART_TITLE)
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.legend()


def generate_chart(input_file, output_file, separate):
    with open(input_file) as f_handle:
        json_data = json.load(f_handle)
        data = preprocess_data(json_data)

    if separate:
        plot_separate(data)
    else:
        plot_together(data)

    plt.savefig(output_file)
    plt.show()
