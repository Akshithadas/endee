from endee import Client

def load_data():
    with open("data.txt", "r") as file:
        text = file.read()

    # Split into small chunks (line by line)
    chunks = text.split("\n")

    # Remove empty lines
    chunks = [chunk.strip() for chunk in chunks if chunk.strip() != ""]

    return chunks


def ingest():
    client = Client()

    data = load_data()

    print("📥 Data to insert:", data)

    client.insert(data)

    print("✅ Data successfully stored in Endee!")


if __name__ == "__main__":
    ingest()