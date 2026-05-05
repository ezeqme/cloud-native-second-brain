---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Alex Arnell", "Heroku / Salesforce"]
sched_url: https://kccncna2024.sched.com/event/1i7nC/lessons-learned-adopting-opentelemetry-at-scale-alex-arnell-heroku-salesforce
youtube_search_url: https://www.youtube.com/results?search_query=Lessons+Learned+Adopting+OpenTelemetry+at+Scale+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Lessons Learned Adopting OpenTelemetry at Scale - Alex Arnell, Heroku / Salesforce

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Alex Arnell, Heroku / Salesforce
- Schedule: https://kccncna2024.sched.com/event/1i7nC/lessons-learned-adopting-opentelemetry-at-scale-alex-arnell-heroku-salesforce
- Busca YouTube: https://www.youtube.com/results?search_query=Lessons+Learned+Adopting+OpenTelemetry+at+Scale+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Lessons Learned Adopting OpenTelemetry at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nC/lessons-learned-adopting-opentelemetry-at-scale-alex-arnell-heroku-salesforce
- YouTube search: https://www.youtube.com/results?search_query=Lessons+Learned+Adopting+OpenTelemetry+at+Scale+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5iM8n3uCo_U
- YouTube title: Lessons Learned Adopting OpenTelemetry at Scale - Alex Arnell, Heroku / Salesforce
- Match score: 0.838
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/lessons-learned-adopting-opentelemetry-at-scale/5iM8n3uCo_U.txt
- Transcript chars: 29329
- Keywords: actually, probably, heroku, little, talking, metrics, observability, vendor, migration, second, challenge, working, dashboards, trying, logging, everything, requests, terraform

### Resumo baseado na transcript

uh we should get started here um so uh my name is Alex I joined Heroku about 10 years ago um interesting fun fact is I've come full circle in my engineering life cycle at Heroku I joined Heroku uh when they for on the original Telemetry team and uh after a while moving around to different other teams uh I've come back to a newly formed Telemetry team this year uh so uh this talk is not going to be your typical kind of tech talk uh I have

### Excerpt da transcript

uh we should get started here um so uh my name is Alex I joined Heroku about 10 years ago um interesting fun fact is I've come full circle in my engineering life cycle at Heroku I joined Heroku uh when they for on the original Telemetry team and uh after a while moving around to different other teams uh I've come back to a newly formed Telemetry team this year uh so uh this talk is not going to be your typical kind of tech talk uh I have um a slightly different uh context of what scale we're going to be talking about today because as Engineers we often think of scale of like how many servers how many requests a second do you do but we're going to be talking about slightly different uh scale um which leads into the second topic how do you drive adoption at a large organization then we'll go into some lessons that we learned along the way uh including uh a deep dive into histograms and then some general tips uh and like how we use terraform to save ourselves some time in the future so first let's talk about scale uh Heroku was founded in 20 2007 uh acquired by Salesforce 2010 right we do 60 billion requests per day and we have you know in Impact across the industry so that's really 17 years of code uh we have 844 public repositories and you can imagine how many private ones we have given that number of public ones um we we utilize quite a number of different languages right so these are some of the top ones Ruby and go being kind of probably the two most prevalent but there's also a lot of JavaScript um and a bit of python in there right we also are pretty big organization lots of Engineers number of teams right so this is really kind of the scale that I'm talking about at least for the first half of this talk so how do you go about influence and change right so the change right we're talking about here is how do you bring open t something like open Telemetry into your organization and get everybody on board with this idea uh so quick showah hands does anybody know who this is okay I see a few if I said that he's a really famous author would that raise any more hands no yeah couple okay he is a really famous author um he also has a uh personal development training program that is based off his work okay the final hint I'll give you is the book that is probably most famous for is titled how to win friends and influence others right so this is Dale Carnegie now you've probably know who I'm talking about um so he in his book uh how to win friends and influence
