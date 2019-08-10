db.faculty.aggregate([

{
    $group :
    { _id : 
        {"dno" : "$deptno" ,
          "qual":"$qualification"
         },
        t_sal : {$sum:"$salary"}
     }
},

{$project:{
    
    "deptno":"$_id.dno",
    "qualification":"$_id.qual",
    "total_salary":"$t_sal",
    _id:0
    }
},

{
   $match:{"total_salary":{$gt:130000}}
}

])