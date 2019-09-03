from potions import make_potion
from potions.potion import Potion

def test_make_python_expert_potion():
    potion = make_potion.make_python_expert_potion(name='Boring Tester')
    assert type(potion) == Potion
    return
