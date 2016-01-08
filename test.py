
import rcsubmit
import time

sc = rcsubmit.StarCluster("smallcluster")
# Simple ssh command example
#sc.ssh('echo "hello world" > test')

# Copying files and running remote script
sc.push_files(['./test.sh'])
#sc.ssh('cd {} && sh test.sh > hello_world.out'.format(sc.remote_dir))
#sc.pull_files(['hello_world.out'])

# Using scheduler
sc.ssh('cd {} && qsub -V -cwd test.sh'.format(sc.remote_dir))
sleep 5
sc.pull_files(['hello_world.out'])

#submission = rcsubmit.Submission(sc, 'qsub', 'job.pbs', 'test.sh')
#submission.run()

