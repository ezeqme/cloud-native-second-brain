---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/grafana-and-prometheus/
youtube_url: https://www.youtube.com/watch?v=PDpP1uX_orE
youtube_search_url: https://www.youtube.com/results?search_query=Grafana+and+Prometheus+PromCon+2017
video_match_score: 0.741
status: video-found
---

# Grafana and Prometheus

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/grafana-and-prometheus/
- YouTube: https://www.youtube.com/watch?v=PDpP1uX_orE

## Resumo

Speaker: Carl Bergquist Being the default dashboard for Prometheus I guess most of you already tried Grafana and created some graphs. But have you tried the table and heat map panels? Did you know that Grafana also offers multiple plugins to visualize and show your Prometheus data?

## Abstract oficial

Speaker: Carl Bergquist

Being the default dashboard for Prometheus I guess most of you already tried Grafana and created some graphs. But have you tried the table and heat map panels? Did you know that Grafana also offers multiple plugins to visualize and show your Prometheus data? What other tricks and optimizations are there?

We will also look at the major changes in Grafana since last PromCon and what we currently work on.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/grafana-and-prometheus/
- YouTube: https://www.youtube.com/watch?v=PDpP1uX_orE
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PDpP1uX_orE
- YouTube title: PromCon 2017: Grafana and Prometheus - Carl Bergquist
- Match score: 0.741
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/grafana-and-prometheus/PDpP1uX_orE.txt
- Transcript chars: 21835
- Keywords: prometheus, dashboard, series, support, template, ravana, feature, certain, basically, queries, alerts, instances, dashboards, rather, editor, change, values, always

### Resumo baseado na transcript

[Music] next up there is car from formerly Renton snow graph an ellipse he'll tell you about the fauna last year's major feature was utf-8 supports he could put in Smiley's and I'm happy to see what we see this summer in a web UI without emojis is sad UI so the title for this presentation is gray fauna and Prometheus also known as best friends forever my name is Cole Backus I'm a software engineer at Corona labs so I spend most of my days working on Gravano until all your dashboards in different folders and as we see we all know their ops people like here logarithmic scales and they said oh yeah each of these folders will have different permissions so you can say that obstacle are only one who can edit

### Excerpt da transcript

[Music] next up there is car from formerly Renton snow graph an ellipse he'll tell you about the fauna last year's major feature was utf-8 supports he could put in Smiley's and I'm happy to see what we see this summer in a web UI without emojis is sad UI so the title for this presentation is gray fauna and Prometheus also known as best friends forever my name is Cole Backus I'm a software engineer at Corona labs so I spend most of my days working on Gravano until recently when I went on parental leave so if I'm kind of rusty on the subject please give me some time and I will find an answer for you but this was a major role in my commitment although I've been following the project but I stayed away from commits almost for those of you who don't know your father Ravana is a time series with sensation tools that support multiple multiple data sources and one of them is Prometheus which is the one we're going to focus on today this talk will not be I mean traduction took a phenom I would rather highlight certain feature and changes that happen during the year since lost Bronk on some features that I don't think you should miss basically so let's start looking at the query editor for Prometheus the major change we had this year was that we change the input field so text area thanks Brian for that suggestion although we're kind of surprised how by the lack of feedback from the extreme religious community about how bad this editor is so we started quite recently improving it it's not in last year but you can find it in the ACE editor branch [Music] a lightning colony and okay and even some like explanations to functions and so on so you can get them right into you I that's quite an upgrade yeah so if you wanna test it use the ACE editor branch and please give us feedback the graph panel is the bread and butter of Ravana hey I'm on cannot talk about it so much but I want to mention one feature that is the display series overrides which allows you to specify and reg X pattern as you can see in the bottom yeah and then in this case I disable lines and enable points and force the color red for the upper 95 percentile or 99 percent or something like that because if you do percentile graphs they tend to be very jumpy and that tend to hurt my eyes and so I like to have the jumpy numbers as points inside another cool thing is that you can feel between gaps between lines so in this case we feel between mean and Max and then we draw an average line in the middle because we
