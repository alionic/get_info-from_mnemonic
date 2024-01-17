from eth_account import Account


def load_seeds() -> list:
    with open("seeds.txt", 'r') as f:
        seeds : list = [row.strip() for row in f if row.strip()]
    return seeds

def get_account_info(seed: str) -> list:
    account = Account.from_mnemonic(mnemonic=seed)
    return [seed, account._private_key.hex(), account._address]

def write(rows: list) -> None:
    with open("res.txt", 'w') as f:
        [f.write(','.join(row).format() + '\n') for row in rows]

if __name__ == "__main__":
    seeds = load_seeds()
    Account.enable_unaudited_hdwallet_features()
    rows = [get_account_info(seed) for seed in seeds]
    write(rows)
