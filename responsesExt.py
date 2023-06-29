from table2ascii import table2ascii as t2a, PresetStyle
from CSGO_Project import CSGOsql

#This file contains functions that get executed for the responses.py file

#Dictionary: keys = the pretty command the user types in 
#            items are the column names in the db
commandsToCol = {}
commandsToCol["kills"] = "totalkills"
commandsToCol["score"] = "score"
commandsToCol["teamkills"] = "tk_count"
commandsToCol["assists"] = "assist"
commandsToCol["deaths"] = "deaths"
commandsToCol["5k"] = "5k"
commandsToCol["4k"] = "4k"
commandsToCol["3k"] = "3k"
commandsToCol["2k"] = "2k"
commandsToCol["1k"] = "1k"
commandsToCol["headshots"] = "headshot"
commandsToCol["kd"] = "kd"
commandsToCol["rws"] = "rws"
commandsToCol["shotsfired"] = "shot_count"
commandsToCol["shotslanded"] = "hit_count"
commandsToCol["flashes"] = "flashbang_thrown"
commandsToCol["smokes"] = "smoke_thrown"
commandsToCol["he"] = "he_thrown"
commandsToCol["mollys"] = "molly_trown"
commandsToCol["incens"] = "incendiary_thrown"
commandsToCol["decoys"] = "decoy_thrown"
commandsToCol["rounds"] = "round_count"
commandsToCol["adr"] = "adr"
commandsToCol["clutches"] = "clutches"
commandsToCol["clutcheswon"] = "clutch_won_count"
commandsToCol["clutcheslost"] = "clutch_loss_count"
commandsToCol["entrykills"] = "entry_kill_won_count"
commandsToCol["entrydeaths"] = "entry_kill_loss_count"
commandsToCol["entriesdenied"] = "entry_hold_kill_won_count"
commandsToCol["entriesgiven"] = "entry_hold_kill_loss_count"
commandsToCol["oldrank"] = "rank_old"
commandsToCol["newrank"] = "rank_new"
commandsToCol["totaldamage"] = "total_health_damage"
commandsToCol["totalarmordamage"] = "total_armor_damage"
commandsToCol["totaldamagetaken"] = "total_health_damage_taken"
commandsToCol["totalarmordamagetaken"] = "total_armor_damage_taken"
commandsToCol["killperround"] = "kill_per_round"
commandsToCol["assistperround"] = "assist_per_round"
commandsToCol["deathperround"] = "death_per_round"
commandsToCol["totaldeathtime"] = "total_time_death"
commandsToCol["avgdeathtime"] = "avg_time_death"
commandsToCol["1v1won"] = "1v1_won_count"
commandsToCol["1v2won"] = "1v2_won_count"
commandsToCol["1v3won"] = "1v3_won_count"
commandsToCol["1v4won"] = "1v4_won_count"
commandsToCol["1v5won"] = "1v5_won_count"
commandsToCol["1v1loss"] = "1v1_loss_count"
commandsToCol["1v2loss"] = "1v2_loss_count"
commandsToCol["1v3loss"] = "1v3_loss_count"
commandsToCol["1v4loss"] = "1v4_loss_count"
commandsToCol["1v5loss"] = "1v5_loss_count"
commandsToCol["1v1total"] = "1v1_count"
commandsToCol["1v2total"] = "1v2_count"
commandsToCol["1v3total"] = "1v3_count"
commandsToCol["1v4total"] = "1v4_count"
commandsToCol["1v5total"] = "1v5_count"

#Display help message tp the user
def help():
    commands = """Commands:
        -steamid <id> <steamkey>
        -avg <optional Steam User>
        -top <optional amount> <optional category>
    <optional Steam User>
        -leaders <optional amount> <optional category>\n\n"""   
    
    categories = "Categories:\n\t"
    categories += "[totalkills, score, tk_count, assist, deaths, 5k, 4k, 3k, 2k, 1k, headshot"
    categories += ", kd, rws, shot_count, hit_count, flashbang_thrown, smoke_thrown, he_thrown"
    categories += ", molly_trown, incendiary_thrown, decoy_thrown, round_count, adr, clutches,"
    categories += " clutch_won_count, clutch_loss_count, entry_kill_won_count, entry_kill_loss_count,"
    categories += " entry_hold_kill_won_count, entry_hold_kill_loss_count, rank_old, rank_new, total_health_damage"
    categories += ", total_armor_damage, total_health_damage_taken, total_armor_damage_taken, "
    categories += "kill_per_round, assist_per_round, death_per_round, total_time_death, avg_time_death"
    categories += "1vX_won_count, 1vX_loss_count, 1vX_count]"   
    
    return commands + categories