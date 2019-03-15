import numpy as np
from converter import Converter

def test_baku_the_mooneater():
  card_id = "GIL_826"
  assert (
    Converter.convert(card_id) == np.array([
      7, #attack
      8, #hp
      9, #cost
      0, #adapt
      0, #battlecry
      0, #casts when drawn
      0, #charge
      0, #choose one
      0, #choose twice
      0, #combo
      0, #counter
      0, #deathrattle
      0, #discover
      0, #divine shield
      0, #echo
      0, #freeze
      0, #immune
      0, #inspire
      0, #lifesteal
      0, #magnetic
      0, #mega-windfury
      0, #overkill
      0, #overload
      0, #poisonous
      0, #quest
      0, #recruit
      0, #rush
      0, #secret
      0, #silence
      1, #start of game
      0, #taunt
      0, #windfury
      1, #beast
      0, #demon
      0, #dragon
      0, #elemental
      0, #mech
      0, #murloc
      0, #pirate
      0, #totem
    ])
  ).all()
