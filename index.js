const http = require("http");
const fs = require('fs');
const express = require('express');
const app = express();
const fastcsv = require('fast-csv');
const ws = fs.createWriteStream("out.csv");
app.set('view engine', 'ejs');

app.get("/", function(req, res){
    res.render("report.ejs");
})

app.use(express.urlencoded({
    extended: true
}))

app.post('/submit-form', (req, res) => {
    const locality = req.body.locality;
    const report = req.body.textarea;
    const data = [
        {"locality": locality, "report": report}
    ];
    fastcsv
        .write(data, { headers: true })
        .pipe(ws);
    res.end();
})
app.listen(8000, ()=>{console.log("App listening on port 8000!")});