import json

import pandas as pd
import numpy as np
import seaborn as sns


# Get files from OSF ======================================================
def osf_listfiles(data_subproject="", token="", after_date=None):
    try:
        import osfclient
    except ImportError:
        raise ImportError("Please install 'osfclient' (`pip install osfclient`)")
    osf = osfclient.OSF(token=token).project(data_subproject)  # Connect to project
    storage = [s for s in osf.storages][0]  # Access storage component
    files = [
        {
            "name": file.name.replace(".csv", ""),
            "date": pd.to_datetime(file.date_created),
            "url": file._download_url,
            "size": file.size,
            "file": file,
        }
        for file in storage.files
    ]
    file = [f for f in storage.files][0]
    file.__dict__

    if after_date is not None:
        date = pd.to_datetime(after_date, format="%d/%m/%Y", utc=True)
        files = [f for f, d in zip(files, [f["date"] > date for f in files]) if d]
    return files


token = ""  # Paste OSF token here to access private repositories
files = osf_listfiles(
    token=token,
    data_subproject="6xdz9",  # Data subproject ID
    after_date="13/12/2023",
)


# Loop through files ======================================================
alldata_sub = pd.DataFrame()  # Initialize empty dataframe
alldata_ig = pd.DataFrame()  # Initialize empty dataframe
sona_ids = {}

for i, file in enumerate(files):
    print(f"File N°{i+1}/{len(files)}")

    data = pd.read_csv(file["file"]._get(file["url"], stream=True).raw)

    # Participant ========================================================
    # data["screen"].unique()

    # Browser info -------------------------------------------------------
    browser = data[data["screen"] == "browser_info"].iloc[0]

    # Experimenter
    if "experimenter" in browser.index:
        experimenter = "Experimenter1"
    else:
        experimenter = browser["researcher"]
    if isinstance(experimenter, float):
        experimenter = "Experimenter" + str(int(experimenter))

    df = pd.DataFrame(
        {
            "Participant": file["name"],
            "Experimenter": experimenter,
            "Experiment_Duration": data["time_elapsed"].max() / 1000 / 60,
            "Date_OSF": file["date"],
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

    if "sona_id" in browser.index:
        if np.isnan(browser["sona_id"]) == False:
            id = int(browser["sona_id"])
            df["SONA_ID"] = id
            if id not in [
                27027,
                28388,
                29913,
                30623,
                30633,
                30645,
                30644,
                30675,
                30694,
                30695,
                30722,
                30725,
                30760,
                30768,
                30772,
                30809,
                30839,
                30827,
                # 30854,
                30862,
                30872,
                30876,
                30885,
                30889,
                30901,
                30993,
                31037,
                31060,
                31065,
                31728,
                31731,
                31777,
                31783,
                31810,
                31822,
                31852,  # Awarded 0
                31857,
                31864,
                31869,
                31827,
                31852,
                31853,
                31885,
                31923,
                31935,
                31978,
                32068,
                32085,
                32148,
                32161,
                32165,
            ]:
                sona_ids[file["name"]] = id

    # Demographics -------------------------------------------------------
    demo1 = data[data["screen"] == "demographics_1"].iloc[0]
    demo1 = json.loads(demo1["response"])

    df["Gender"] = demo1["gender"]
    df["Education"] = demo1["education"]

    demo2 = data[data["screen"] == "demographics_2"].iloc[0]
    demo2 = json.loads(demo2["response"])

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
        "Caucasian"
        if race in ["British", "White British", "Czech", "European", "Nederlander"]
        else race
    )
    race = "Mixed" if race in ["Caucasion Metis"] else race
    race = "South Asian" if race in ["Indian"] else race
    race = np.nan if race in [""] else race
    df["Ethnicity"] = race

    # Questionnaires =====================================================

    # Manual fix (2 first participants had duplicated questionnaires)
    if file["name"] in ["8va2haolh5", "exgf9of50l"]:
        data.loc[data["screen"][data["trial_type"] == "survey"].index, "screen"] = (
            "questionnaire_mist"
        )
        if file["name"] == "exgf9of50l":
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

    mist = json.loads(mist["response"])["P0_Q1"]
    for item in mist:
        df[item] = mist[item]

    alldata_sub = pd.concat([alldata_sub, df], ignore_index=True)

    # Illusion Game =====================================================
    ig = data[data["screen"] == "IG_Trial"]
    ig = ig[ig["block"] != "Practice"]

    df_ig = ig[
        ["Illusion_Type", "Illusion_Difference", "Illusion_Strength"]
    ].reset_index(drop=True)
    df_ig["Participant"] = file["name"]
    df_ig["File"] = [
        s.replace("https://realitybending.github.io/IllusionGame/v3/stimuli/", "")
        for s in ig["stimulus"].values
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

# Save data ==============================================================

# SONA check =============================================================
if len(sona_ids) > 0:
    # np.sort([int(k[1]) for k in sona_ids.items()])
    d = alldata_ig[
        [i in list(sona_ids.keys()) for i in alldata_ig["Participant"].values]
    ]
    d.loc[:, "Participant"] = [str(sona_ids[i]) for i in d["Participant"].values]
    # d = d[[x in ["31852"] for x in d.Participant]]
    sns.kdeplot(data=d[d.Block == "A"], x="RT", hue="Participant", bw_adjust=0.5).set(
        xlim=(0, 3)
    )
    sns.kdeplot(
        data=d[d.Block == "B"], x="RT", hue="Participant", bw_adjust=0.5, linestyle="--"
    ).set(xlim=(0, 3))
# sona = np.sort(alldata_sub["SONA_ID"].unique())
# sona = sona[~np.isnan(sona)].astype(int)
# 30868 in sona


# Remove columns
alldata_sub = alldata_sub.drop(
    columns=["Time", "Browser", "Platform", "Screen_Width", "Screen_Height", "SONA_ID"]
)
# Inspect ================================================================
# alldata_sub["Experimenter"].unique()
# alldata_sub["Ethnicity"].unique()

# Reanonimize ============================================================
alldata_sub = alldata_sub.sort_values(by=["Date_OSF"]).reset_index(drop=True)
correspondance = {j: f"S{i+1:03}" for i, j in enumerate(alldata_sub["Participant"])}
alldata_sub["Participant"] = [correspondance[i] for i in alldata_sub["Participant"]]
alldata_ig["Participant"] = [correspondance[i] for i in alldata_ig["Participant"]]
alldata_sub = alldata_sub.drop(columns=["Date_OSF"])  # Drop OSf column

# Save
alldata_sub.to_csv("../data/rawdata_participants.csv", index=False)
alldata_ig.to_csv("../data/rawdata_IllusionGame.csv", index=False)
print("Done!")
