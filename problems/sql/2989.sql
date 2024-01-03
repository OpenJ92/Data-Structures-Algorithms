with diff as 
(
    select
        student_id,
        assignment1 + assignment2 + assignment3 as total
    from
        Scores
)
select
    max(total) - min(total) as difference_in_score
from
    diff;
