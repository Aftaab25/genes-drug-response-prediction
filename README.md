# Genes Drug Prediction

This repository contains a project for predicting the response of various cell lines to specific drug treatments based on concentration and exposure time. The analysis is based on a dataset that includes genetic cell line information, drug concentration, time points, and corresponding cell viability responses. The project explores drug efficacy prediction through machine learning models, primarily using **Random Forest Regressor** and **Principal Component Analysis (PCA)**.

## Project Overview

Understanding the impact of drug concentration and exposure on cell viability is essential for drug discovery and personalized medicine. This project aims to predict cell viability based on specific conditions (drug, concentration, and time) for different cell lines. We employ a combination of exploratory data analysis, dimensionality reduction, and machine learning to build a predictive model and interpret the results.

## Key Features

- **Data Exploration and Analysis**: Visualization of response distribution and identification of meaningful thresholds for cell viability classification.
- **Dimensionality Reduction**: Use of PCA to reduce feature dimensionality, improving model performance and interpretability.
- **Machine Learning Modeling**: Random Forest Regressor is trained and evaluated to predict cell viability based on drug concentration and time.
- **Custom Input Prediction**: Allows users to input custom drug concentration and time points for prediction, with automatic feedback on whether the combination is optimal or suboptimal.

## Files

- `genes_drug_prediction.ipynb`: The main Jupyter Notebook containing code, visualizations, and explanations for data preprocessing, modeling, and prediction.

## Getting Started

### Prerequisites

To run the code in this repository, you’ll need the following:

- Python 3.x
- Jupyter Notebook
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `ipywidgets` (for interactive dropdowns)

Install the required libraries using:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn ipywidgets
```

## Data

The dataset used in this project is expected to be in .gctx format, containing information about different cell lines, drugs, concentrations, and time points. Ensure the dataset is available in the appropriate path as specified in the notebook.

## Running the Notebook

1. Clone this repository.
   ```bash
   git clone https://github.com/aftaab25/genes-drug-response-prediction.git
   cd genes_drug_prediction
   ```
2. Open the Jupyter Notebook:
   ```bash
    jupyter notebook genes_drug_prediction.ipynb
   ```
3. Follow the cells sequentially for data exploration, preprocessing, modeling, and prediction.

## Project Workflow

1. **Data Loading and Cleaning**:
   - Load the dataset and preprocess it, including extracting relevant columns like `cell line`, `drug`, `concentration`, and `time point`.
   - Generate threshold values for categorizing cell viability based on the dataset distribution.

2. **Exploratory Data Analysis**:
   - Visualize the distribution of response values to determine thresholds for low, medium, and high cell viability.

3. **Dimensionality Reduction**:
   - Use PCA to reduce the feature space, improving model performance and interpretability.

4. **Model Training and Evaluation**:
   - Train a Random Forest Regressor to predict cell viability based on transformed PCA features.
   - Evaluate model performance using metrics like Mean Squared Error (MSE) and R-squared (R²).

5. **Custom Prediction Interface**:
   - Input custom drug concentration and time points through interactive dropdowns to predict cell viability.
   - Automatic feedback on the effectiveness of the selected drug and condition.

## Results

The model achieved strong performance with high R-squared values, indicating that it effectively captures the relationship between drug conditions and cell viability. Using dataset-specific thresholds, we can classify predicted viability as low, medium, or high, aiding in the identification of optimal drug conditions.

## Example Usage

To make a prediction for a specific cell line and drug combination, input the desired concentration and time point, and the notebook will output the predicted cell viability category.

```python
# Example input for concentration and time point
example_concentration = 3.77
example_time_point = 3

# Predict cell viability response
predicted_response = model.predict(example_pca_df)
print(f"Predicted Response: {predicted_response[0]}")
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions for improvements or additional features.

## License

This project is licensed under the [MIT License](LICENSE).
