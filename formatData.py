from CSGO_Project import CSGOsql

#Write a function to find all top categories for a user given an id
def findtopstat():
    userStats = []
    userStats.append(['Kills: ' , CSGOsql.finduserandstat('totalkills')])
    userStats.append(['Score: ' , CSGOsql.finduserandstat('score')])
    userStats.append(['Team kills: ' , CSGOsql.finduserandstat('tk_count')])
    userStats.append(['Assists: ' , CSGOsql.finduserandstat('assist')])
    userStats.append(['Deaths: ' , CSGOsql.finduserandstat('deaths')])
    userStats.append(['5ks: ' , CSGOsql.finduserandstat('5k')])
    userStats.append(['4ks: ' , CSGOsql.finduserandstat('4k')])
    userStats.append(['3ks: ' , CSGOsql.finduserandstat('3k')])
    userStats.append(['2ks: ' , CSGOsql.finduserandstat('2k')])
    userStats.append(['1ks: ' , CSGOsql.finduserandstat('1k')])
    userStats.append(['Headshots: ' , CSGOsql.finduserandstat('headshot')])
    userStats.append(['KD: ' , CSGOsql.finduserandstat('kd')])
    userStats.append(['RWS: ' , CSGOsql.finduserandstat('rws')])
    userStats.append(['Shots Fired: ' , str(CSGOsql.finduserandstat('shot_count'))])
    userStats.append(['Hit Count: ' , str(CSGOsql.finduserandstat('hit_count'))])
    userStats.append(['ADR: ' , str(CSGOsql.finduserandstat('adr'))])
    userStats.append(['Clutch won: ' , str(CSGOsql.finduserandstat('clutch_won_count'))])
    userStats.append(['Entry Frags: ' , str(CSGOsql.finduserandstat('entry_kill_won_count'))])
    userStats.append(['Entry Deaths: ' , str(CSGOsql.finduserandstat('entry_kill_loss_count'))])
    userStats.append(['Entries Denied: ' , str(CSGOsql.finduserandstat('entry_hold_kill_won_count'))])
    userStats.append(['Entries Given: ' , str(CSGOsql.finduserandstat('entry_hold_kill_loss_count'))])
    userStats.append(['Total Health Damage: ' , str(CSGOsql.finduserandstat('total_health_damage'))])
    userStats.append(['Kills Per Round: ' , str(CSGOsql.finduserandstat('kill_per_round'))])
    userStats.append(['Assists Per Round: ' , str(CSGOsql.finduserandstat('assist_per_round'))])
    userStats.append(['Deaths Per Round: ' , str(CSGOsql.finduserandstat('death_per_round'))])
    userStats.append(['1v1 Wins: ' , str(CSGOsql.finduserandstat('1v1_won_count'))])
    userStats.append(['1v2 Wins: ' , str(CSGOsql.finduserandstat('1v2_won_count'))])
    userStats.append(['1v3 Wins: ' , str(CSGOsql.finduserandstat('1v3_won_count'))])
    userStats.append(['1v4 Wins: ' , str(CSGOsql.finduserandstat('1v4_won_count'))])
    userStats.append(['1v5 Wins: ' , str(CSGOsql.finduserandstat('1v5_won_count'))])
    
    head = ["Category", "Best Recorded Game"]
    return [userStats, head]