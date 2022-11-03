import pandas as pd
import streamlit as st


data=pd.read_csv("C:\\Users\\user\\Downloads\\final.csv")
st.set_page_config(page_title="IPL 2022",layout="wide")
st.header("IPL 2022 Player Stats")
def img_url(string):
	val= string.split("/")
	player_val=val[-1]
	url=player_val.split("-")
	num= url.pop(0)
	nam= '-'.join([str(i) for i in url[:-1]])
	return f'https://s.ndtvimg.com//images/entities/120/{nam}-{num}.png'
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

col1,col2,col3 =st.columns([2,3,3])
with col1:
    inputdata= st.text_input(label="Enter a player name",value="Virat Kohli")
    inputdata=inputdata.lower()
    player=data[data["lower"].str.contains(inputdata)].head(1)
    Url=player["Url"].values
    try:
        st.image(img_url(Url[0]),width=300)
        st.markdown(hide_img_fs, unsafe_allow_html=True)
    except:
        pass
    name=player["Name"].values
    type=player["Type"].values
    team=player["Team"].values
    runscored=player["RunsScored"].values
    hundred=player["100s"].values
    fifty=player["50s"].values
    batavg=player['BattingAVG'].values
    batstrike=player["BattingS/R"].values
    bat_style=player["Batting Style"].values
    bowling=player["Bowling"].values
    wicket=player["Wickets"].values
    Run_consided=player["RunsConceded"].values
    bol_avg=player["BowlingAVG"].values
    eco_rate=player["EconomyRate"].values
    stumping=player["StumpingsMade"].values
    best=player["Best"].values
if type=="Batsman ":
    with col2:
        st.metric(label="Name",value=name[0])
        st.metric(label="Team",value=team[0])
        st.metric(label="Type",value=type[0])
        st.metric(label="Batting Style", value=bat_style[0])
    with col3:
        st.metric(label="Run Scored",value=runscored[0])
        st.metric(label="Batting Average", value=batavg[0])
        st.metric(label="Batting Strikerate", value=batstrike[0])
        st.metric(label="100s", value=hundred[0])
        st.metric(label= "50s", value=fifty[0])




elif type == "Bowler ":
    with col2:
        st.metric(label="Name", value=name[0])
        st.metric(label="Team", value=team[0])
        st.metric(label="Type", value=type[0])
        st.metric(label="Bowling Type", value=bowling[0])
    with col3:
        st.metric(label="Wickets", value=wicket[0])
        st.metric(label="Runs Concided", value=Run_consided[0])
        st.metric(label="Bowling Average", value=bol_avg[0])
        st.metric(label="Economy Rate", value=eco_rate[0])
        st.metric(label="Best Figures",value=best[0])

elif type == "All-Rounder ":
    with col2:
        st.metric(label="Name", value=name[0])
        st.metric(label="Team", value=team[0])
        st.metric(label="Type", value=type[0])
        st.metric(label="Run Scored", value=runscored[0])
    with col3:
        st.metric(label="Wickets", value=wicket[0])
        st.metric(label="Batting Strikerate", value=batstrike[0])
        st.metric(label="Runs Concided", value=Run_consided[0])
        st.metric(label="Economy Rate", value=eco_rate[0])
        st.metric(label="50s", value=fifty[0])

else:
    with col2:
        st.metric(label="Wickets", value=wicket[0])
        st.metric(label="Team", value=team[0])
        st.metric(label="Type", value=type[0])
        st.metric(label="Batting Style", value=bat_style[0])
    with col3:
        st.metric(label="Stumping Made", value=stumping[0])
        st.metric(label="Run Scored", value=runscored[0])
        st.metric(label="50s", value=fifty[0])
        st.metric(label="Batting Average", value=batavg[0])
        st.metric(label="50s", value=fifty[0])






