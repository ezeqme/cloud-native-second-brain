---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2023"
edition_id: 2023-berlin
year: 2023
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Kubernetes", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2023-berlin/talks/perses/
youtube_url: https://www.youtube.com/watch?v=7G_0TCrcVyg
youtube_search_url: https://www.youtube.com/results?search_query=Perses%3A+The+CNCF+candidate+for+observability+visualisation+PromCon+2023
video_match_score: 1.028
status: video-found
---

# Perses: The CNCF candidate for observability visualisation

## Identificação

- Edição: PromCon EU 2023
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Kubernetes]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2023-berlin/talks/perses/
- YouTube: https://www.youtube.com/watch?v=7G_0TCrcVyg

## Resumo

Speaker(s): Augustin Husson & Antoine Thebaud Perses is a new visualization tool supporting Prometheus, owned by the Linux foundation under the open source license Apache V2. It aims to become a standard dashboard visualization tool for Prometheus and other datasources. It will focus on being GitOps-compatible and thus enabling a smooth ""dashboards as code"" workflow via a new and well-defined dashboard definition model.

## Abstract oficial

Speaker(s): Augustin Husson & Antoine Thebaud

Perses is a new visualization tool supporting Prometheus, owned by the Linux foundation under the open source license Apache V2.


It aims to become a standard dashboard visualization tool for Prometheus and other datasources. It will focus on being GitOps-compatible and thus enabling a smooth ""dashboards as code"" workflow via a new and well-defined dashboard definition model.
While being another visualization tool, Perses also aims to provide different npm packages, so it can benefit anyone that would like to embed charts and dashboards in their UI. For example, these packages might be used to improve the display of the data in the Prometheus UI.
To be friendly to dashboards as code users, we want to provide a complete static validation of the dashboard format. That means you will be able to validate your dashboards in a CI/CD using the Perses CLI.


For the PromCon, we are proud to announce we are reaching a first public alpha version with all primary features we wanted to propose:


Basic chart types available (timeseries, gauge, stat).
Shared variables across dashboards.
Scoped datasources (a datasource can be defined either at project or at global level).
Plugin system at different levels (panel, query, datasource, variable).
Dashboards as code with Cuelang and a data model that follows Kubernetes practices.


Any feedback will be greatly appreciated to be sure we didn’t miss anything around the architecture.
In a later stage, we will propose:


a Kubernetes-native mode in which dashboard definitions can be deployed into and read from individual application namespaces (Using CRDs).
Authentication & Authorization support.
Visualization for logs and traces.
Datasources discovery.
Sub folder management.
Panels generation.

## Links

- Página oficial: https://promcon.io/2023-berlin/talks/perses/
- YouTube: https://www.youtube.com/watch?v=7G_0TCrcVyg
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7G_0TCrcVyg
- YouTube title: PromCon 2023 - Perses: The CNCF candidate for observability visualisation
- Match score: 1.028
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2023/perses-the-cncf-candidate-for-observability-visualisation/7G_0TCrcVyg.txt
- Transcript chars: 18955
- Keywords: dashboard, display, support, process, pretus, variables, version, actually, peress, moment, source, dashboards, resources, global, defined, coming, looking, thanos

### Resumo baseado na transcript

[Music] uh hello everyone my name is austan I'm a principal engineer from Amadeus I'm also part of the pretus team and uh I will be with fan who is a senior developer also from Amadeus and together we are going to present a new tool called pcess and uh I hope you will enjoy the this new product but before going deeper in the details I just want to give you some G some details about where does it come from the Genesis of pess so actually just it's

### Excerpt da transcript

[Music] uh hello everyone my name is austan I'm a principal engineer from Amadeus I'm also part of the pretus team and uh I will be with fan who is a senior developer also from Amadeus and together we are going to present a new tool called pcess and uh I hope you will enjoy the this new product but before going deeper in the details I just want to give you some G some details about where does it come from the Genesis of pess so actually just it's coming from a simple statement uh if you are looking to the Clone native Computing Foundation tools like pretus and Kutis uh you will see that okay you have the metric form you have pretus you have open Terry you have open metrics uh you have Thanos and cortex to scale pretus but there is nothing for the visualization so that's where PR uh passess is coming from we want to fill this Gap and uh we want to go to the cncf and that's where we created the project we created the project uh under the license Apache V2 and today it belongs to the Linux function and one day it will go to the cncf uh the project is supported by Amad Chronos and rat and maybe later with more and more comp let's say um so let's go to for a quick overview first thing you should know peress is dashboard tooling uh specialized in the metric visualization for the moment uh so if you are going to try it today you can only uh connect PES to promus or Thanos or any vendor supporting the promus RPI and nothing more for the moment we when we started to think about peress what we want to do with this project uh what what we want to achieve exactly uh first thing that came on the paper was we want something really G us friendly uh because for example in amadu we have like 3,000 dashboard using raana and it's quite hard to maintain all these dashboard and to be sure they are following uh the upgrade of graph they are still good they are still loading when you are on on call at 3:00 a.m.

we are hoping everything is fine so we want in something much more GTO friendly and the let's say dashboard as code oriented so to to be able to achieve that we have three different um let's say topics first things we want to have is a static validation which come with peress with CLI and Kong schema and with both of them we are able to to validate dashboard Jon using any any kind of C cicd you would like uh we want also to be uh native to kubernetes which means to be able to install the dashboard with crds and to have the data source Discovery and then we will think abo
