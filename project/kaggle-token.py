import json
kaggle_username = "idoukk"
kaggle_key = "71cc9220f03d0e541ab88b3e193cb552"

# Save API token the kaggle.json file
with open("/home/ubu/.config/kaggle/kaggle.json", "w") as f:
    f.write(json.dumps({"username": kaggle_username, "key": kaggle_key}))