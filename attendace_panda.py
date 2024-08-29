import pandas as pd

df = pd.read_json('attendace_records.json')


def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.extend(flatten_dict(item, f"{new_key}_{i}", sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

flattened_data = {k: flatten_dict(v) for k, v in df.items()}

df_flat = pd.DataFrame(flattened_data).T

file_path = "attendance_records.xlsx"
df_flat.to_excel(file_path, index=False)
