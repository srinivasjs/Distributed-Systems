from celery import Celery

# Celery instantiation
app = Celery()

print app
print dir(app)

# Output :
# <Celery __main__:0x7f2789d1ca10> >> Since, Celery was instantiated without name
# __main__ is been taken

app1 = Celery("hello world")

# output
# <Celery hello world:0x7fd16de5da10>  >> Celery System instantiated with "hello world" name

# So, now in the same process space two Celery Processes exists which can have it's own 
# Configurations, Tasks (as specified in README)
