# DB connection here


"""
Design Decision

don't use ORM's
- they hide complexity
- they produce inefficient, un-followable SQL
- they are slow
- they allow performance leaks to slip through the cracks
- they don't always support DB specific features
- they are bloated
- they don't let you learn actual SQL
"""


"""
use DyanamoDB
- very flexible
- pay by scale (vs AWS RDS which is pay for fixed size --> unused space)
- integrates really well with other cloud services
"""
