const cors = require('cors')
const express = require('express');
const app = express();

const path = require('path'); 
const indexRoutes = require('./routes/index'); // index mean-app
const tasksRoutes = require('./routes/tasks'); // ruta tasks
//const fiwareReport = require('./fiwareReport/fiware'); // ruta fiware report
//const geFiware = require('./geFiware/geFiware'); // geFiware

//setings
app.set('views',path.join(__dirname, 'views'));
app.set('port', process.env.PORT || 3000);
//app.set('port', 3000);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');

/*/ GE-Fiware
app.get('/kurento', callName);
function callName(req, res){
    var spawn = require("child_process").spawn;
    var process = spawn('python',["./index.py"]);
    //                        req.query.firstname,
    //                        req.query.lastname] );
    //process.stdout.on('data', function(data){
    //    res.send(data.toString());
    //})
    process.stdout.on('data', function (data){
        //console.log('process: ',data);
        res.send(data.toString());
    })
}*/

//middlewares
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({extended: false}));

// routes
app.use(indexRoutes); // index mean-app
app.use('/api',tasksRoutes); // tasks
//app.use('/fiware',fiwareReport); // fiware
//app.use('/ge',geFiware);

//static files
app.use(express.static(path.join(__dirname, 'dist')));

//start server
app.listen(app.get('port'), () => {
    console.log('server on port 3000', app.get('port'))
});