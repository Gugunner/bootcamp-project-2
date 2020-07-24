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
    return data

def create_microprocessor_clock_speed_dict(mongo_values):
    data = {}
    data["values"] = []
    for value in mongo_values:
        newDict = {
            "entity": value["Entity"],
            "year": value["Year"],
            "microprocessor": value["Microprocessor clock speed (Hertz (pulses per second))"]
        }
        data["values"].append(newDict)
    return  data
