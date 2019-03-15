import numpy as np
from hearthstone import cardxml
from hearthstone.enums import Race
class Converter(object):
  @classmethod
  def convert(cls, entity_id):
    if not hasattr(cls, "db"):
      cls.db, _ = cardxml.load()
    if entity_id in cls.db:
      return np.array([
        cls.db[entity_id].atk,
        cls.db[entity_id].health,
        cls.db[entity_id].cost,
        int("<b>Adapt</b>" in cls.db[entity_id].description),
        int(cls.db[entity_id].battlecry),
        int("<b>Casts When Drawn</b>" in cls.db[entity_id].description),
        int("<b>Charge</b>" in cls.db[entity_id].description),
        0, #choose one
        0, #choose twice
        0, #combo
        0, #counter
        int(cls.db[entity_id].deathrattle),
        int(cls.db[entity_id].discover),
        int(cls.db[entity_id].divine_shield),
        int(cls.db[entity_id].echo),
        0, #freeze
        int(cls.db[entity_id].immune),
        int(cls.db[entity_id].inspire),
        0, #lifesteal
        0, #magnetic
        0, #mega-windfury
        0, #overkill
        int(cls.db[entity_id].overload),
        0, #passive
        int(cls.db[entity_id].poisonous),
        int(cls.db[entity_id].quest),
        0, #recruit
        int(cls.db[entity_id].rush),
        int(cls.db[entity_id].secret),
        0, #silence
        0, #start of game
        int(cls.db[entity_id].taunt),
        int(cls.db[entity_id].windfury), # LAST ABILITY
        int(cls.db[entity_id].race == Race.BEAST), # first race
        int(cls.db[entity_id].race == Race.DEMON),
        int(cls.db[entity_id].race == Race.DRAGON),
        int(cls.db[entity_id].race == Race.ELEMENTAL),
        0, # race is a MECH
        int(cls.db[entity_id].race == Race.MURLOC),
        int(cls.db[entity_id].race == Race.PIRATE),
        int(cls.db[entity_id].race == Race.TOTEM)
      ])
    else:
      raise ValueError("The following ID is not in the database: %s" % entity_id)
