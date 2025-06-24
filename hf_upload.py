from huggingface_hub import HfApi, Repository
import os
import shutil

USERNAME = "rdxrud"
REPO_NAME = "forest-fire-detector"
REPO_ID = f"{USERNAME}/{REPO_NAME}"

base_path = "/Users/rudrakshagarwal/Forest Fire Detection"

files_to_upload = {
    "classification/vgg-16/my_keras_model.keras": f"{base_path}/classification/vgg-16/my_keras_model.keras",
    "classification/custom cnn/custom_cnn_model.keras": f"{base_path}/classification/custom cnn/custom_cnn_model.keras",
    "classification/resNet-34/resnet_model.keras": f"{base_path}/classification/resNet-34/resnet_model.keras"
}

api = HfApi()

if not api.repo_exists(REPO_ID):
    print(f"🛠️ Creating repo: {REPO_ID}")
    api.create_repo(REPO_ID, exist_ok=True, private=False)
else:
    print(f"✅ Repo already exists: {REPO_ID}")

# Clean clone
if os.path.exists("temp_hf_repo"):
    shutil.rmtree("temp_hf_repo")
print("📦 Cloning repo locally...")
repo = Repository(local_dir="temp_hf_repo", clone_from=REPO_ID)

# Track .keras files using Git LFS
print("📦 Enabling Git LFS for *.keras files")
os.system("cd temp_hf_repo && git lfs install && git lfs track '*.keras'")
with open("temp_hf_repo/.gitattributes", "a") as f:
    f.write("*.keras filter=lfs diff=lfs merge=lfs -text\n")

# Copy files
for dest, src in files_to_upload.items():
    dest_path = os.path.join("temp_hf_repo", dest)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    shutil.copy2(src, dest_path)
    print(f"📁 Copied: {src} -> {dest_path}")

# Push
print("📤 Pushing files to Hugging Face using LFS...")
repo.git_add()
repo.git_commit("Add Keras model files with Git LFS")
repo.git_push()

print(f"✅ Upload complete! View your repo at: https://huggingface.co/{REPO_ID}")