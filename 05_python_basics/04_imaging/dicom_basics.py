"""DICOM basics with pydicom.
Reads metadata from a DICOM file if provided; otherwise explains usage.
"""
import sys
try:
    import pydicom  # type: ignore
except Exception as e:
    print("pydicom not installed. Install with: pip install pydicom")
    sys.exit(0)

if len(sys.argv) < 2:
    print("Usage: python 05_python_basics/04_imaging/dicom_basics.py <path_to_dicom>")
    sys.exit(0)

path = sys.argv[1]
ds = pydicom.dcmread(path)
print("PatientID:", getattr(ds, 'PatientID', 'NA'))
print("Modality:", getattr(ds, 'Modality', 'NA'))
print("Rows x Cols:", getattr(ds, 'Rows', '?'), 'x', getattr(ds, 'Columns', '?'))
