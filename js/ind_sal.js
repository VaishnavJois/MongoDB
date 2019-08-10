/*db.faculty.aggregate([

{$project:
    {
        _id:0,name:"$name",sal:"$salary",
        t_sal:{$multiply:[{$sum:["$salary","$bonus"]},12]}
    }
}

])
*/

/*
db.faculty.aggregate(
[
{
    $group:{_id:"$deptno",f_list:{$push:"$name"}}
    },
{
    $project:{"deptno":"$_id","faculties":"$f_list",_id:0}
    }
]
)
    
    */
 


/* 
db.faculty.aggregate(
[
{
    $group:{_id:0,f_list:{$addToSet:"$name"}}
    },
{
    $project:{"faculties":"$f_list",_id:0}
    }
]
)
    
    db.faculty.aggregate(
[
{
    $group:{_id:0,f_list:{$push:"$name"}}
    },
{
    $project:{"faculties":"$f_list",_id:0}
    }
]
)
  */  
db.faculty.aggregate(
[
{$unwind:"$subjects"},
{$match:{"subjects":"JAVA"}},
{$unwind:"$rating"},
{$match:{"rating":7}},
{$project:
    {
        "Name":"$name",
        "State":"$address.state",
        _id:0,
        "Rating":"$rating"
    }},
    {$out:"java_faculty"}
 
]
)
    