from cmapPy.pandasGEXpress.parse import parse

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Specify the path to the .gctx file
gctx_file = "/home/batman/Downloads/level5_beta_trt_cp_n720216x12328.gctx"

# Load only a subset of rows and columns (use row/col ids or slice for specific portions)
gctoo = parse(gctx_file, rid=["Gene_1", "Gene_2", "Gene_3"], cid=["Sample_1", "Sample_2"])

# Access the subset of data
data_df = gctoo.data_df

# Print the data dimensions and first few rows
print(data_df.shape)
print(data_df.head())

