const API_URL = "http://localhost:5000/project-2-api/";
const computingPath = API_URL+'computing_efficiency.json';
const microprocessorsPath = API_URL+'microprocessor_clock_speed.json';
const priceChangesPath = API_URL+'price_changes_in_consumer_goods_and_services_in_the_usa_1997_2017.json';
const nonCommercialFlightsPath = API_URL+'non_commercial_flight_distance_records.json';
const humanGenomePath = API_URL+'number_of_human_genome_base_pairs_sequenced_per_us.json';
const supercomputerFlopsPath = API_URL+'supercomputer_power_flops.json';
const transistorsPerMicroprocessorPath = API_URL+'transistors_per_microprocessor.json';
const investmentMexicoPath = API_URL+'conacyt_investment_by_entity_mexico.json';

d3.json(computingPath).then(data => {
    console.log("Computing data",data);
});

d3.json(microprocessorsPath).then(data => {
    console.log("Microprocessors data", data);
});

d3.json(priceChangesPath).then(data => {
    console.log("Price changes data", data);
});

d3.json(nonCommercialFlightsPath).then(data => {
    console.log("Non commercial flights data", data);
});

d3.json(humanGenomePath).then(data => {
    console.log("Human genome pairs data", data);
});

d3.json(supercomputerFlopsPath).then(data => {
    console.log("Supercomputer flops data", data);
});

d3.json(transistorsPerMicroprocessorPath).then(data => {
    console.log('Transistors per microprocessor data',data);
});

d3.json(investmentMexicoPath).then(data => {
    console.log("Investment by entity Mexico data", data);
});