import os

file_path = 'path/to/file'

file_size_bytes = os.path.getsize(file_path)

file_size_kilobytes = file_size_bytes/1000
file_size_megabytes = file_size_bytes/1000
print(f"file size: {file_size_bytes} bytes")
print(f"file size: {file_size_kilobytes} kilobytes")
print(f"file size: {file_size_megabytes} megabytes")
