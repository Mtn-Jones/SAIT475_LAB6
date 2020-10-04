# %%
from nltk import Prover9, Prover9Command
from nltk.sem import Expression

read_expr = Expression.fromstring

p = Prover9()
p._binary_location = r"C:\Program Files (x86)\Prover9-Mace4\bin-win32"


# %%
assumptions = [
    read_expr(p)
    for p in [
        # Every child loves Santa.
        """
        all x.( child(x) -> loves(x,Santa) )
        """,
        # Everyone who loves Santa loves any reindeer.
        """
        """,
        # Rudolph is a reindeer, and Rudolph has a red nose.
        """
        """,
        # Anything which has a red nose is weird or is a clown.
        """
        """,
        # No reindeer is a clown.
        """
        """,
        # Scrooge does not love anything which is weird.
        """
        """,
    ]
]

goal = read_expr(
    # Scrooge is not a child.
    """
    """
)


# %%
prover = Prover9Command(goal=goal, assumptions=assumptions, prover=p)

prover.print_assumptions()

print()
is_proved = prover.prove()

if is_proved:
    print("It can be proved.\nSee below:\n")
    print(prover.proof())
else:
    print("It cannot be proved")
