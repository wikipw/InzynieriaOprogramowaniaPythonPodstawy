import string
from collections import defaultdict, Counter

def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    # Preprocessing – tworzenie listy słowników zliczających słowa w dokumentach
    word_counts = []
    translator = str.maketrans('', '', string.punctuation)

    for doc in documents:
        cleaned = doc.lower().translate(translator)
        word_counts.append(Counter(cleaned.split()))

    results = []
    for query in queries:
        query = query.lower()
        freq_doc_list = []

        for i, word_count in enumerate(word_counts):
            freq = word_count[query]
            if freq > 0:
                freq_doc_list.append((freq, i))

        # Sortuj wg liczby wystąpień malejąco, potem wg indeksu dokumentu malejąco
        freq_doc_list.sort(key=lambda x: (-x[0], -x[1]))
        result = [doc_id for _, doc_id in freq_doc_list]
        results.append(result)

    return results

if __name__ == "__main__":
    # Pobranie liczby dokumentów
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())

    # Pobranie liczby zapytań
    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())

    # Przetworzenie zapytań
    results = index_documents(documents, queries)

    # Wypisanie wyników
    print("Wyniki:")
    for res in results:
        print(res)