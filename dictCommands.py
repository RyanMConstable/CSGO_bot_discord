#Dictionary: keys = the pretty command the user types in 
#            items are the column names in the db
commandsToCol = {}
commandsToCol["kills"] = "totalkills"
commandsToCol["totalkills"] = "totalkills"
commandsToCol["kill"] = "totalkills"
commandsToCol["score"] = "score"
commandsToCol["teamkills"] = "tk_count"
commandsToCol["tk"] = "tk_count"
commandsToCol["assists"] = "assist"
commandsToCol["deaths"] = "deaths"
commandsToCol["5k"] = "5k"
commandsToCol["4k"] = "4k"
commandsToCol["3k"] = "3k"
commandsToCol["2k"] = "2k"
commandsToCol["1k"] = "1k"
commandsToCol["headshots"] = "headshot"
commandsToCol["head"] = "headshot"
commandsToCol["hd"] = "headshot"
commandsToCol["kd"] = "kd"
commandsToCol["rws"] = "rws"
commandsToCol["shotsfired"] = "shot_count"
commandsToCol["shots"] = "shot_count"
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
commandsToCol["damage"] = "total_health_damage"
commandsToCol["totalarmordamage"] = "total_armor_damage"
commandsToCol["tad"] = "total_armor_damage"
commandsToCol["totaldamagetaken"] = "total_health_damage_taken"
commandsToCol["tdt"] = "total_health_damage_taken"
commandsToCol["totalarmordamagetaken"] = "total_armor_damage_taken"
commandsToCol["tadt"] = "total_armor_damage_taken"
commandsToCol["killperround"] = "kill_per_round"
commandsToCol["kpr"] = "kill_per_round"
commandsToCol["assistperround"] = "assist_per_round"
commandsToCol["apr"] = "assist_per_round"
commandsToCol["deathperround"] = "death_per_round"
commandsToCol["dpr"] = "death_per_round"
commandsToCol["totaldeathtime"] = "total_time_death"
commandsToCol["deathtime"] = "total_time_death"
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




gameStatsColumns = []
gameStatsColumns += ["Kills", "Score", "TK", "Assist", "Deaths", "5k", "4k", "3k", "2k", "1k", "HEAD", "KD", "RWS", "Shots", "Hits", "Flashes", "HE", "Molly"]
gameStatsColumns += ["Incen", "Decoy", "Rounds", "Date", "ADR", "Clutch", "ClutchW", "ClutchL", "EntryW", "EntryL"]
gameStatsColumns += ["HoldW", "HoldL", "OldRank", "NewRank", "DmgDone", "ArmDmg", "DmgLoss"]
gameStatsColumns += ["ArmTook", "KPR", "APR", "DPR", "DeathTm", "AvgTmLi", "1v1Won", "1v2Won"]
gameStatsColumns += ["1v3Won", "1v4Won", "1v5Won", "1v1Loss", "1v2Loss", "1v3Loss", "1v4Loss", "1v5Loss", "1v1Tot", "1v2Tot"]
gameStatsColumns += ["1v3Tot", "1v4Tot", "1v5Tot"]


max_index = 0
for item in range(len(gameStatsColumns)):
    if len(gameStatsColumns[item]) > len(gameStatsColumns[max_index]):
        max_index = item
print(max_index, gameStatsColumns[max_index], len(gameStatsColumns[max_index]))