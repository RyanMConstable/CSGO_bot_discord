import CSGOsql, dictCommands

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



#Write a function to find all top categories for a user given an id
def findusertop(steamid):
    userStats = []
    userStats.append(['Total Games:' , str(CSGOsql.findNumberOfGames(steamid))])
    userStats.append(['Kills:' , CSGOsql.findTop1user('totalkills', steamid)])
    userStats.append(['Score:' , CSGOsql.findTop1user('score', steamid)])
    userStats.append(['Team kills:' , CSGOsql.findTop1user('tk_count', steamid)])
    userStats.append(['Assists:' , CSGOsql.findTop1user('assist', steamid)])
    userStats.append(['Deaths:' , CSGOsql.findTop1user('deaths', steamid)])
    userStats.append(['5ks:' , CSGOsql.findTop1user('5k', steamid)])
    userStats.append(['4ks:' , CSGOsql.findTop1user('4k', steamid)])
    userStats.append(['3ks:' , CSGOsql.findTop1user('3k', steamid)])
    userStats.append(['2ks:' , CSGOsql.findTop1user('2k', steamid)])
    userStats.append(['1ks:' , CSGOsql.findTop1user('1k', steamid)])
    userStats.append(['Headshots:' , CSGOsql.findTop1user('headshot', steamid)])
    userStats.append(['KD:' , CSGOsql.findTop1user('kd', steamid)])
    userStats.append(['RWS:' , CSGOsql.findTop1user('rws', steamid)])
    userStats.append(['Shots Fired:' , str(CSGOsql.findTop1user('shot_count', steamid))])
    userStats.append(['Hit Count:' , str(CSGOsql.findTop1user('hit_count', steamid))])
    userStats.append(['ADR:' , str(CSGOsql.findTop1user('adr', steamid))])
    userStats.append(['Clutch won:' , str(CSGOsql.findTop1user('clutch_won_count', steamid))])
    userStats.append(['Clutch loss:' , str(CSGOsql.findTop1user('clutch_loss_count', steamid))])
    userStats.append(['Entry Frags:' , str(CSGOsql.findTop1user('entry_kill_won_count', steamid))])
    userStats.append(['Entry Death:' , str(CSGOsql.findTop1user('entry_kill_loss_count', steamid))])
    userStats.append(['Entry Deny:' , str(CSGOsql.findTop1user('entry_hold_kill_won_count', steamid))])
    userStats.append(['Entry Given:' , str(CSGOsql.findTop1user('entry_hold_kill_loss_count', steamid))])
    userStats.append(['Damage:' , str(CSGOsql.findTop1user('total_health_damage', steamid))])
    userStats.append(['Armor Dmg:' , str(CSGOsql.findTop1user('total_armor_damage', steamid))])
    userStats.append(['Damage Took:' , str(CSGOsql.findTop1user('total_health_damage_taken', steamid))])
    userStats.append(['Armor Loss:' , str(CSGOsql.findTop1user('total_armor_damage_taken', steamid))])
    userStats.append(['Kills PR:' , str(CSGOsql.findTop1user('kill_per_round', steamid))])
    userStats.append(['Assists PR:' , str(CSGOsql.findTop1user('assist_per_round', steamid))])
    userStats.append(['Deaths PR:' , str(CSGOsql.findTop1user('death_per_round', steamid))])
    userStats.append(['Alive Time:' , round(CSGOsql.findTop1user('total_time_death', steamid))])
    userStats.append(['1v1 Wins:' , str(CSGOsql.findTop1user('1v1_won_count', steamid))])
    userStats.append(['1v2 Wins:' , str(CSGOsql.findTop1user('1v2_won_count', steamid))])
    userStats.append(['1v3 Wins:' , str(CSGOsql.findTop1user('1v3_won_count', steamid))])
    userStats.append(['1v4 Wins:' , str(CSGOsql.findTop1user('1v4_won_count', steamid))])
    userStats.append(['1v5 Wins:' , str(CSGOsql.findTop1user('1v5_won_count', steamid))])
    head = ["Category", "Best"]
    return [userStats, head]



####Write a function for 
def findAvg(id, limiter):
    strVal = []
    if int(limiter) >= 50000:
        strVal.append(["Total Games", str(CSGOsql.findNumberOfGames(id))])
    else:
        strVal.append(["Total Games:", limiter])
    
    strVal.append(["Kills", round(CSGOsql.selectAvgUserStat("totalkills", id, limiter), 2)])
    strVal.append(["Score", round(CSGOsql.selectAvgUserStat("score", id, limiter), 2)])
    strVal.append(["Team Kills", round(CSGOsql.selectAvgUserStat("tk_count", id, limiter),2)])
    strVal.append(["Assists", round(CSGOsql.selectAvgUserStat("assist", id, limiter),2)])
    strVal.append(["Deaths", round(CSGOsql.selectAvgUserStat("deaths", id, limiter),2)])
    strVal.append(["Headshots", round(CSGOsql.selectAvgUserStat("headshot", id, limiter),2)])
    strVal.append(["KD", round(CSGOsql.selectAvgUserStat("kd", id, limiter),2)])
    strVal.append(["RWS", round(CSGOsql.selectAvgUserStat("rws", id, limiter),2)])
    strVal.append(["Shot Count", round(CSGOsql.selectAvgUserStat("shot_count", id, limiter),2)])
    strVal.append(["Hit Count", round(CSGOsql.selectAvgUserStat("hit_count", id, limiter),2)])
    strVal.append(["ADR", round(CSGOsql.selectAvgUserStat("adr", id, limiter),2)])
    strVal.append(["Entry Frags", round(CSGOsql.selectAvgUserStat("entry_kill_won_count", id, limiter),2)])
    strVal.append(["Entry Deaths", round(CSGOsql.selectAvgUserStat("entry_kill_loss_count", id, limiter),2)])
    strVal.append(["Total Damage", round(CSGOsql.selectAvgUserStat("total_health_damage", id, limiter),2)])
    strVal.append(["Total Damage Taken", round(CSGOsql.selectAvgUserStat("total_health_damage_taken", id, limiter),2)])
    strVal.append(["Kills Per Round", round(CSGOsql.selectAvgUserStat("kill_per_round", id, limiter),2)])
    strVal.append(["Assists Per Round", round(CSGOsql.selectAvgUserStat("assist_per_round", id, limiter),2)])
    strVal.append(["Deaths Per Round", round(CSGOsql.selectAvgUserStat("death_per_round", id, limiter),2)])
    return [["Category", "Average"], strVal]


def sortGame(gameInfo):
    return