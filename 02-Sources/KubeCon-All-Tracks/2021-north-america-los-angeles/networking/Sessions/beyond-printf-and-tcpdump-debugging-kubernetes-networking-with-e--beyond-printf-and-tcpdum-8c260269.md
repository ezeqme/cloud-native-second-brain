---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Networking"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Martynas Pumputis", "Aditi Ghag", "Isovalent"]
sched_url: https://kccncna2021.sched.com/event/lV5a/beyond-printf-and-tcpdump-debugging-kubernetes-networking-with-ebpf-martynas-pumputis-aditi-ghag-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+printf+and+tcpdump%3A+Debugging+Kubernetes+Networking+with+eBPF+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Beyond printf and tcpdump: Debugging Kubernetes Networking with eBPF - Martynas Pumputis & Aditi Ghag, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Martynas Pumputis, Aditi Ghag, Isovalent
- Schedule: https://kccncna2021.sched.com/event/lV5a/beyond-printf-and-tcpdump-debugging-kubernetes-networking-with-ebpf-martynas-pumputis-aditi-ghag-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+printf+and+tcpdump%3A+Debugging+Kubernetes+Networking+with+eBPF+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Beyond printf and tcpdump: Debugging Kubernetes Networking with eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5a/beyond-printf-and-tcpdump-debugging-kubernetes-networking-with-ebpf-martynas-pumputis-aditi-ghag-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Beyond+printf+and+tcpdump%3A+Debugging+Kubernetes+Networking+with+eBPF+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vqx-hLYfCYE
- YouTube title: Beyond printf & tcpdump: Debugging Kubernetes Networking with eBPF - Martynas Pumputis & Aditi Ghag
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/beyond-printf-and-tcpdump-debugging-kubernetes-networking-with-ebpf/vqx-hLYfCYE.txt
- Transcript chars: 19601
- Keywords: kernel, packet, function, network, information, program, address, ebpf, destination, request, whenever, functions, filter, executed, source, interface, debugging, networking

### Resumo baseado na transcript

well hi everyone uh welcome to my talk uh i'm aditi i'm a software engineer working at isovelyn and this talk features a joint work with martinez a bit of context into why debugging kubernetes networking is relevant for us martinez and i work on psyllium which is an open source cni uh powered by ebpf and we work with one of the most sophisticated set of users uh and to enable them to network and secure their communities clusters uh so yeah let's get started uh in this talk

### Excerpt da transcript

well hi everyone uh welcome to my talk uh i'm aditi i'm a software engineer working at isovelyn and this talk features a joint work with martinez a bit of context into why debugging kubernetes networking is relevant for us martinez and i work on psyllium which is an open source cni uh powered by ebpf and we work with one of the most sophisticated set of users uh and to enable them to network and secure their communities clusters uh so yeah let's get started uh in this talk i'm going to share our debugging experiences and present a new tool that we have developed using ebpf so let's take a common kubernetes cluster where our request is coming onto kubernetes node and it's being delivered to a service part so the request traffic will first get processed at neck it'll then get routed to linux kernel networking stack and then uh it'll traverse from host network namespace to report network namespace via a couple of uh v devices pair so whenever there are network connect connectivity issues we start with control plane checking all the configurations are correct our services our services are deployed the service part is up and running and we always make sure that it's not the dns but today i want to draw attention to a key component that often are treated as a black box and that's the linux kernel network debugging linux current networking is hard and let's zoom in to see why that is so this is a detailed network flow diagram of linux kernel network internals and as you can see there are overwhelming number of uh packet processing functions so when you send a single packet it requires many many hops until it reaches its destination uh so sure there are like packet counters and uh stats that you can observe uh but these are not enough uh to get to the root cause because kernel state can't be observed in real time uh in an easy manner so we have this internal uh joke uh that whenever we're trying to track a packet in linux kernel uh it's like finding waldo one can easily feel lost when they uh fall down the uh rabbit hole of linux kernel networking so next we are gonna look at some of our uh uh most godo tools um so one of our most favorite tools is tcp dump and you always reach first whenever there are like network connectivity issues and i agree that uh it's a good tool to start your debug routine but the problem with tcp down is that it only gives you high level information because uh the tcp tap tcp dump tap points are at the periphery of linux kernel networkin
