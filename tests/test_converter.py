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

def test_druid_of_the_claw():
  card_id = "EX1_165"
  assert (
    Converter.convert(card_id) == np.array([
      4, #attack
      4, #hp
      5, #cost
      0, #adapt
      0, #battlecry
      0, #casts when drawn
      0, #charge
      1, #choose one
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

def test_si7_agent():
  card_id = "EX1_134"
  assert (
    Converter.convert(card_id) == np.array([
      3, #attack
      3, #hp
      3, #cost
      0, #adapt
      0, #battlecry
      0, #casts when drawn
      0, #charge
      0, #choose one
      0, #choose twice
      1, #combo
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

def test_counterspell():
  card_id = "EX1_287"
  assert (
    Converter.convert(card_id) == np.array([
      0, #attack
      0, #hp
      3, #cost
      0, #adapt
      0, #battlecry
      0, #casts when drawn
      0, #charge
      0, #choose one
      0, #choose twice
      0, #combo
      1, #counter
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
      1, #secret
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

def test_water_elemental():
  card_id = "CS2_033"
  assert (
    Converter.convert(card_id) == np.array([
      3, #attack
      6, #hp
      4, #cost
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
      1, #freeze
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
      0, #start of game
      0, #taunt
      0, #windfury
      0, #beast
      0, #demon
      0, #dragon
      1, #elemental
      0, #mech
      0, #murloc
      0, #pirate
      0, #totem
    ])
  ).all()

def test_felsoul_inquisitor():
  card_id = "GIL_527"
  assert (
    Converter.convert(card_id) == np.array([
      1, #attack
      6, #hp
      4, #cost
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
      1, #lifesteal
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
      0, #start of game
      1, #taunt
      0, #windfury
      0, #beast
      1, #demon
      0, #dragon
      0, #elemental
      0, #mech
      0, #murloc
      0, #pirate
      0, #totem
    ])
  ).all()

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
    ])
  ).all()

def test_v_07_tr_0n():
  card_id = "GVG_111t"
  assert (
    Converter.convert(card_id) == np.array([
      4, #attack
      8, #hp
      8, #cost
      0, #adapt
      0, #battlecry
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
      1, #mega-windfury
      0, #overkill
      0, #overload
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
      1, #mech
      0, #murloc
      0, #pirate
      0, #totem
    ])
  ).all()

def test_baited_arrow():
  card_id = "TRL_347"
  assert (
    Converter.convert(card_id) == np.array([
      0, #attack
      0, #hp
      5, #cost
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
      1, #overkill
      0, #overload
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

def test_possessed_lackey():
  card_id = "LOOT_306"
  assert (
    Converter.convert(card_id) == np.array([
      2, #attack
      2, #hp
      6, #cost
      0, #adapt
      0, #battlecry
      0, #casts when drawn
      0, #charge
      0, #choose one
      0, #choose twice
      0, #combo
      0, #counter
      1, #deathrattle
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
      1, #recruit
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

def test_ironbeak_owl():
  card_id = "CS2_203"
  assert (
    Converter.convert(card_id) == np.array([
      2, #attack
      1, #hp
      3, #cost
      0, #adapt
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
      0, #poisonous
      0, #quest
      0, #recruit
      0, #rush
      0, #secret
      1, #silence
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
