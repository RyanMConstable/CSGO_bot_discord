from table2ascii import table2ascii as t2a, PresetStyle
from CSGO_Project import CSGOsql

#This file contains functions that get executed for the responses.py file


#Display help message tp the user
def help():
    returnString = """Commands:  
        -steamid <id> <steamkey>  
        -avg <optional Steam User>  
        -top <optional amount> <optional category> 
            <optional Steam User> 
        -leaders <optional amount> <optional category>
        
Categories:
    {totalkills, score, tk_count, assist, deaths,
5k, 4k, 3k, 2k, 1k, headshot, kd, rws, shot_count,
hit_count, flashbang_thrown, smoke_thrown,
he_thrown, molly_thrown, incendiary_thrown, decoy_thrown,
round_count, adr, clutches, clutch_won_count,
clutch_loss_count, entry_kill_won_count, entry_kill_loss_count,
entry_hold_kill_won_count, entry_hold_kill_loss_count,
rank_old, rank_new, total_health_damage, total_armor_damage,
total_health_damage_taken, total_armor_damage_taken,
kill_per_round, assist_per_round, death_per_round,
total_time_death, avg_time_death, 1v1_won_count, 1v2_won_count,
1v3_won_count, 1v4_won_count, 1v5_won_count, 1v1_loss_count, 
1v2_loss_count, 1v3_loss_count, 1v4_loss_count, 1v5_loss_count, 
1v1_count, 1v2_count, 1v3_count, 1v4_count, 1v4_count}""" 
    return returnString 