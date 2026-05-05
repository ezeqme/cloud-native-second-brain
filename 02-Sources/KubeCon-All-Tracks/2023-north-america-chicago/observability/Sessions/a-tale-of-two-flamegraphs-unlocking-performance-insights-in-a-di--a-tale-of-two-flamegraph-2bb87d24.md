---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Observability"
themes: ["Observability", "SRE Reliability"]
speakers: ["Ryan Perry", "Grafana Labs"]
sched_url: https://kccncna2023.sched.com/event/1R2mo/a-tale-of-two-flamegraphs-unlocking-performance-insights-in-a-diverse-application-landscape-ryan-perry-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=A+Tale+of+Two+Flamegraphs%3A+Unlocking+Performance+Insights+in+a+Diverse+Application+Landscape+CNCF+KubeCon+2023
slides: []
status: parsed
---

# A Tale of Two Flamegraphs: Unlocking Performance Insights in a Diverse Application Landscape - Ryan Perry, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Ryan Perry, Grafana Labs
- Schedule: https://kccncna2023.sched.com/event/1R2mo/a-tale-of-two-flamegraphs-unlocking-performance-insights-in-a-diverse-application-landscape-ryan-perry-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=A+Tale+of+Two+Flamegraphs%3A+Unlocking+Performance+Insights+in+a+Diverse+Application+Landscape+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre A Tale of Two Flamegraphs: Unlocking Performance Insights in a Diverse Application Landscape.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2mo/a-tale-of-two-flamegraphs-unlocking-performance-insights-in-a-diverse-application-landscape-ryan-perry-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=A+Tale+of+Two+Flamegraphs%3A+Unlocking+Performance+Insights+in+a+Diverse+Application+Landscape+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XES5Irk08qw
- YouTube title: A Tale of Two Flamegraphs: Unlocking Performance Insights in a Diverse Application Lan... Ryan Perry
- Match score: 1.021
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/a-tale-of-two-flamegraphs-unlocking-performance-insights-in-a-diverse/XES5Irk08qw.txt
- Transcript chars: 31026
- Keywords: profiling, graphs, function, region, little, application, understand, traces, efficiently, basically, actually, looking, logs, consuming, resources, second, started, whatever

### Resumo baseado na transcript

yeah all right cool what's going on everyone my name is Ryan I am going to be talking today about A Tale of Two flame graphs at least that's what the uh talk is titled um but really uh what I hope for this to be is kind of a more practical guide to how you can get value from flame graphs from continuous profiling uh those two are somewhat synonymous uh I'm going to get more into the nuances of what that all means throughout this talk but uh

### Excerpt da transcript

yeah all right cool what's going on everyone my name is Ryan I am going to be talking today about A Tale of Two flame graphs at least that's what the uh talk is titled um but really uh what I hope for this to be is kind of a more practical guide to how you can get value from flame graphs from continuous profiling uh those two are somewhat synonymous uh I'm going to get more into the nuances of what that all means throughout this talk but uh yeah I hope by the end of this that you'll have an idea of how you can use flame graphs and profiling to better understand your applications and understand things about it that you wouldn't be able to otherwise understand with uh you know the other signals that are out there um so before I start as I said I'm Ryan um I'm from Indianapolis originally uh moved out to Oakland to work on pyroscope with uh my co-founder Dimitri over here um we were acquired by graffo later that's where I now work um the uh as I guess as a side note one of the reasons why was that we we really felt like profiling had a lot of use inside of the context of other logs metrics and traces and uh that seemed easiest to do there um but that's a conversation for another time um yeah I focus mostly on the product and ux side of profiling obviously there's a lot that goes into collecting profiling data efficiently storing all these flame graphs um being able to query them from the technical side but all of that doesn't necessarily mean anything or have any value if you aren't able to then analyze that data in a way that's meaningful and valuable and so I spent a lot of time focusing on that and how we can improve that within the uh within the project um as far as fun stuff I'm an avid Super Smash Bros player I like disc golf trashy reality TV um yeah with that let's go ahead and get into it what I'm I'm going to talk to talk about today uh what are flame graphs um different types of profilers how profiling kind of fits into the overall observability space how to efficiently you know manage the storage of profiles over time and uh the main use cases for profiling and then finally uh I'm going to give some examples both uh real world of um some internal things that we've done with profiling and also how it can be used to uh help tell a story so starting with what are flame graphs um this is a image by Julia Evans who's one of the uh creators of RB spy a ruby profiler um and this is a abstract example but basically what a flame graph is is it shows which
