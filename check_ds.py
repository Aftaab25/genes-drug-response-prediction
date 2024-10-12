from cmapPy.pandasGEXpress import parse_gctx
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Specify the path to the .gctx file
gctx_file = "/home/batman/Downloads/level5_beta_trt_cp_n720216x12328.gctx"

import os

# Check if the file exists and is accessible
print("File exists:", os.path.exists(gctx_file))
print("File is readable:", os.access(gctx_file, os.R_OK))


# Get row (gene) and column (sample) IDs
# gctoo = parse_gctx.parse(gctx_file)

# Print available gene IDs (row IDs)
# gene_ids = gctoo.row_metadata_df.index.tolist()
# print("Available Gene IDs:", gene_ids[:10])  # print the first 10 for inspection
# 
# # Print available sample IDs (column IDs)
# sample_ids = gctoo.col_metadata_df.index.tolist()
# print("Available Sample IDs:", sample_ids[:10])  # print the first 10 for inspection

