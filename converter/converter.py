import re
import numpy as np
from hearthstone import cardxml
from hearthstone.enums import CardType, Race
class Converter(object):
  @classmethod
  def convert(cls, entity_id):
    if not hasattr(cls, "db"):
      cls.db, _ = cardxml.load()
    if not hasattr(cls, "choose_one_regex"):
      cls.choose_one_regex = re.compile(r".*?<b>Choose One -<\/b>(.*?);\n(.+)",  re.DOTALL)
    if not hasattr(cls, "choose_two_regex"):
      cls.choose_two_regex = re.compile(r".*?<b>Choose Twice -</b>(.*?);(.*?);(.*?)$",  re.DOTALL)
    choose_one_regex_match = cls.choose_one_regex.match(cls.db[entity_id].description)
    choose_two_regex_match = cls.choose_two_regex.match(cls.db[entity_id].description)
    if entity_id in cls.db:
      return np.array([
        cls.db[entity_id].atk,
        cls.db[entity_id].health,
        cls.db[entity_id].cost,
        int("<b>Adapt</b>" in cls.db[entity_id].description),
        int(cls.db[entity_id].battlecry),
        int("<b>Casts When Drawn</b>" in cls.db[entity_id].description),
        int("<b>Charge</b>" in cls.db[entity_id].description and not choose_one_regex_match),
        int(bool(choose_one_regex_match)),
        int(bool(choose_two_regex_match)),
        int("<b>Combo:</b>" in cls.db[entity_id].description),
        int("<b>Counter</b>" in cls.db[entity_id].description),
        int(cls.db[entity_id].deathrattle),
        int(cls.db[entity_id].discover),
        int(cls.db[entity_id].divine_shield),
        int(cls.db[entity_id].echo),
        int("<b>Freeze</b>" in cls.db[entity_id].description),
        int(cls.db[entity_id].immune),
        int(cls.db[entity_id].inspire),
        int("<b>Lifesteal</b>" in cls.db[entity_id].description),
        int("<b>Magnetic</b>" in cls.db[entity_id].description),
        int("<b>Mega-Windfury</b>" in cls.db[entity_id].description),
        int("<b>Overkill:</b>" in cls.db[entity_id].description),
        int(cls.db[entity_id].overload),
        int(cls.db[entity_id].poisonous),
        int(cls.db[entity_id].quest),
        int("<b>Recruit</b>" in cls.db[entity_id].description),
        int(cls.db[entity_id].rush),
        int(cls.db[entity_id].secret),
        int("<b>Silence</b>" in cls.db[entity_id].description),
        int("<b>Start of Game:</b>" in cls.db[entity_id].description),
        int(cls.db[entity_id].taunt),
        int(cls.db[entity_id].windfury), # LAST ABILITY
        int(cls.db[entity_id].race == Race.BEAST), # first race
        int(cls.db[entity_id].race == Race.DEMON),
        int(cls.db[entity_id].race == Race.DRAGON),
        int(cls.db[entity_id].race == Race.ELEMENTAL),
        int(cls.db[entity_id].race == Race.MECHANICAL),
        int(cls.db[entity_id].race == Race.MURLOC),
        int(cls.db[entity_id].race == Race.PIRATE),
        int(cls.db[entity_id].race == Race.TOTEM),
        int(cls.db[entity_id].type == CardType.SPELL)
      ])
    else:
      raise ValueError("The following ID is not in the database: %s" % entity_id)
