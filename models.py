import os

# Define the extensions you're looking for
extensions = {
    ".h5", ".hdf5", ".pb", ".pkl", ".joblib", ".sav",
    ".tflite", ".pt", ".onnx", ".keras"
}

# Root directory to start search (change '.' if needed)
root_dir = "Forest Fire Detection"

# Store matching file paths
matching_files = []

# Walk through the directory tree
for root, _, files in os.walk(root_dir):
    for file in files:
        if any(file.endswith(ext) for ext in extensions):
            full_path = os.path.join(root, file)
            matching_files.append(full_path)

# Output the result
if matching_files:
    print("Found the following model files:")
    for path in matching_files:
        print(path)
else:
    print("No matching model files found.")