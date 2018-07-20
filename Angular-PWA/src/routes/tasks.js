const router = require('express').Router();
const mongojs = require('mongojs');
const db = mongojs('mean-tasks', ['tasks']);
const dbfiware = mongojs('report_fiware',['fiware']); 

// fiware databases
// {
// GET All tasks
router.get('/fiware',(req, res, next) =>{
    dbfiware.fiware.find((err, fiware) => {
        if (err) return next (err);
        res.json(fiware);
    });
});

// GE specific
//var ge = require.params.ge;
//var query={};
//query[GE_name] = ge; 
//router.get('/fiware/GEespecific', (req, res, next) => {
//    dbfiware.fiware.find(query,{GE_name:1,Version:1,Test:1,Execution_time:1,Date:1,Time:1,Containers:1,_id:0}, (err, ge) => {
//        if (err) return next(err);
//        res.json(ge);
//    });
//});

// GE Kurento 
router.get('/fiware/kurento', (req, res, next) => {
    dbfiware.fiware.find({GE_name:"kurento"},{GE_name:1,Version:1,Test:1,Execution_time:1,Date:1,Time:1,Containers:1,_id:0}, (err, ge) => {
        if (err) return next(err);
        res.json(ge);
    });
});
// }


// GET All tasks
router.get('/tasks', (req, res, next) => {
    db.tasks.find((err, tasks) => {
        if (err) return next(err);
        res.json(tasks);
    });
});

// Single Task
router.get('/tasks/:id', (req, res, next) => {
    db.tasks.findOne({_id: mongojs.ObjectId(req.params.id)}, (err, task) => {
        if (err) return next(err);
        res.json(task);
    });
});

// Add a Task
router.post('/tasks', (req, res, next) => {
    const task = req.body;
    if(!task.title || !(task.isDone + '')) {
        res.status(400).json({
            'error': 'Bad Data'
        });
    } else {
        db.tasks.save(task, (err, task) => {
            if (err) return next(err);
            res.json(task);
        });
    }
});

// Delete task
router.delete('/tasks/:id', (req, res, next) => {
    db.tasks.remove({_id: mongojs.ObjectId(req.params.id)}, (err, task) => {
        if(err){ res.send(err); }
        res.json(task);
    });
})

// Update Task
router.put('/tasks/:id', (req, res, next) => {
    const task = req.body;
    let updateTask = {};
    
    if(task.isDone) {
        updateTask.isDone = task.isDone;
    }
    if(task.title) {
        updateTask.title = task.title;
    }
    if(!updateTask) {
        res.status(400);
        res.json({'error': 'bad request'});
    } else {
        db.tasks.update({_id: mongojs.ObjectId(req.params.id)}, updateTask, {}, (err, task) => {
            if (err) return next(err);
            res.json(task);
        });
    }
});

// GE-Fiware
router.get('/kurento', callName);
function callName(req, res){
    var spawn = require("child_process").spawn;
    var process = spawn('python',["./index.py"]);
    //                        req.query.firstname,
    //                        req.query.lastname] );
    //process.stdout.on('data', function(data){
    //    res.send(data.toString());
    //})
    process.stdout.on('data', function (data){
        console.log('process: ',data);
        //res.send(data.toString());
    })
}


module.exports = router;