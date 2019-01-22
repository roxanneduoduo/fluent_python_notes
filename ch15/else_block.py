# except if sentence, 

"""
else sub-sentence not just used in if sentence, 
also can be used in for, while, try sentence.

for/else
    only when loop completed (for loop is not interrupted by break sentence), run else block

while/else
    only when while loop exited because condition with False value
    (when while loop is not interrupted by break sentence), run else block

try/else
    only when try block has no exception throwing, run else block
    and the exception throw in else block, will not be operated by the before except block


in all conditions, if exception or return, break or continue sentence make control jump out
to the compround sentence main block, else sentence also been skip.

"""


for item in ['aa', 'bb', 'cc']:
    if item == 'dd':
        break
else:
    raise ValueError('no dd found')

"""

try:
    dangerous_call()
except OSError:
    log('OSError...')
else:
    after_call()


"""


"""
EAFP
    easier to ask for forgiveness than permission


LBYL
    look before you leap

"""