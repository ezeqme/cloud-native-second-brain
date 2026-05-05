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
themes: ["Observability"]
speakers: ["Tyler Helmuth", "Honeycomb", "Evan Bradley", "Dynatrace"]
sched_url: https://kccncna2024.sched.com/event/1i7mZ/the-ottl-cookbook-a-collection-of-solutions-to-common-problems-tyler-helmuth-honeycomb-evan-bradley-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=The+OTTL+Cookbook%3A+A+Collection+of+Solutions+to+Common+Problems+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The OTTL Cookbook: A Collection of Solutions to Common Problems - Tyler Helmuth, Honeycomb & Evan Bradley, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Tyler Helmuth, Honeycomb, Evan Bradley, Dynatrace
- Schedule: https://kccncna2024.sched.com/event/1i7mZ/the-ottl-cookbook-a-collection-of-solutions-to-common-problems-tyler-helmuth-honeycomb-evan-bradley-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=The+OTTL+Cookbook%3A+A+Collection+of+Solutions+to+Common+Problems+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The OTTL Cookbook: A Collection of Solutions to Common Problems.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7mZ/the-ottl-cookbook-a-collection-of-solutions-to-common-problems-tyler-helmuth-honeycomb-evan-bradley-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=The+OTTL+Cookbook%3A+A+Collection+of+Solutions+to+Common+Problems+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UGTU0-KT_60
- YouTube title: The OTTL Cookbook: A Collection of Solutions to Common Problems - Tyler Helmuth & Evan Bradley
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-ottl-cookbook-a-collection-of-solutions-to-common-problems/UGTU0-KT_60.txt
- Transcript chars: 35814
- Keywords: metric, attribute, collector, attributes, logs, function, string, metrics, prefix, values, resource, statements, points, transformations, otel, statement, inside, wanted

### Resumo baseado na transcript

all right hi everyone thank you for coming to the late track the last track of the day session we appreciate it uh this is the OTL cookbook my name is Tyler houth I'm an engineer from honeycomb I'm Evan Bradley I'm an engineer from din trce so first I need to show a hands how many people in here have used OTL before okay pretty good number all right well I see that there weren't some hands up and I'm going to assume that's not because your arms cramping

### Excerpt da transcript

all right hi everyone thank you for coming to the late track the last track of the day session we appreciate it uh this is the OTL cookbook my name is Tyler houth I'm an engineer from honeycomb I'm Evan Bradley I'm an engineer from din trce so first I need to show a hands how many people in here have used OTL before okay pretty good number all right well I see that there weren't some hands up and I'm going to assume that's not because your arms cramping so first uh I'm going to cover what we're going to cover today here and first we're going to get into what the collector is and how OT fits into that just so that everybody's up to speed after that we're going to solve a couple of scenarios with OTL um we have the recipes as part of our cookbook and we're going to frame them using these scenarios um so we hope you'll enjoy those and then to show ot's flexibility we're going to take your scenarios and then we're going to do them live so we hope that you've brought some or that you can think of some throughout our presentation so just to get started here the open collector is an observability pipeline middleware that can Import and Export data in all sorts of formats and the user can control the flow of data as it goes to the collector and The Collector owes this to its pipeline model which is based on a custom like internal version that it or of data that's based on OTL um and this is particularly useful with processors so processors are able to work on data on this internal representation without having to worry about what the data is going to look like going out or how it looked coming in and this is going to be the focus of the presentation today um o usually comes in at the processing stage in particular we're going to be focusing on two processors in The Collector the transform processor which can edit data in place as it travels to the collector and the filter processor which drops data from a pipeline so what is ootl ootl is a DSL that is custom built for The Collector really fast really flexible it's probably the most flexible way to modify data inside of the collector and it owes this to a couple of properties first you can access any field on the otop payload so any data coming into the collector OT is going to provide some way of providing access to this second since it's a programming language you are given a degree of expressiveness that might not be present in something like a yaml config um and we've made the syntax just complex enough hopeful
