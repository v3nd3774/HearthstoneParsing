import numpy as np
from converter import Converter
def test_leeroy():
  card_id = "EX1_116"
  assert (
    Converter.convert(card_id) == np.array([
      6, #attack
      2, #hp
      5, #cost
      0, #adapt
      1, #battlecry
      0, #casts when drawn
      1, #charge
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
      0, #passive
      0, #poisonous
      0, #quest
      0, #recruit
      0, #rush
      0, #secret
      0, #silence
      0, #start of game
      0, #taunt
      0, #windfury
      0, #beast
      0, #demon
      0, #dragon
      0, #elemental
      0, #mech
      0, #murloc
      0, #pirate
      0, #totem
    ])
  ).all()

def test_verdant_longneck():
  card_id = "UNG_100"
  assert (
    Converter.convert(card_id) == np.array([
      5, #attack
      4, #hp
      5, #cost
      1, #adapt
      1, #battlecry
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
      0, #passive
      0, #poisonous
      0, #quest
      0, #recruit
      0, #rush
      0, #secret
      0, #silence
      0, #start of game
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

def test_spider_ambush():
  card_id = "LOOT_026e"
  assert (
    Converter.convert(card_id) == np.array([
      0, #attack
      0, #hp
      4, #cost
      0, #adapt
      0, #battlecry
      1, #casts when drawn
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
      0, #passive
      0, #poisonous
      0, #quest
      0, #recruit
      0, #rush
      0, #secret
      0, #silence
      0, #start of game
      0, #taunt
      0, #windfury
      0, #beast
      0, #demon
      0, #dragon
      0, #elemental
      0, #mech
      0, #murloc
      0, #pirate
      0, #totem
    ])
  ).all()
