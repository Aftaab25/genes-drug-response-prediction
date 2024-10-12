from cmapPy.pandasGEXpress.parse import parse

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



# Specify the path to the .gctx file
gctx_file = "/home/batman/Downloads/level5_beta_trt_misc_n8283x12328.gctx"

metadata = parse(gctx_file)
df = metadata.data_df
print(df)
# gctoo = parse(metadata, rid = pert_id)
# print(gctoo)
print("==================================================================")

col_gctoo = parse(gctx_file, cid = "ABY001_A375_XH:ADO-TRASTUZUMAB_EMTANSINE:0.3125:24")
col_gctoo_df = col_gctoo.data_df
print(col_gctoo_df.shape)
print(col_gctoo_df)

print("==================================================================")

row_gctoo = parse(gctx_file, rid = "10")
row_gctoo_df = row_gctoo.data_df
print(row_gctoo_df.shape)
print(row_gctoo_df)

print("==================================================================")
