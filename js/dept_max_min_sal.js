db.faculty.aggregate([
{$group :
    { _id : "$deptno",
          min : {$max:"$salary"},
          max : {$min:"$salary"},
          
      }
      
},
{$project:{exp:{$sum:"$exp"}}}


])