#for debug

from modules.qlearn import qagent

q = qagent.Qagent(0.1, 0.1, 2)
q.load()
request = 111011021201000
act = [0, 0]
print(q.select_q(request, act))
