import time


def follow(thefile):
    thefile.seek(0, 2)    # Go to the end of file
    while True:
        next_line = thefile.readline()  # type: object
        if not next_line:
            time.sleep(0.1)    # Sleep briefly
            continue
        yield next_line

"""
    one of the most powerful application of generator is setting up processing pipelines
    Similer to shell pipes in UNIX
    Input Sequence ==> generator ==> generator ==> generator ==> for x in s:
    
    Idea: You can stack a series of generator functions together into a pipe  and pull items
    through it with a for-loop
    
    Example:
        Print all server log entires containing 'python'
"""

def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


# Set up a processing pipe : tail -f |grep python

logfile = open("test_log_file", "r")
loglines = follow(logfile)
pylines = grep("python", loglines)

# Pull results out of the processing pipeline
for line in pylines:
    print line,

"""
Yield as an expression: You could now use yield as an expression
For example, on right side of an assignment.
"""


def grep_expression(pattern):
    print "Looking for %s" % pattern
    while True:
        line = (yield)
        if pattern in line:
            print line,
