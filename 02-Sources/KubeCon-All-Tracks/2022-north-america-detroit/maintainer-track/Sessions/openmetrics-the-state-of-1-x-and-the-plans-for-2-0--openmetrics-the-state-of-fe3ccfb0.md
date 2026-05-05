---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Richard Hartmann", "Grafana Labs"]
sched_url: https://kccncna2022.sched.com/event/182Ob/openmetrics-the-state-of-1x-and-the-plans-for-20-richard-hartmann-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=OpenMetrics%3B+the+State+Of+1.X+And+the+Plans+For+2.0+CNCF+KubeCon+2022
slides: []
status: parsed
---

# OpenMetrics; the State Of 1.X And the Plans For 2.0 - Richard Hartmann, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Richard Hartmann, Grafana Labs
- Schedule: https://kccncna2022.sched.com/event/182Ob/openmetrics-the-state-of-1x-and-the-plans-for-20-richard-hartmann-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=OpenMetrics%3B+the+State+Of+1.X+And+the+Plans+For+2.0+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre OpenMetrics; the State Of 1.X And the Plans For 2.0.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ob/openmetrics-the-state-of-1x-and-the-plans-for-20-richard-hartmann-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=OpenMetrics%3B+the+State+Of+1.X+And+the+Plans+For+2.0+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8zyoYFFiIdI
- YouTube title: OpenMetrics; the State Of 1.X And the Plans For 2.0 - Richard Hartmann, Grafana Labs
- Match score: 0.849
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/openmetrics-the-state-of-1-x-and-the-plans-for-2-0/8zyoYFFiIdI.txt
- Transcript chars: 29701
- Keywords: prometheus, metrics, actually, standard, histograms, underscore, format, course, native, within, single, library, write, completely, created, efficient, directly, better

### Resumo baseado na transcript

anyway so welcome to an update on open metrics uh if you could close it oh perfect so um how we structure this is relatively easy we do a speed run through the history for those who don't know and then we we come to the current state and then we go towards the future at the end of we have a room for questions uh Cayman is going to run around so looking at at observability data um historically you had basically one standard in this space which is

### Excerpt da transcript

anyway so welcome to an update on open metrics uh if you could close it oh perfect so um how we structure this is relatively easy we do a speed run through the history for those who don't know and then we we come to the current state and then we go towards the future at the end of we have a room for questions uh Cayman is going to run around so looking at at observability data um historically you had basically one standard in this space which is SNMP any one of you who's ever dealt with networks is probably familiar with this there is a little bit of a lot of love-hate relationships and one of my major pain points with SNMP is actually that it's based on asn1 which is like super old seven bit encoding highly efficient and absolute mess to get right and it's really really really I see people laughing yeah it's really a mess and it's kind of risky it's often chatty and slow uh oftentimes interfaces are hard to implement like yes you can walk through them but it's it's really inconvenient the data models are vastly different between vendors sometimes even between just versions of software and the thing about hierarchical data sets is it almost never fits your needs because like if you have region data center customer and you want to group by customer congratulations your your data is wrong so those are just pain points which which existed before Prometheus after Prometheus it is the de facto standard anyone in this audience who is is using kubernetes is very likely also using Prometheus or something within the Prometheus family of course else you're going to have a really bad time with the kubernetes the same is true for the Prometheus Exposition format that it also became this de facto standard but like not a real standard we and I'm speaking as a Prometheus team member here and also there's quite a few up front um there was an episode explosion over the years of compatible endpoints with literally hundreds of thousands of installations of Prometheus alone with literally millions probably tens of millions because the slide is two years old tens of millions of users who are who are using these these formats directly or indirectly every single day to keep their stuff running and we have standard exporters we have standard libraries in particular the go library is one of the most goal libraries on Earth so there is substantial access success but yet again this is no official standard and yeah label sets I mean I don't have to convince your labels are better tha
