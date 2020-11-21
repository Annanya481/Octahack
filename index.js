const http = require("http");
const fs = require('fs');
const express = require('express');
const app = express();
const fastcsv = require('fast-csv');
const ws = fs.createWriteStream("out.csv", {flag:"a"});
const csvFilePath= "out.csv"
const csv=require('csvtojson')
const alert=require('alert')

app.set('view engine', 'ejs');

app.get("/", function(req, res){
    csv().fromFile('Table.csv')
    .then(users => {
        console.log();
    }).catch(err => {
        // log error if any
        console.log(err);
    });
    res.render("report.ejs");
})
app.use(express.static("./static"));
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
    csv().fromFile(csvFilePath).then((data)=>{
      console.log(data);
    }).catch(err => {
        // log error if any
        console.log(err);
    });
    alert("Your report has been submitted!")
    res.render('report.ejs');
})
app.get("/map", function(req, res){
    res.sendFile(__dirname+"/Engine/laPointMap.html");
})
app.listen(8000, ()=>{console.log("App listening on port 8000!")});
