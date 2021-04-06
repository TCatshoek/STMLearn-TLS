import tempfile

from stmlearn.equivalencecheckers import WmethodEquivalenceChecker
from stmlearn.equivalencecheckers._wmethod import SmartWmethodEquivalenceChecker
from stmlearn.learners import LStarMealyLearner, TTTMealyLearner
from stmlearn.suls import MealyState, MealyMachine
from stmlearn.teachers import Teacher
from stmlearn.suls.caches.dictcache import DictCache
from TLSSUL import TLSSUL
from TLSAttackerMapper import TLSAttackerMapper

sul = DictCache(
    storagepath='cache/1_0_1g',
    saveinterval=1,
    sul=TLSSUL(TLSAttackerMapper(
            tlsa_path='/home/tom/projects/tlsattacker/TLS-Attacker/apps/TLS-Client.jar'
    ))
).load()

# Use the W method equivalence checker
eqc = SmartWmethodEquivalenceChecker(sul, horizon=2)

teacher = Teacher(sul, eqc)

# We are learning a mealy machine
learner = LStarMealyLearner(teacher)

hyp = learner.run(show_intermediate=True)

hyp.render_graph(tempfile.mktemp('.gv'))