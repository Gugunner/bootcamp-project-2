const path = 'http://localhost:5000/project-2-api/computing_efficiency.json';
const path2 = 'http://localhost:5000/project-2-api/microprocessor_clock_speed.json';
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

d3.json(path).then(data => {
    console.log("D3 Data",data);
    const list = d3.select("#listed");

    list
        .selectAll("li")
        .data(data.values)
        .enter()
        .append("li")
        .text(v => v.entity);
});

d3.json(path2).then(data => {
    console.log("Data 2", data);
});
