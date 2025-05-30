from huggingface_hub import snapshot_download
# from modelscope import snapshot_download as modelscope_snapshot_download
mineru_patterns = [
    # "models/Layout/LayoutLMv3/*",
    
    "models/Layout/YOLO/*",
    "models/MFD/YOLO/*",
    "models/MFR/unimernet_hf_small_2503/*",
    "models/OCR/paddleocr_torch/*",

    # "models/TabRec/TableMaster/*", we dont use this atm




]
model_dir = snapshot_download(
    "opendatalab/PDF-Extract-Kit-1.0",
    local_dir="/root/PDF-Extract-Kit",
    allow_patterns=mineru_patterns,
    max_workers=20
)
# /root/PDF-Extract-Kit/models/OCR/paddleocr_torch/ch_PP-OCRv3_det_infer.pth
# hantian/layoutreader
layoutreader_model_dir = snapshot_download(
    "hantian/layoutreader", local_dir="/root/layoutreader"
)
# layoutreader_model_dir = modelscope_snapshot_download(
#     "ppaanngggg/layoutreader", local_dir="/root/layoutreader"
# )
