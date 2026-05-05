---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/grafana-master-class/
youtube_url: https://www.youtube.com/watch?v=KoU_DquChS8
youtube_search_url: https://www.youtube.com/results?search_query=Grafana+Master+Class+PromCon+2016
video_match_score: 0.718
status: video-found
---

# Grafana Master Class

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/grafana-master-class/
- YouTube: https://www.youtube.com/watch?v=KoU_DquChS8

## Resumo

Speaker: Carl Bergquist Grafana is a powerful tool with lots of options and settings. Some of them are barely documented. In this session I will show some of the features in Grafana that go beyond just drawing graphs on a screen.

## Abstract oficial

Speaker: Carl Bergquist

Grafana is a powerful tool with lots of options and settings. Some of them are
barely documented. In this session I will show some of the features in Grafana
that go beyond just drawing graphs on a screen.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/grafana-master-class/
- YouTube: https://www.youtube.com/watch?v=KoU_DquChS8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KoU_DquChS8
- YouTube title: PromCon 2016: Grafana Master Class - Carl Bergquist
- Match score: 0.718
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/grafana-master-class/KoU_DquChS8.txt
- Transcript chars: 17070
- Keywords: grafana, prometheus, template, series, source, dashboard, templating, select, whenever, sources, dashboards, queries, create, another, variables, version, values, variable

### Resumo baseado na transcript

so yes i'm a grandfather developer and i've been working on grafana full-time about a year since i joined renthank and as brian said that's about the same time prometheus was added to grafana and for those of you do you who don't know grafana it's a dashboarding tool that supports multiple data sources not just prometheus to support six different data sources in the core model and one of them is prometheus as i said and in grafana we have a small call home feature that every day sends

### Excerpt da transcript

so yes i'm a grandfather developer and i've been working on grafana full-time about a year since i joined renthank and as brian said that's about the same time prometheus was added to grafana and for those of you do you who don't know grafana it's a dashboarding tool that supports multiple data sources not just prometheus to support six different data sources in the core model and one of them is prometheus as i said and in grafana we have a small call home feature that every day sends some data about your grafana installation back to us and it's no sensitive data you can check it it's it's pure version numbers and so on and we also send the data source usage so we calculate how many uh graphene installations has elite at least one prometheus data source and when i checked that yesterday there's about two thousand eight hundred graphene installation that has prometheus which i think is kind of great if the usage increase has been steady since a year ago so i think this is almost worth celebrating grafana itself it's uh a little bit bigger and we have about almost uh tren almost two million dashboard almost getting close to two million dashboards for you every day uh so this is about how grafana is basically how graffana looks um regarding last dashboard you can view it on the playgrouphana.org it's public information if you want to see more stats about grafana you can get version numbers and so on so this is kind of how grafana looks and my idea now is to jump into grafana and show you some features that i think you should be aware of and don't miss and also introduce it a bit so all these these dashboards that i'm going to show now are available on playgrouphana.org as well and they're tagged with prom conf so when you get on your dashboard you can add a new panel by clicking the green one or you can go to click the title go edit mode uh so this is how you write your premier squares i'm not going to show you so many prometheus queries because the primitives team would probably slap me in the face um but it allows you to do some filtering like job equals no stuff like that and you can also form of the label because this this is the name that prometheus returns and it's uh correct but kind of ugly so i suggest you give it a better name by using the legit formatter like that then you will select the label job and all your air graphs it looks much better you can also quick search on time series to the right if you want to search to get the correct spelling and
