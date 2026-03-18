# 01 — Pandas Series

## What is a Series?
A Series is a **1D labelled array** — like a single column in a spreadsheet.
Every value has an index label (default: 0, 1, 2...)

## Methods covered

| Method | Description |
|--------|-------------|
| `pd.Series([...])` | From a list |
| `pd.Series([...], index=[...])` | From a list with custom index |
| `pd.Series((...))` | From a tuple |
| `pd.Series({...})` | From a dictionary |
| `pd.Series({...}, index=[...])` | From dict with specified index |
| `pd.Series(scalar, index=[...])` | Scalar value repeated |
| `pd.Series(np.array([...]))` | From NumPy array |
| `pd.Series([...], dtype="float")` | With forced dtype |
| `pd.Series(dtype="int")` | Empty Series |
| `pd.Series(range(1,6))` | From range |
| `pd.Series(list("DATA"))` | From string characters |
| `pd.Series(index=[...])` | Index only — NaN values |
| `pd.Series([...], name="...")` | With name attribute |

## Key Takeaways
- If index label has no matching key in dict → value becomes `NaN`
- If even one `NaN` exists in numeric Series → dtype auto-upgrades `int64` → `float64`
- Label slicing `s["b":"d"]` → end is **inclusive**
- Position slicing `s[1:3]` → end is **exclusive**
- `s.name` gives the Series a label (useful when building DataFrames later)