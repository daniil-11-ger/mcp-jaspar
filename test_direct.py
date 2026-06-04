import requests

def search_jaspar(tf_name: str, species: str = "human") -> dict:
    tax_map = {"human": "9606", "mouse": "10090", "rat": "10116", "drosophila": "7227"}
    tax = tax_map.get(species.lower(), "9606")
    url = f"https://jaspar.elixir.no/api/v1/matrix?name={tf_name}&tax_group={tax}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
        else:
            return {"error": f"API error {r.status_code}"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print("=== TEAD1 human ===")
    print(search_jaspar("TEAD1", "human"))
    print("\n=== CEBPA human ===")
    print(search_jaspar("CEBPA", "human"))
    print("\n=== NO_SUCH_TF ===")
    print(search_jaspar("NO_SUCH_TF", "human"))