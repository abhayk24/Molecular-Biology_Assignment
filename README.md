# Promoter Prediction with a 1D-CNN

This project trains and compares machine learning models that detect a
bacterial-type **promoter** inside a 100-base DNA sequence. A promoter here
means a `-35 box (TTGACA)` followed by a spacer of 16-18 bases and then a
`-10 box (TATAAT)`. The notebook builds its own dataset, trains three
models, and compares them.

## Files in this folder

| File | What it is |
|---|---|
| `Promoter_Prediction_CNN.ipynb` | Main notebook. Run this. |
| `promoter_dataset.csv` | Ready-made dataset (8,000 DNA sequences with labels), so you don't have to generate it again. |
| `README.md` | This file. |

## Requirements

- Python 3.9 or newer
- Packages: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `tensorflow`
- Jupyter Notebook, JupyterLab, or Google Colab to open the `.ipynb` file

Install everything with:

```bash
pip install numpy pandas scikit-learn matplotlib tensorflow jupyter
```

`tensorflow` is a large download (several hundred MB). If your laptop is
slow or has no GPU, it is easiest to upload the notebook and the CSV to
**Google Colab** (colab.research.google.com) and run it there for free.

## How to run

1. Open `Promoter_Prediction_CNN.ipynb` in Jupyter or Colab.
2. Make sure `promoter_dataset.csv` is in the **same folder** as the
   notebook (Colab: upload it in the Files panel on the left).
3. Run all cells in order, from top to bottom
   (Jupyter: `Cell > Run All`. Colab: `Runtime > Run all`).
4. The notebook re-creates the dataset itself in the first section, so it
   will overwrite `promoter_dataset.csv` with a new (but very similar)
   version. If you want to keep the exact original file, make a copy of it
   before running.

Total run time is a few minutes on a normal laptop CPU; no GPU is needed.

## What the notebook does, step by step

1. **Create the dataset** – generates 8,000 DNA sequences: 4,000 real
   promoters and 4,000 negatives (random DNA, single-box decoys, and
   wrong-spacing decoys, so the task is not too easy).
2. **Load data and inspect** – reads the CSV and shows the class counts.
3. **Encode sequences** – turns each sequence into a 100 x 4 one-hot
   matrix (A, C, G, T).
4. **Train / validation / test split** – 70% / 15% / 15%, stratified.
5. **Baseline models** – Logistic Regression and Random Forest, trained on
   6-mer counts.
6. **1D-CNN** – a small convolutional neural network trained on the
   one-hot sequences.
7. **Results table** – Accuracy, Precision, Recall, F1, MCC and ROC-AUC
   for all three models, saved to `results.csv`.
8. **Figures** – training/validation curves, ROC curves, a confusion
   matrix, and the learned first-layer CNN filters, saved as `.png` files.
9. **Try the model on new sequences** – runs the trained CNN on two
   hand-written example sequences to sanity-check what it learned.

## Output files created after running

These are not included here; they are created the first time you run the
notebook:

- `promoter_dataset.csv` (regenerated)
- `results.csv`
- `training_curves.png`
- `roc_curves.png`
- `confusion_matrix.png`
- `cnn_filters.png`
- `promoter_cnn.keras` (the trained model, can be reloaded later)

## Expected results (approximate)

| Model | Accuracy | MCC | ROC-AUC |
|---|---|---|---|
| Logistic Regression (6-mer) | ~0.60 | ~0.20 | ~0.66 |
| Random Forest (6-mer) | ~0.71 | ~0.42 | ~0.77 |
| **1D-CNN (one-hot)** | **~0.91** | **~0.83** | **~0.97** |

Exact numbers vary slightly between runs because of random weight
initialisation, even with a fixed seed, and can also vary a little between
TensorFlow versions.

## Using your own / real data

Replace `promoter_dataset.csv` with any CSV that has exactly two columns:

- `sequence` – a DNA string using only A, C, G, T
- `label` – 1 (promoter) or 0 (not a promoter)

If your sequences are not 100 bases long, change the length value used in
Section 3 (one-hot encoding) and Section 6 (CNN input shape) to match.
Real promoter data can be obtained from **RegulonDB** (E. coli) or the
**Eukaryotic Promoter Database (EPD)**.

## Notes

- The dataset is synthetic (rule-based), built only to demonstrate the
  method. Results are not a claim about real biological promoters.
- A fixed random seed (42) is used throughout for reproducibility.
- No GPU is required; training finishes in under two minutes on CPU.
