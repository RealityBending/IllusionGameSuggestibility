import json
import os

import numpy as np
import pandas as pd
import seaborn as sns

# Incentivized ===================================================================

sona_credited = [
    27027,
    28388,
    29913,
    29761,
    30081,  # Doesn't show up in records
    30102,
    30605,
    30611,
    30617,  # Doesn't show up in records
    30618,
    30623,
    30624,
    30625,
    30631,
    30629,
    30633,
    30634,
    30636,
    30645,
    30644,
    30647,
    30649,
    30660,
    30664,
    30661,
    30668,
    30669,
    30675,
    30679,
    30681,
    30682,
    30694,
    30695,
    30697,
    30699,
    30703,
    30712,
    30716,  # Doesn't show up in records
    30722,
    30725,
    31729,
    30733,
    30737,
    30746,
    30748,  # Award 0 but not in records
    30749,  # Awarded 0
    30754,
    30756,
    30758,
    30760,
    30762,
    30768,
    31770,
    30772,
    30773,
    30777,
    30779,
    30783,
    30784,
    30785,
    31788,
    30791,
    30794,
    30800,
    30802,
    30804,
    30806,
    30809,
    30817,
    30818,
    30824,  # Awarded 0
    30839,
    30827,
    30832,
    30844,
    30845,
    30848,
    30850,
    30854,  # Doesn't show up in records
    30857,
    30862,
    30863,
    30867,
    30868,
    30872,
    30876,
    30880,
    30884,
    30885,
    30888,
    30889,
    30895,
    30896,
    30901,
    30905,
    30924,
    30925,
    30950,
    30935,  # Doesn't show up in records
    30939,
    30956,
    30948,
    30953,
    30954,
    30966,
    30971,
    30993,
    31001,
    31003,
    31006,
    31018,
    31025,
    31032,
    31037,
    31039,
    31046,
    31047,
    31050,
    31060,
    31065,
    31073,
    31075,  # Doesn't show up in records
    31080,
    31086,
    31087,
    31100,
    31107,
    31110,
    31101,
    31111,
    31114,
    31667,
    31673,
    31717,
    31720,
    31723,
    31726,
    31727,
    31728,
    31731,
    31734,
    31736,
    31741,
    31742,
    31745,
    31747,
    31748,
    31753,
    31754,
    31756,
    31757,
    31758,
    31759,
    31761,
    31762,
    31766,
    31768,
    31769,
    31771,
    31774,
    31776,
    31777,
    31778,
    31782,
    31783,
    31787,
    31796,
    31799,
    31801,
    31803,
    31807,
    31808,
    31809,
    31810,
    31811,
    31814,
    31817,
    31820,
    31821,
    31822,
    # 31824,  not in list
    31830,
    31833,
    31834,
    31835,
    31836,
    31837,
    31838,
    31839,
    31840,
    31841,
    31843,
    31844,
    31845,
    31849,
    31851,
    31852,  # Awarded 0
    31856,
    31857,
    31862,
    31863,
    31864,
    31865,
    31869,
    31874,
    31827,
    31852,
    31853,
    31867,
    31868,
    31877,
    31880,
    31881,
    31885,
    31886,
    31889,
    31891,
    31895,
    31896,
    31897,
    31902,
    31903,
    31907,
    31911,
    31913,
    31914,
    31915,
    31918,
    31920,
    31923,
    31925,
    31928,  # Not in list
    31929,
    31930,
    31935,
    31937,
    31938,
    31940,
    31943,
    31944,
    31946,
    31950,
    31953,
    31955,
    31956,
    31957,
    31958,
    31959,
    31960,
    31961,  # Awarded half
    31962,
    31967,
    31968,  # Awarded half
    31970,
    31972,
    31973,
    31974,
    31975,
    31978,
    31981,
    31984,
    31985,
    31987,
    31988,
    31992,
    31997,
    32001,
    32002,
    32003,
    32007,
    32012,
    32013,
    32014,
    32018,
    32021,
    32022,
    32023,
    32026,
    32027,
    32028,
    32030,
    32033,
    32034,
    32036,
    32038,
    32041,
    32042,  # Doesn't show up in records
    32043,
    32045,
    32046,
    32047,
    32048,
    32050,
    32052,
    32054,
    32055,
    32056,
    32057,
    32058,
    32060,
    32062,
    32064,
    32065,
    32067,
    32068,
    32070,
    32071,
    32074,
    32076,
    32077,
    32078,
    32080,
    32081,
    32083,
    32084,
    32085,
    32086,
    32088,
    32089,
    32090,  # Awarded 0
    32091,
    32097,
    32098,
    32101,
    32102,
    32105,
    32106,
    32107,
    32108,
    32109,
    32110,
    32114,
    32115,
    32116,
    32117,
    32119,
    32121,
    32129,
    32133,
    32138,
    32123,
    32136,  # Awarded half
    32147,
    32148,
    32151,
    32152,
    32159,
    32155,
    32158,
    32160,
    32161,
    32163,
    32165,
    32168,
    32173,
    32174,
    32175,
    32178,
    32179,
    32180,
    32182,
    32184,
    32186,
    32188,
    32191,
    32232,
    32244,
    32252,  # Awarded 0
    32260,
    # 15/10/2024
    31781,
    31805,
    31850,
    31854,
    31965,
    32061,
    32140,
    32146,
    32150,
    32294,
    32314,
    32330,
    32331,
    32358,
    32362,
    32365,
    32367,
    32373,
    32374,
    32376,
    32380,
    32381,
    32385,
    32386,
    32387,
    32391,
    32399,
    32408,
    32426,
    32428,
    32435,
    32436,
    32444,
    32452,
    32453,
    32462,
    32469,
    32484,
    32497,
    32502,
    32510,
    32534,
    32559,
    32567,
    32568,
    32574,
    32576,
    32585,
    32593,
    32603,
    32643,
    32645,
    32648,
    32650,
    32651,
    32658,
    32663,
    32664,
    32670,
    32680,
    32684,
    32691,
    32699,
    32708,
    32716,
    32722,
    32726,
    32731,
    32735,
    32738,
    32746,
    32749,
    32753,
    32756,
    32757,
    32761,
    32762,
    32773,
    32774,
    32779,
    32796,
    # 03/11/2024
    32286,
    32287,
    32293,
    32311,
    32327,
    32341,
    32349,
    32368,
    32371,
    32375,
    32394,
    32406,
    32468,
    32486,
    32489,
    32491,
    32494,
    32498,
    32500,
    32501,
    32511,
    32517,
    32528,
    32533,
    32579,
    32582,
    32615,
    32616,
    32652,
    32672,
    32675,
    32686,
    32695,
    32711,
    32718,
    32720,
    32727,
    32765,
    32767,
    32769,  # not in list
    32772,
    32798,
    30663,
    31732,
    31791,
    31812,
    31824,  # not in list
    31883,
    31921,
    31977,
    32131,
    32169,
    32291,
    32300,
    32306,
    32307,
    32335,
    32338,
    32353,
    32410,
    32412,
    32416,
    32427,
    32432,
    32437,
    32446,
    32456,
    32460,
    32471,
    32480,
    32483,
    32520,
    32523,
    32529,  # not in list
    32547,
    32563,
    32564,
    32575,
    32606,
    32622,
    32628,
    32629,
    32642,
    32647,
    32649,
    32653,  # not in list
    32660,
    32673,
    32713,
    32729,
    32743,
    32758,
    32768,
    32780,
    # 23/11/2024
    31738,
    31749,
    31785,  # not in list
    31795,
    31825,
    31942,
    31952,
    31976,
    32025,  # not in list
    32093,
    32318,
    32320,
    32322,
    32383,
    32423,
    32448,
    32481,
    32504,
    32507,
    32519,
    32537,
    32583,
    32618,
    32687,
    32724,
    32737,
    32783,
    # 04/12/2024
    32422,
    32748,
    31846,
    32447,
    32134,
    32587,
    32288,
    31873,
    30657,  # not in list
    32305,
    30672,
    32697,
    32332,
    32550,
    32072,
    32690,
    32619,
    32544,
    32478,
    32589,
    32621,
    31876,  # not in list
    32678,
    30687,
    32094,
    31859,
    32490,
    32113,  # not in list
    32698,
    32815,
    32609,
    32814,
    32389,
    31751,
    32556,
    32776,
    32554,
    31900,
    32465,
    32069,
    32625,
    32290,  # not in list
    31772,
    # 06/12/2024
    29932,
    31800,
    31947,
    32005,
    32122,
    32142,
    32153,
    32183,
    32351,
    32405,
    32509,
    32742,
    # 29/03/2025
    31904,
    31980,
    32392,
    32496,
    32513,
    # Outliers (Low effort participation for the 2nd phase. Awarding half.)
    32505,
    32442,
    32379,
    32304,
]


# path = "C:/Users/domma/Box/Data/IllusionGameSuggestibility/"
path = "C:/Users/dmm56/Box/Data/IllusionGameSuggestibility/"
files = os.listdir(path)


# Loop through files ======================================================
alldata_sub = pd.DataFrame()  # Initialize empty dataframe
alldata_ig = pd.DataFrame()  # Initialize empty dataframe
prolific_ids = {}

for i, file in enumerate(files):
    print(f"File N°{i+1}/{len(files)}")

    filename = file.replace(".csv", "")

    if len(alldata_sub) > 0:
        if filename in alldata_sub["Participant"].values:
            continue

    data = pd.read_csv(path + file)

    # Participant ========================================================
    # data["screen"].unique()

    # Browser info -------------------------------------------------------
    browser = data[data["screen"] == "browser_info"].iloc[0]

    # Experimenter
    if "experimenter" in browser.index:
        experimenter = "Experimenter1"
    else:
        experimenter = browser["researcher"]
    if "prolific_id" in browser.index:
        if isinstance(browser["prolific_id"], str):
            experimenter = "Prolific"
    if isinstance(experimenter, float):
        if np.isnan(experimenter):
            experimenter = np.nan
        else:
            experimenter = "Experimenter" + str(int(experimenter))
    if experimenter == "test":
        continue

    df = pd.DataFrame(
        {
            "Participant": filename,
            "Experimenter": experimenter,
            "Experiment_Duration": data["time_elapsed"].max() / 1000 / 60,
            "Date": browser["date"],
            "Time": browser["time"],
            "Browser": browser["browser"],
            "Mobile": browser["mobile"],
            "Platform": browser["os"],
            "Screen_Width": browser["screen_width"],
            "Screen_Height": browser["screen_height"],
        },
        index=[0],
    )

    if experimenter == "Prolific":
        id = browser["prolific_id"]
        if id not in [
            "5d9b60eb027b56001220d84e",
            "631745a70c7c585248df1a5d",
            "5714e0958adadb00098deed4",
            "59d4fac0d1ab390001da2e46",
            "5ed934c19e6b4a496cd6da06",
            "645bc6fcd55cf9db562b97f8",
        ]:
            prolific_ids[filename] = id

    if "sona_id" in browser.index:
        if np.isnan(browser["sona_id"]) == False:
            id = int(browser["sona_id"])
            df["SONA_ID"] = id

    # Demographics -------------------------------------------------------
    demo1 = data[data["screen"] == "demographics_1"].iloc[0]
    demo1 = json.loads(demo1["response"])

    demo2 = data[data["screen"] == "demographics_2"].iloc[0]
    demo2 = json.loads(demo2["response"])

    df["Gender"] = demo1["gender"]
    df["Age"] = demo2["age"]

    # Education
    edu = demo1["education"]
    edu = "Bachelor" if "bachelor" in edu else edu
    edu = "Master" if "master" in edu else edu
    edu = "Doctorate" if "doctorate" in edu else edu
    edu = "High School" if "High school" in edu else edu
    df["Education"] = edu

    # Ethnicity
    race = demo2["ethnicity"].title().rstrip()
    race = (
        "White"
        if race
        in [
            "Caucasian",
            "British",
            "White British",
            "Czech",
            "European",
            "Nederlander",
            "British White",
            "Bulgarian",
            "Caucasion",
            "Causasian",
            "English",
            "Greek",
            "Other White",
            "Polish",
            "White - Czech",
            "White (British)",
            "White Other",
            "White, British",
            "White",
            "White European",
            "Hwhite",
            "Serbian",
            "British - White",
            "Causian",
            "White Caucasian",
            "White British Caucasian",
            "White Other Background",
            "Italian",
            "Britsih Asian",
            "White - British",
            "White English",
            "Portuguese",
            "Caucasain",
            "Cypriot",
            "Cucasion",
            "Caucasian White British",
            "Danish",
            "Caucasioan",
        ]
        else race
    )
    race = (
        "Mixed"
        if race
        in [
            "Caucasion Metis",
            "Mixt",
            "Black/British Other",
            "White/ Asian",
            "White Asian",
            "Southeast Asian And White",
            "Indian/Mozambican",
            "White And Black Caribbean",
            "White & Asian",
            "White British/Arab",
        ]
        else race
    )
    race = "Mixed" if "Mixed" in race else race
    race = (
        "South Asian"
        if race
        in ["Indian", "Bengali", "British Indian", "Pakistani", "British Sri Lankan", "Bangladeshi", "Sri Lankan"]
        else race
    )
    race = (
        "Asian"
        if race
        in [
            "Asian-British",
            "Asian British",
            "Chinese",
            "Other Asian Background",
            "South East Asian",
            "British Asian",
            "East Asian",
        ]
        else race
    )
    race = (
        "Black"
        if race
        in [
            "Black African",
            "Black Carribean",
            "Black/African/Caribbean/Black British",
            "British Caribbean",
            "Black African Caribbean",
            "Black British",
        ]
        else race
    )
    race = "Hispanic" if race in ["South American", "Caucasian / Latino", "Brazilian"] else race
    race = (
        "Middle Eastern"
        if race
        in [
            "Arab - English",
            "Egyptian",
            "Turkish",
            "North African",
            "North  African",
            "Arab",
            "Afghan",
            "Middle-Eastern / White British",
        ]
        else race
    )
    race = (
        "Other"
        if race
        in [
            "Native American",
            "Filipino",
            "Polynesian",
        ]
        else race
    )

    race = np.nan if race in ["", "Br", "Prefer Not To Say"] else race
    df["Ethnicity"] = race

    # Questionnaires =====================================================

    # Manual fix (2 first participants had duplicated questionnaires)
    if filename in ["8va2haolh5", "exgf9of50l"]:
        data.loc[data["screen"][data["trial_type"] == "survey"].index, "screen"] = "questionnaire_mist"
        if filename == "exgf9of50l":
            data = data.drop(data[data["screen"] == "questionnaire_mist"].index[1])
            data = data.drop(data[data["screen"] == "questionnaire_ipip6"].index[1])
        else:
            data = data.drop(data[data["screen"] == "questionnaire_mist"].index[0])
            data = data.drop(data[data["screen"] == "questionnaire_pid5"].index[0])

    df = df.copy()  # Defragment dataframe

    # Questionnaire Order ------------------------------------------------
    # Select all screens start _with 'questionnaire'
    order = data["screen"].str.startswith("questionnaire")
    order[order.isna()] = False
    order = list(data[order]["screen"])

    # PID-5 ---------------------------------------------------------------
    pid5 = data[data["screen"] == "questionnaire_pid5"].iloc[0]

    df["PID5_Duration"] = pid5["rt"] / 1000 / 60
    df["PID5_Order"] = order.index("questionnaire_pid5") + 1

    pid5 = json.loads(pid5["response"])
    for item in pid5:
        df["PID5_" + item] = pid5[item]

    # IPIP-6 --------------------------------------------------------------
    ipip6 = data[data["screen"] == "questionnaire_ipip6"].iloc[0]

    df["IPIP6_Duration"] = ipip6["rt"] / 1000 / 60
    df["IPIP6_Order"] = order.index("questionnaire_ipip6") + 1

    ipip6 = json.loads(ipip6["response"])
    for item in ipip6:
        df["IPIP6_" + item] = ipip6[item]

    # SSS -----------------------------------------------------------------
    sss = data[data["screen"] == "questionnaire_sss"].iloc[0]

    df["SSS_Duration"] = sss["rt"] / 1000 / 60
    df["SSS_Order"] = order.index("questionnaire_sss") + 1

    sss = json.loads(sss["response"])
    for item in sss:
        df[item] = sss[item]

    # MIST ----------------------------------------------------------------
    mist = data[data["screen"] == "questionnaire_mist"].iloc[0]

    df["MIST_Duration"] = mist["rt"] / 1000 / 60
    df["MIST_Order"] = order.index("questionnaire_mist") + 1

    mist = json.loads(mist["response"])["P0_Q1"]  # TODO: what is P0_Q1?
    for item in mist:
        df[item] = mist[item]

    alldata_sub = pd.concat([alldata_sub, df], ignore_index=True)

    # Illusion Game =====================================================
    ig = data[data["screen"] == "IG_Trial"]
    ig = ig[ig["block"] != "Practice"]

    df_ig = ig[["Illusion_Type", "Illusion_Difference", "Illusion_Strength"]].reset_index(drop=True)
    df_ig["Participant"] = filename
    df_ig["File"] = [
        s.replace("https://realitybending.github.io/IllusionGame/v3/stimuli/", "") for s in ig["stimulus"].values
    ]
    df_ig["Block"] = ig["block"].values
    df_ig["Trial"] = ig["trial_number"].values
    df_ig["ISI"] = ig["isi"].values
    df_ig["RT"] = ig["rt"].values / 1000  # In seconds
    df_ig["Response"] = ig["response"].values
    df_ig["Response_Correct"] = ig["correct_response"].values
    df_ig["Error"] = (ig["correct"] == False).values.astype(int)
    # TODO: Fixation cross

    # Reorder Columns
    first_column = df_ig.pop("Participant")
    df_ig.insert(0, "Participant", first_column)

    alldata_ig = pd.concat([alldata_ig, df_ig], ignore_index=True)


# Checks ===================================================================
# SONA -------------------------------------------------------------------
alldata_ig["SONA_ID"] = alldata_sub.set_index("Participant").loc[alldata_ig["Participant"].values]["SONA_ID"].values


d = alldata_ig[~np.isnan(alldata_ig["SONA_ID"])]
d = d[~np.isin(d["SONA_ID"].values, sona_credited)]
d.loc[:, "SONA_ID"] = d["SONA_ID"].astype(int).astype(str).values
d = d.sort_values(by=["SONA_ID", "Block", "Trial"])
# d = d[[x in ["31852"] for x in d.Participant]]
sns.kdeplot(data=d[d.Block == "A"], x="RT", hue="SONA_ID", bw_adjust=0.5).set(xlim=(0, 3))
sns.kdeplot(data=d[d.Block == "B"], x="RT", hue="SONA_ID", bw_adjust=0.5, linestyle="--").set(xlim=(0, 3))

print(d["SONA_ID"].unique())
# "32009" in alldata_sub["SONA_ID"][~np.isnan(alldata_sub["SONA_ID"])].astype(str).values

# Check mean RT
rez = d.groupby(["SONA_ID", "Block"]).mean("RT")
rez = rez.loc[rez.index.get_level_values("Block") == "B"][["RT", "Error"]]
rez.sort_values(by="RT")


# Prolific ----------------------------------------------------------------
if len(prolific_ids) > 0:
    d = alldata_ig[[i in list(prolific_ids.keys()) for i in alldata_ig["Participant"].values]]
    d.loc[:, "Participant"] = [str(prolific_ids[i]) for i in d["Participant"].values]
    # d = d[[x in ["31852"] for x in d.Participant]]
    sns.kdeplot(data=d[d.Block == "A"], x="RT", hue="Participant", bw_adjust=0.5).set(xlim=(0, 3))
    sns.kdeplot(data=d[d.Block == "B"], x="RT", hue="Participant", bw_adjust=0.5, linestyle="--").set(xlim=(0, 3))
    print(np.sort([k[1] for k in prolific_ids.items()]))

# Save data ==============================================================

# Remove columns
alldata_sub = alldata_sub.drop(columns=["Browser", "Platform", "Screen_Width", "Screen_Height", "SONA_ID"])
alldata_ig = alldata_ig.drop(columns=["SONA_ID"])

# Inspect ================================================================
# alldata_sub["Experimenter"].unique()
# alldata_sub["Ethnicity"].unique()

# Reanonimize ============================================================
alldata_sub["d"] = pd.to_datetime(alldata_sub["Date"] + " " + alldata_sub["Time"], format="%d/%m/%Y %H:%M:%S")
alldata_sub = alldata_sub.sort_values(by=["d"]).reset_index(drop=True)
correspondance = {j: f"S{i+1:03}" for i, j in enumerate(alldata_sub["Participant"])}
alldata_sub["Participant"] = [correspondance[i] for i in alldata_sub["Participant"]]
alldata_ig["Participant"] = [correspondance[i] for i in alldata_ig["Participant"]]
alldata_sub = alldata_sub.drop(columns=["d", "Time"])  # Drop OSf column


# Experimenter
# rray(['Experimenter1', 'reddit1', 'Experimenter2', 'fb2', 'website',
#        'reddit4', 'sona', 'fb1:', 'Prolific', nan, 'readme', 'lw_fam_1',
#        'lw_aus_1', 'ep_wa2', 'ep_wa1', 'jl_su', 'jl_fa', 'jl_me', 'jl_pu',
#        'ep_ig1', 'lw_fri_1'], dtype=object)
alldata_sub["Experimenter"].unique()
alldata_sub["Experimenter"] = alldata_sub["Experimenter"].replace(
    {
        "sona": "SONA",
        "reddit1": "Experimenter_DM",
        "reddit4": "Experimenter_DM",
        "fb1:": "Experimenter_DM",
        "fb2": "Experimenter_DM",
        "website": "Website",
        "readme": "Readme",
        "lw_fam_1": "Experimenter_LW",
        "lw_aus_1": "Experimenter_LW",
        "lw_fri_1": "Experimenter_LW",
        "ep_wa2": "Experimenter_EP",
        "ep_wa1": "Experimenter_EP",
        "ep_ig1": "Experimenter_EP",
        "jl_su": "Experimenter_JL",
        "jl_fa": "Experimenter_JL",
        "jl_me": "Experimenter_JL",
        "jl_pu": "Experimenter_JL",
    }
)

# Save
alldata_sub.to_csv("../data/rawdata_participants.csv", index=False)
alldata_ig.to_csv("../data/rawdata_IllusionGame.csv", index=False)
print("Done!")
