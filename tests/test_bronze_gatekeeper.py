import numpy as np
from converter import Converter

def test_bronze_gatekeeper():
  card_id = "BOT_021"
  assert (
    Converter.convert(card_id) == np.array([
      1, #attack
      5, #hp
      3, #cost
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
      1, #magnetic
      0, #mega-windfury
      0, #overkill
      0, #overload
      0, #poisonous
      0, #quest
      0, #recruit
      0, #rush
      0, #secret
      0, #silence
      0, #start of game
      1, #taunt
      0, #windfury
      0, #beast
      0, #demon
      0, #dragon
      0, #elemental
      1, #mech
      0, #murloc
      0, #pirate
      0, #totem
      0  #spell
    ])
  ).all()
