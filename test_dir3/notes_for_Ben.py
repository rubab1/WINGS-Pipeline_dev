#! /usr/bin/env python

#myJob  = Job.get(job_id)

comp_name1 = 'completed'+testname1
comp_name2 = 'completed'+testname2


options = {comp_name1:0, comp_name2:0}

_opt = Options(options).create('job',int(job_id))

# to retrieve options for a job, we know job_id

_opt = Options.get('job',int(job_id))

temp1 =  _opt[comp_name1]

==================


parent_event = Event.get(event_id)

parent_job_id = parent_event.job_id


