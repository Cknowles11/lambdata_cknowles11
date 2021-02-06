# Keep track of all the queries you create for the assignment

TOTAL_CHARACTERS = """SELECT count(distinct character_id) as
TOTAL_CHARACTERS FROM charactercreator_character"""

TOTAL_SUBCLASS = """ """


TOTAL_ITEMS = """SELECT count(distinct item_id) as TOTAL_ITEMS
FROM armory_item"""


WEAPONS = """SELECT count(distinct item_ptr_id) as WEAPONS
FROM armory_weapon"""


NON_WEAPONS = """SELECT
(SELECT count(distinct item_id) FROM armory_item)
-(SELECT count(distinct item_ptr_id) FROM armory_weapon) as NON_WEAPONS"""


CHARACTER_ITEMS = """SELECT character_id
,count(distinct item_id) as CHARACTER_ITEMS
FROM charactercreator_character_inventory
GROUP BY character_id
ORDER BY CHARACTER_ITEMS DESC
LIMIT 20"""


CHARACTER_WEAPONS = """SELECT character_id
,count(distinct item_ptr_id) as CHARACTER_WEAPONS
FROM(
    SELECT
    charactercreator_character_inventory.character_id
    ,charactercreator_character_inventory.item_id

    ,armory_weapon.item_ptr_id

    FROM charactercreator_character_inventory

    INNER JOIN armory_weapon
    ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
) subq
GROUP BY character_id
ORDER BY CHARACTER_WEAPONS DESC
"""


AVG_CHARACTER_ITEMS = """SELECT avg(character_items) as AVG_CHARACTER_ITEMS
FROM(
    SELECT
    character_id
    ,count(distinct item_id) as character_items
    FROM charactercreator_character_inventory
    GROUP BY character_id
    Limit 20
    ) subq"""


AVG_CHARACTER_WEAPONS = """SELECT avg(character_weapons) AS AVG_CHARACTER_WEAPONS
FROM(
    SELECT character_id
	,count(item_ptr_id) as character_weapons
    FROM(
        SELECT
        charactercreator_character_inventory.character_id
        ,charactercreator_character_inventory.item_id

        ,armory_weapon.item_ptr_id

        FROM charactercreator_character_inventory

        INNER JOIN armory_weapon
        ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
        )
        GROUP BY character_id
    )subq"""
