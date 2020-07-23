import json

def create_test_json(mongo_values):
    data = {}
    data["values"] = []
    for value in mongo_values:
        newDict = {
            "entity": value["Entity"],
            "year": value["Year"],
            "computing": value["Computing efficiency (Watts per MIPS)"]
        }
        data["values"].append(newDict)
    print(f"Data {data} {len(data)}")
    with open('static/data/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
