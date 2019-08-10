db.faculty.aggregate([

{$project:
    {
        _id:0,name:"$name",sal:"$salary",
        bouns:"$bonus",t_sal:{$sum:["salary","$bonus"]}
    }
}

])