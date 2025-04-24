# polygon_faucet_auto.py
# Injected auto-claimer for MATIC testnet (Wallet replaced)

import time
import requests

wallet = "0xf689f4e97993b8835F997e09C8A9b851542bcD7e"

print("[+] Claiming MATIC from faucet...")

url = f"https://polygon-fakefaucet.net/claim?address={wallet}"
res = requests.get(url)

if res.status_code == 200:
    print("[✅] Claim sent successfully.")
else:
    print("[❌] Failed to claim MATIC.")

# Wait to mimic legit bot
time.sleep(10)
