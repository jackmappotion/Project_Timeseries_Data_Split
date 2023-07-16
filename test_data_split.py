datasets = list(range(1,1000))

CFG = {
    "dataset_window": 300,
    "input_window": 15,
    "output_window": 5,
}

x_dataset = list()
y_dataset = list()

dataset = datasets[-CFG["dataset_window"] :]
for data_idx in range(len(dataset) - CFG["input_window"] - CFG["output_window"] + 1):
    x = dataset[data_idx : data_idx + CFG["input_window"]]
    y = dataset[
        data_idx + CFG["input_window"] : 
        data_idx + CFG["input_window"] + CFG["output_window"]
    ]
    x_dataset.append(x)
    y_dataset.append(y)
    final_x = dataset[-CFG["input_window"] :]

test_dataset = (x_dataset, y_dataset, final_x)