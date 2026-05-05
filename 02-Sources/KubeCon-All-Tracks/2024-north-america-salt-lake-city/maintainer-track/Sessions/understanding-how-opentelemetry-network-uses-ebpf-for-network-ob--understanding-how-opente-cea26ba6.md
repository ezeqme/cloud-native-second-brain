---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Networking", "Community Governance"]
speakers: ["Shivanshu Raj Shrivastava", "SigNoz", "Jonathan Perry", "PerfPod"]
sched_url: https://kccncna2024.sched.com/event/1how7/understanding-how-opentelemetry-network-uses-ebpf-for-network-observability-shivanshu-raj-shrivastava-signoz-jonathan-perry-perfpod
youtube_search_url: https://www.youtube.com/results?search_query=Understanding+How+OpenTelemetry+Network+Uses+eBPF+for+Network+Observability+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Understanding How OpenTelemetry Network Uses eBPF for Network Observability - Shivanshu Raj Shrivastava, SigNoz & Jonathan Perry, PerfPod

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Shivanshu Raj Shrivastava, SigNoz, Jonathan Perry, PerfPod
- Schedule: https://kccncna2024.sched.com/event/1how7/understanding-how-opentelemetry-network-uses-ebpf-for-network-observability-shivanshu-raj-shrivastava-signoz-jonathan-perry-perfpod
- Busca YouTube: https://www.youtube.com/results?search_query=Understanding+How+OpenTelemetry+Network+Uses+eBPF+for+Network+Observability+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Understanding How OpenTelemetry Network Uses eBPF for Network Observability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1how7/understanding-how-opentelemetry-network-uses-ebpf-for-network-observability-shivanshu-raj-shrivastava-signoz-jonathan-perry-perfpod
- YouTube search: https://www.youtube.com/results?search_query=Understanding+How+OpenTelemetry+Network+Uses+eBPF+for+Network+Observability+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ljf671BSu2g
- YouTube title: Understanding How OpenTelemetry Network Uses eBPF for Network Observab... S.R. Shrivastava, J. Perry
- Match score: 0.944
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/understanding-how-opentelemetry-network-uses-ebpf-for-network-observab/Ljf671BSu2g.txt
- Transcript chars: 28708
- Keywords: network, collector, information, metadata, kernel, basically, reducer, application, aggregation, overhead, provider, coming, collection, running, itself, events, collected, sending

### Resumo baseado na transcript

welcome everyone um thanks for coming for the talk I hope you have enough energy this is the last talk of today sessions and yeah I'm shivanu I'm a founding engineer at signos I'm also a CNF Ambassador and maintainer and cond to open DEET and uh we have Jonathan here who is yeah who is the founder NC at buff pod so let's get started so first of all um let's see what is the outline of the talk so firstly we will see why network observ is important

### Excerpt da transcript

welcome everyone um thanks for coming for the talk I hope you have enough energy this is the last talk of today sessions and yeah I'm shivanu I'm a founding engineer at signos I'm also a CNF Ambassador and maintainer and cond to open DEET and uh we have Jonathan here who is yeah who is the founder NC at buff pod so let's get started so first of all um let's see what is the outline of the talk so firstly we will see why network observ is important and uh what is evf and how you can use it for Network obility what are the tooling available uh for to facilitate Network obility by vpf and understand the architecture of open network we'll dive deep into all the individual components and agents that open tele Network uses finally will have a demo and also how you can get involved so let's see why network obility is important what problem does it solves and why use vpf so modern distributed systems are hard they are hybrid meaning they are running different kubernetes clusters across different regions sometimes M cloud and they are heterogeneous in nature meaning there are collection of VMS bare metals and communties clusters working all together and it becomes challenging to uh figure out some problems especially at the network level because lowlevel tetri are not present by default your logs uh spans and traces does not give give enough context on the Network clear even if you are using uh service smash uh for example if you are using sto or Envoy sometimes you need to correlate the anoy logs to get the flow of the logs and flow of the network request fundamentally it's very complex uh to troubleshoot the network related problems there's limited visibility into Network performance um there's in ineffective detection of anomaly and security threads so for for example if some of the ports are open in your infrastructure you wouldn't know and and and if there's some traffic flowing through it if there's not there's no network observability it would be very hard to figure out those problems there's lack of insight into user experience and application performance there are compliance and audit challenges and um it is very hard for Network cost analysis so for example in a side car pattern if you're using sto There is extra overhead off side car but if you're using some lowlevel tool which is gathering all the Telemetry from the Linux con itself uh the cost is low but if you are not monitoring your network then figuring out the network cost analysis is is hard also N
