db.dept.aggregate(
[{$lookup:
    {
        from:"faculty",
        foreignField:"deptno",
        localField:"id",
        as:"faculties"
    }
    },
    {
        $match:{"dname":"CSE"}
        }
    ]
)