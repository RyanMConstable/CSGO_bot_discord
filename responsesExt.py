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
    commands = "Commands:\n\t"
    commands += "-steamid <id> <steamkey>\n\t"
    commands += "avg <optional steam user>\n\t"
    commands += "top <optional amount> <optional category> <optional steam user>\n\t"
    commands += "-leaders <optional amount> <optional category>\n\n"
    commands += "Categories:\n\t"
      

    dictionaryKeys = []
    for key in commandsToCol:
        dictionaryKeys.append(key)
    
    return commands + str(dictionaryKeys)


def steamid(discordID, steamID, steamKEY):
    try:
        CSGOsql.setDiscordUser(discordID, steamID, steamKEY)
    except:
        errorMSG = "Incorrect Input try '-steamid <id> <key>'\n"
        errorMSG += "Steam key is found here as 'Authentication key': "
        errorMSG += "https://help.steampowered.com/en/wizard/HelpWithGameIssue/?appid=730&issueid=128"
        return errorMSG
    return "SteamID updated"