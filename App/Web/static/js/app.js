const computingPath = 'http://localhost:5000/project-2-api/computing_efficiency.json';
const microprocessorsPath = 'http://localhost:5000/project-2-api/microprocessor_clock_speed.json';
const priceChangesPath = 'http://localhost:5000/project-2-api/price_changes_in_consumer_goods_and_services_in_the_usa_1997_2017.json';

// const data = {
//     headers: {
//         'Accept': 'application/json',
//         'Content-Type': 'application/json'
//     }
// };

// const getData = async() => {
//     data.method = 'GET';
//     return fetch(path)
//         .then(response => {
//             if(response.ok) {
//                 return response.json();
//             } else {
//                 return  false;
//             }
//         })
//         .then(jsonResponse => {
//             if(!jsonResponse) {
//                 return false;
//             }
//             return jsonResponse;
//         }).catch((error) => {
//             console.log("Error",error);
//         })
// };
//
// getData().then(jsonResponse => {
//     console.log("D3 Data",jsonResponse);
// });

d3.json(computingPath).then(data => {
    console.log("Computing data",data);
    const list = d3.select("#listed");

    list
        .selectAll("li")
        .data(data.values)
        .enter()
        .append("li")
        .text(v => v.entity);
});

d3.json(microprocessorsPath).then(data => {
    console.log("Microprocessors data", data);
});

d3.json(priceChangesPath).then(data => {
    console.log("Price changes data", data);
});


