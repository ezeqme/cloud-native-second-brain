---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Networking + Edge + Telco"
themes: ["Networking"]
speakers: ["Vinay Kulkarni", "eBay"]
sched_url: https://kccnceu2024.sched.com/event/1YeNT/no-soup-for-you-enforcing-network-policies-for-host-processes-via-ebpf-vinay-kulkarni-ebay
youtube_search_url: https://www.youtube.com/results?search_query=No+%27Soup%27+for+You%21+Enforcing+Network+Policies+for+Host+Processes+via+eBPF+CNCF+KubeCon+2024
slides: []
status: parsed
---

# No 'Soup' for You! Enforcing Network Policies for Host Processes via eBPF - Vinay Kulkarni, eBay

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]]
- País/cidade: France / Paris
- Speakers: Vinay Kulkarni, eBay
- Schedule: https://kccnceu2024.sched.com/event/1YeNT/no-soup-for-you-enforcing-network-policies-for-host-processes-via-ebpf-vinay-kulkarni-ebay
- Busca YouTube: https://www.youtube.com/results?search_query=No+%27Soup%27+for+You%21+Enforcing+Network+Policies+for+Host+Processes+via+eBPF+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre No 'Soup' for You! Enforcing Network Policies for Host Processes via eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNT/no-soup-for-you-enforcing-network-policies-for-host-processes-via-ebpf-vinay-kulkarni-ebay
- YouTube search: https://www.youtube.com/results?search_query=No+%27Soup%27+for+You%21+Enforcing+Network+Policies+for+Host+Processes+via+eBPF+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AWAf3H4Qwq8
- YouTube title: No 'Soup' for You! Enforcing Network Policies for Host Processes via eBPF - Vinay Kulkarni, eBay
- Match score: 0.955
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/no-soup-for-you-enforcing-network-policies-for-host-processes-via-ebpf/AWAf3H4Qwq8.txt
- Transcript chars: 31879
- Keywords: network, identity, teller, processes, auditor, traffic, database, policy, process, cluster, equals, cgroup, ebpf, container, running, celium, policies, server

### Resumo baseado na transcript

welcome to the last day of ccon do you guys have a good time so far yay okay so let's get started in this uh session we will cover a new and Innovative way to use ebpf to efficiently enforce Network policies for host processes using ebpf uh before we start a bit about myself uh I'm my name is Vin Kerney and I work for eBay Cloud where I'm helping build uh the network segmentation identity based Network segmentation for eBay the agenda for today is we start with you know kubernetes API server you could have five instances in a typical cluster that has uh like a production cluster uh now you take that to some other uh applications how do we map the identities that is the uh harder part of the problem that we want to solve and the control plan interface that's what we're trying to Define uh which will be very generic the uh the the question about uh what this script does it assumes that part is plumbed in so if you notice plane and then Plumbing it it could still happen but that's some that's a case that I've not really considered uh what we really were looking at is the use case here is uh kubernetes API server in cluster a should only be able to talk to kubernetes cuets in cluster a and not cluster B so thanks for the reply but my question is what if I got introd reduced to some vulnerability after node update like through our my package repository so I would like to set up

### Excerpt da transcript

welcome to the last day of ccon do you guys have a good time so far yay okay so let's get started in this uh session we will cover a new and Innovative way to use ebpf to efficiently enforce Network policies for host processes using ebpf uh before we start a bit about myself uh I'm my name is Vin Kerney and I work for eBay Cloud where I'm helping build uh the network segmentation identity based Network segmentation for eBay the agenda for today is we start with an overview of what network Nam spaces are and understand the difference between host processes and processes that are running in kuber SPS uh we will then cover our use case of efficiently securing host Network process communication that motivated this project and look at how host processes are secured today uh in order to set uh to show what's new in this talk we need to set some background and context for that uh I will briefly look uh we'll briefly look at the structure of celium identities and celium network policies and see how celum uses BPF to enforce Network policies for regular kubernetes spot traffic we then look at how we may assign identities to host processes uh then we wave that EF magic one and identify uh in order to identify host processes inside the kernel in the network traffic data path then uh I will show you a demo of this feature and after that I will touch upon EBAs trust fabric solution which we currently use for securing Network traffic in our defense and depth strategy and then I will open up the floor for questions most of you may be familiar with kubernetes name spaces uh they provide us with a way to isolate cluster resources and divide it amongst users similarly Network namespaces provide us with a way to isolate and share the kernel Network stack amongst multiple applications that are running on the Node on the very left here you can see it's a blue box it's a host process a regular host process it gets to use the local host and the E zero the IP addresses and the routing firewall rules that are there available to the host Network namespace to the right of that you have this SP one with a single container in it it gets its own interfaces IP addresses routing rules Etc which is isolated from the host and for two here has two containers they get to share their own Local Host and ezero interface and and the IP addresses and routing rules but isolated from pod one and from the host so in that sense to summarize the key difference between host processes and kubernetes Spo
