---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Mario Macías", "Marc Tudurí", "Grafana"]
sched_url: https://kccnceu2025.sched.com/event/1txDK/using-ebpf-for-non-invasive-performant-instant-network-monitoring-mario-macias-marc-tuduri-grafana
youtube_search_url: https://www.youtube.com/results?search_query=Using+eBPF+for+Non-invasive%2C+Performant%2C+Instant+Network+Monitoring+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Using eBPF for Non-invasive, Performant, Instant Network Monitoring - Mario Macías & Marc Tudurí, Grafana

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United Kingdom / London
- Speakers: Mario Macías, Marc Tudurí, Grafana
- Schedule: https://kccnceu2025.sched.com/event/1txDK/using-ebpf-for-non-invasive-performant-instant-network-monitoring-mario-macias-marc-tuduri-grafana
- Busca YouTube: https://www.youtube.com/results?search_query=Using+eBPF+for+Non-invasive%2C+Performant%2C+Instant+Network+Monitoring+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Using eBPF for Non-invasive, Performant, Instant Network Monitoring.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txDK/using-ebpf-for-non-invasive-performant-instant-network-monitoring-mario-macias-marc-tuduri-grafana
- YouTube search: https://www.youtube.com/results?search_query=Using+eBPF+for+Non-invasive%2C+Performant%2C+Instant+Network+Monitoring+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HV3Nb_wUro4
- YouTube title: Using eBPF for Non-invasive, Performant, Instant Network Monitoring - Mario Macías & Marc Tudurí
- Match score: 0.924
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/using-ebpf-for-non-invasive-performant-instant-network-monitoring/HV3Nb_wUro4.txt
- Transcript chars: 20614
- Keywords: application, network, information, request, programs, metrics, thanks, thread, probes, cluster, kernel, events, trace, provide, basically, monitoring, graphana, program

### Resumo baseado na transcript

Thank you everybody to come to the very last session of CubeCon in this room. We're really happy that that you have the patience to stay here until the last moment. It has good native performance because it has a just in time compiled and it also uh adds safety. It provides metrics at different levels of your network stack like uh levels about uh metrics about network connections. Uh also application level metrics following the open telemetry specification about different services your application may carry like HTTP, gRPC, Kafka etc. For network metrics, what we what you get is every time for every packet a program is is is run and extracts some information from your connections, source IPs, ports, destination IPs, destination ports also other information like payload size in uh system interface and so on.

### Excerpt da transcript

Thank you everybody to come to the very last session of CubeCon in this room. We're really happy that that you have the patience to stay here until the last moment. Uh my name is uh Mark Tudori. I'm a software engineer in Graphana Labs and we're going to talk today about using EVPF for non-invasive invasive instant network monitoring. And here's Mario. Hello. I'm Mario Matias also from Grafana Lab and uh I work in the same team as as Mark. Uh we work mainly on EVPF and we are going to present how we use EVPF to provide uh monitor to monitor your network your and your application at different layers of the network stack. I know many of you already know EVPF. So but I'd like to do a small introduction uh how we are using ebpf in in in the graphana beta team. Basically you your application run on top of or using uh a set of libraries and it runs on top of the Linux kernel using it it interacts to it with sys call and the Linux kernel has a runtime that allocates the resources and operates your application.

an EVPFbased solution like Grafana Baila uh to provide observability or security or networking any not concretely Graphana but any EVPF based solution also runs as a as a user level application in the user space application but it interacts with the EVP the the EVPF implementation that runs in the kernel that provides It's verification and just in time compilation for safe access to the resources. It provides some maps to communicate the user and the kernel space and some kernel helper helper API to interact and to load the programs. We are using many types of EVPF programs. EVPF is not something like okay I run a I deploy a single program and it does everything. EVPF runs or injects multiple small unlimited programs into different parts of your uh stack in the operating system runtime. You can load network programs that in your network stack. You can run K probes that will be triggered upon concrete or or given uh kernel events. But also you can load you probes. You can load you can add probes into the application or the user space level application.

This is in libraries or in the actual application executable. Good part of EVPF is that if you want to run EVPF or for example instrument an application, you you don't need to rebuild the code of your application to inject the probes. You don't need to redeploy your services with with the EPF agent. It will be EB it will be the EVPF solution who injects directly and transparently to the instrumented applicat
