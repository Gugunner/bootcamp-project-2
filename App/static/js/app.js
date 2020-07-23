
d3.json("static/data/data.json").then(data => {
    console.log("D3 Data",data);
    const list = d3.select("#listed");
    console.log("List", list);

    list
        .selectAll("li")
        .data(data.values)
        .enter()
        .append("li")
        .text(v => v.entity);
});