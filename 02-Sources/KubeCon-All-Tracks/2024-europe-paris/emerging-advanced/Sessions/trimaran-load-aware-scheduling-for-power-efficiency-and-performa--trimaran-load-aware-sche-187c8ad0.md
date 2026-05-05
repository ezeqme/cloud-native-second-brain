---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Emerging + Advanced"
themes: ["SRE Reliability"]
speakers: ["Asser Tantawi", "Chen Wang", "IBM"]
sched_url: https://kccnceu2024.sched.com/event/1YeRE/trimaran-load-aware-scheduling-for-power-efficiency-and-performance-stability-asser-tantawi-chen-wang-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Trimaran%3A+Load-Aware+Scheduling+for+Power+Efficiency+and+Performance+Stability+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Trimaran: Load-Aware Scheduling for Power Efficiency and Performance Stability - Asser Tantawi & Chen Wang, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Asser Tantawi, Chen Wang, IBM
- Schedule: https://kccnceu2024.sched.com/event/1YeRE/trimaran-load-aware-scheduling-for-power-efficiency-and-performance-stability-asser-tantawi-chen-wang-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Trimaran%3A+Load-Aware+Scheduling+for+Power+Efficiency+and+Performance+Stability+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Trimaran: Load-Aware Scheduling for Power Efficiency and Performance Stability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRE/trimaran-load-aware-scheduling-for-power-efficiency-and-performance-stability-asser-tantawi-chen-wang-ibm
- YouTube search: https://www.youtube.com/results?search_query=Trimaran%3A+Load-Aware+Scheduling+for+Power+Efficiency+and+Performance+Stability+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CSNIrl-Qtx4
- YouTube title: Trimaran: Load-Aware Scheduling for Power Efficiency and Performance Stability
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/trimaran-load-aware-scheduling-for-power-efficiency-and-performance-st/CSNIrl-Qtx4.txt
- Transcript chars: 22476
- Keywords: utilization, plugin, average, target, variation, cluster, second, plugins, variations, packing, traran, request, memory, limits, little, background, schedular, others

### Resumo baseado na transcript

good morning everybody uh welcome to the talk on traran load load aware uh schedule plugins my name is Asser Tanta from IBM research my colleague uh my name is Chen Wong I'm also uh working in IBM research and we have been working in these schedular plugins for years all right so let me walk you through or both of us we're going to walk you through the traran if you haven't heard about it it's a family of schedu plug there are load aware and there is three

### Excerpt da transcript

good morning everybody uh welcome to the talk on traran load load aware uh schedule plugins my name is Asser Tanta from IBM research my colleague uh my name is Chen Wong I'm also uh working in IBM research and we have been working in these schedular plugins for years all right so let me walk you through or both of us we're going to walk you through the traran if you haven't heard about it it's a family of schedu plug there are load aware and there is three of them it's a bit confusing and we're trying to resolve that here make a distinction between the the three plugins that exist they are all Upstream you can download them and try them if you haven't yet and we're going to show you some use cases and demos of what these traran plugins do so the the alarms that you might see in in your cluster that some nodes um may be experiencing High load congested and others are not or that some nodes have spiky uh kind of uh uh CPU and or memory uh load whereas others are not and you may have in your cluster some uh parts that are able to get up to their limits whereas others in the same cluster cannot these are all symptoms of uh a need for one of the traran plugins this is not necessarily true that traran will solve these this might be due to other cases but we just list them as um uh motivation for for for the need of a traran plugin traran is load aware as I said and it it relies on the load Watcher which is an open source uh piece of component that Chen and others have been working on and you can see in the diagram here it relies on either the metric server Prometheus server or or some other signal FX server and we'll will'll get all the metrics for utilization of CPU and memory both averages and variations around the average and will expose that through premisus and that's what the Taran uh plugins use through premisus those um metrics uh they they are smoothed through the load Watcher and used by the trian plugins all right so what are the goals of these uh three plugins uh they kind of have separate separate goals and that's why we have three of them so the first one tackles the energy it works to get the uh the node utilization uh currently it's only CPU but hopefully we're going to expand that to other resources such as GPU and others uh to get the utilization around a particular Target utilization and I'll talk about that in a second uh the second plugin is about avoiding congestion and interference it avoids the a lot of spiky kind of behavior in in load D
