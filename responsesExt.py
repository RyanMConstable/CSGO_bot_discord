from table2ascii import table2ascii as t2a, PresetStyle
from CSGO_Project import CSGOsql

#This file contains functions that get executed for the responses.py file


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