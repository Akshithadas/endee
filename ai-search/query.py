from endee import Client

client = Client()

def search(query):
    print(f"\n🔍 Searching for: {query}")

    results = client.search(query)

    print("\n📄 Results found:")
    for r in results:
        print("-", r)

    return results