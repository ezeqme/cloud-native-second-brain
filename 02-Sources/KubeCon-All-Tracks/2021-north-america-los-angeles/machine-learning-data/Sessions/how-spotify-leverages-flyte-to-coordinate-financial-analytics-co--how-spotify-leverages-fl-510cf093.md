---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data"]
speakers: ["Haytham Abuelfutuh", "Union.ai", "Dylan Wilder Patterson", "Spotify"]
sched_url: https://kccncna2021.sched.com/event/lV59/how-spotify-leverages-flyte-to-coordinate-financial-analytics-company-wide-haytham-abuelfutuh-unionai-dylan-wilder-patterson-spotify
youtube_search_url: https://www.youtube.com/results?search_query=How+Spotify+Leverages+Flyte+To+Coordinate+Financial+Analytics+Company-Wide+CNCF+KubeCon+2021
slides: []
status: parsed
---

# How Spotify Leverages Flyte To Coordinate Financial Analytics Company-Wide - Haytham Abuelfutuh, Union.ai & Dylan Wilder Patterson, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: United States / Los Angeles
- Speakers: Haytham Abuelfutuh, Union.ai, Dylan Wilder Patterson, Spotify
- Schedule: https://kccncna2021.sched.com/event/lV59/how-spotify-leverages-flyte-to-coordinate-financial-analytics-company-wide-haytham-abuelfutuh-unionai-dylan-wilder-patterson-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=How+Spotify+Leverages+Flyte+To+Coordinate+Financial+Analytics+Company-Wide+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre How Spotify Leverages Flyte To Coordinate Financial Analytics Company-Wide.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV59/how-spotify-leverages-flyte-to-coordinate-financial-analytics-company-wide-haytham-abuelfutuh-unionai-dylan-wilder-patterson-spotify
- YouTube search: https://www.youtube.com/results?search_query=How+Spotify+Leverages+Flyte+To+Coordinate+Financial+Analytics+Company-Wide+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wkZs98pTSsc
- YouTube title: How Spotify Leverages Flyte To Coordinate Financial A... Haytham Abuelfutuh & Dylan Wilder Patterson
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/how-spotify-leverages-flyte-to-coordinate-financial-analytics-company/wkZs98pTSsc.txt
- Transcript chars: 33786
- Keywords: flight, write, python, spotify, inputs, workflow, running, process, workflows, business, exactly, execution, platform, couple, requirements, certain, environment, within

### Resumo baseado na transcript

all right um well hi everyone and welcome to the i guess the last day of the conference so you made it congrats uh we are going to talk today about how spotify has used flight to revamp their financial analytics platform and my name is haitham abruptor i am one of the co-founders and maintainers of the flight open source projects and joining me today is dylan wilder from spotify but unfortunately due to personal circumstances he wasn't able to be here in person but he was gracious enough

### Excerpt da transcript

all right um well hi everyone and welcome to the i guess the last day of the conference so you made it congrats uh we are going to talk today about how spotify has used flight to revamp their financial analytics platform and my name is haitham abruptor i am one of the co-founders and maintainers of the flight open source projects and joining me today is dylan wilder from spotify but unfortunately due to personal circumstances he wasn't able to be here in person but he was gracious enough to share his thoughts in a recorded video so without further ado i let him introduce himself and talk about what spotify has been trying to do my name is dylan oops um i'm an engineering manager uh on a team called vivaldi within spotify we work in the finance department um and i'm also the tech lead on a project called one model and so that's what this is about and one model is really powered by flight i just want to give some background on what we're talking about so this is really one model is a financial forecasting problem um and quickly what financial forecasting is um is every quarter as part of compliance objectives spotify is required to project two years into the future what we think our profit and losses are and that's part of just being a public company um and so it's basically a projection across all of spotify's various business processes uh what revenues do we think will take in what cost do we think we'll have to spend in order to get there um as in addition to just being part of you know requirement it also forms a big part of spotify's business planning uh you can imagine this is useful for investment investors it's just as useful internally for the people making decisions the c-suite etc unfortunately you know it's organically evolved over the years to be a bunch of different heterogeneous processes across many different teams as you might imagine spotify is a pretty complicated company we have a lot of different products we work in a lot of different markets we deal with licensors music law stuff like that and so the expertise in order to kind of run this system is scattered across a lot of different domain experts and so as it stands this process takes about three to four weeks every quarter span as many as eight different teams these teams work in silos some of these pieces are excel models um and then at the end of the day you might imagine team one is handing off a google sheet to team two to start running you know if the number of subscribers we ge
