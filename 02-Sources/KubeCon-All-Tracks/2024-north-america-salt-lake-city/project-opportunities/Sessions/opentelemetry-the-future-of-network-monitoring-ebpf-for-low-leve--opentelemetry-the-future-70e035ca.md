---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Observability", "Networking"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW8k/opentelemetry-the-future-of-network-monitoring-ebpf-for-low-level-insights-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=OpenTelemetry%3A+The+Future+of+Network+Monitoring%2C+eBPF+for+Low-Level+Insights+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# OpenTelemetry: The Future of Network Monitoring, eBPF for Low-Level Insights | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Observability]], [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW8k/opentelemetry-the-future-of-network-monitoring-ebpf-for-low-level-insights-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=OpenTelemetry%3A+The+Future+of+Network+Monitoring%2C+eBPF+for+Low-Level+Insights+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre OpenTelemetry: The Future of Network Monitoring, eBPF for Low-Level Insights | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8k/opentelemetry-the-future-of-network-monitoring-ebpf-for-low-level-insights-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=OpenTelemetry%3A+The+Future+of+Network+Monitoring%2C+eBPF+for+Low-Level+Insights+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LSAl0qVWXKQ
- YouTube title: OpenTelemetry: The Future of Network Monitoring eBPF for Low-Level Insights | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/opentelemetry-the-future-of-network-monitoring-ebpf-for-low-level-insi/LSAl0qVWXKQ.txt
- Transcript chars: 3718
- Keywords: collector, reducer, collected, basically, network, ebpf, component, kernel, process, components, deployment, collect, matrix, monitoring, lowlevel, instrument, elementary, deployed

### Resumo baseado na transcript

hello everyone uh this is shivanu I'm a founding engineer in signos I'm also a cncf Ambassador and uh I take some of the shoes in the open Telemetry maintain and contributed at open Telemetry um today we are going to talk about how you can use uh ebpf for lowlevel network monitoring um so let's take a look at what ebpf is on a very high level what you can do is uh you can program the kernel um for example if you want to instrument and process uh

### Excerpt da transcript

hello everyone uh this is shivanu I'm a founding engineer in signos I'm also a cncf Ambassador and uh I take some of the shoes in the open Telemetry maintain and contributed at open Telemetry um today we are going to talk about how you can use uh ebpf for lowlevel network monitoring um so let's take a look at what ebpf is on a very high level what you can do is uh you can program the kernel um for example if you want to instrument and process uh get the relevant data put it into the APF maps and then do some correlation on top of those Maps let's see how open Elementary network does that so there are four crucial components that are involved in the process one is uh kuties collector kernel collector Cloud collector and reducer usually you deploy Kel collector per node as a demon set network collector uh communties collector uh is deployed as a deployment and uh the cloud collector is uh running again as a deployment um K collector is responsible to actually collect the lowlevel network Elementary from all the nodes and it instruments all the traffic that's going through the deployments your pods in that node cuties collector involves two components one is KS fer and KS relay KS Watcher specifically monitors the ku's API server and it monitors some events like like pod deletion and pod creation and then it correlates that with the Tet collected from uh current collector the tety collected from kades water Watcher goes to kads relay that basically forwards that reducer so if you look at this diagram basically all the T that is being collected from all the agents goes to the reducer component which interns forwards that to collector Cloud collector gathers some metadata from the cloud provider for example theability zones it is currently only supported for AWS and gcp so if you are looking for contribution to add more support for other Cloud providers feel free to do so on let's see how the magic works on the reducer side every T once ingested uh it goes through this uh ingestor uh M matching and aggregation where in the individual shards um you basically correlate the low level dietry we'll see that in the demo and um on a very high level uh this is the tenative Pro in the reducer component you collect all the instance metad data from the ks uh collector contain container data from The Collector and basically instrument the process all the processes using the ker collector and the data goes through uh the reducer component where it does the matching and enri
