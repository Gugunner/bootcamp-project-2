
def create_computing_efficiency_dict(mongo_values):
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
    return data

def create_non_commercial_flight_distance_records_dict(mongo_values):
    data = {}
    data["values"] = []
    for value in mongo_values:
        newDict = {
            "entity": value["Entity"],
            "year": value["Year"],
            "kilometers": value[" (kilometres)"]
        }
        data["values"].append(newDict)
    return data

#Check data as it may be incomplete
# def create_number_of_human_genome_base_pairs_sequenced_per_us_dict(mongo_values):
#     data = {}
#     data["values"] = []
#     for value in mongo_values:
#         newDict = {
#             "entity": value["Entity"],
#             "year": value["Year"],
#             "kilometers": value[" (kilometres)"]
#         }
#         data["values"].append(newDict)
#     return data

def create_price_changes_in_consumer_goods_and_services_in_the_usa_1997_2017_dict(mongo_values):
    data = {}
    data["values"] = []
    for value in mongo_values:
        newDict = {
            "entity": value["Entity"],
            "year": value["Year"],
            "clothing": value["Clothing (%)"],
            "newCars": value["New cars (%)"],
            "toys": value["Toys (%)"],
            "tvs": value["TVs (%)"],
            "software": value["Software (%)"],
            "householdEnergy": value["Household energy (%)"],
            "publicTransportation": value["Public transportation (%)"],
            "education": value["Education (%)"],
            "collegeTuitionFees": value["College tuition fees (%)"],
            "childcare": value["Childcare (%)"],
            "foodBeverages": value["Food & Beverages (%)"],
            "housing": value["Housing (%)"],
            "medicalCare": value["Medical care (%)"]
        }
        data["values"].append(newDict)
    return data

