# Promoter Prediction with a 1D-CNN

This project trains and compares machine learning models to detect a bacterial-type **promoter** inside a 100-base DNA sequence.

A promoter is defined here as:

- **-35 box:** `TTGACA`
- **Spacer:** 16–18 bases
- **-10 box:** `TATAAT`

The notebook creates the dataset, preprocesses DNA sequences, trains three different models, and compares their performance.

---

## Files in This Folder

| File | Description |
|---|---|
| `Promoter_Prediction_CNN.ipynb` | Main notebook. Run this file. |
| `promoter_dataset.csv` | Dataset containing 8,000 DNA sequences with labels. |
| `README.md` | Project documentation. |

---

## Requirements

- Python 3.9 or newer
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- TensorFlow
- Jupyter Notebook / JupyterLab / Google Colab

### Installation

```bash
pip install numpy pandas scikit-learn matplotlib tensorflow jupyter
