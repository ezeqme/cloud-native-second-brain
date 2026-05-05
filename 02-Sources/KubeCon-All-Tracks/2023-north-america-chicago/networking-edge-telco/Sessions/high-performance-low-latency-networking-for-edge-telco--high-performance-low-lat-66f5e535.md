---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Networking + Edge + Telco"
themes: ["AI ML", "Networking", "SRE Reliability"]
speakers: ["Dan Daly", "Nupur Jain", "Intel", "Vipin Jain", "AMD", "Ian Coolidge", "Google", "Nabil Bitar", "Bloomberg"]
sched_url: https://kccncna2023.sched.com/event/1R2nJ/high-performance-low-latency-networking-for-edge-telco-dan-daly-nupur-jain-intel-vipin-jain-amd-ian-coolidge-google-nabil-bitar-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=High+Performance%2C+Low+Latency+Networking+for+Edge+%26+Telco+CNCF+KubeCon+2023
slides: []
status: parsed
---

# High Performance, Low Latency Networking for Edge & Telco - Dan Daly & Nupur Jain, Intel; Vipin Jain, AMD; Ian Coolidge, Google; Nabil Bitar, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[AI ML]], [[Networking]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Dan Daly, Nupur Jain, Intel, Vipin Jain, AMD, Ian Coolidge, Google, Nabil Bitar, Bloomberg
- Schedule: https://kccncna2023.sched.com/event/1R2nJ/high-performance-low-latency-networking-for-edge-telco-dan-daly-nupur-jain-intel-vipin-jain-amd-ian-coolidge-google-nabil-bitar-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=High+Performance%2C+Low+Latency+Networking+for+Edge+%26+Telco+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre High Performance, Low Latency Networking for Edge & Telco.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2nJ/high-performance-low-latency-networking-for-edge-telco-dan-daly-nupur-jain-intel-vipin-jain-amd-ian-coolidge-google-nabil-bitar-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=High+Performance%2C+Low+Latency+Networking+for+Edge+%26+Telco+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hXAcaLOh2Uw
- YouTube title: High Performance, Low Latency Networking for Edge & Telco
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/high-performance-low-latency-networking-for-edge-telco/hXAcaLOh2Uw.txt
- Transcript chars: 30089
- Keywords: network, control, offload, hardware, performance, basically, processing, networking, calico, running, functions, encryption, application, workloads, latency, second, enable, packet

### Resumo baseado na transcript

we have a few team members that could not make it uh today one of them was ill for covid one of them couldn't make make it because they're in the UK um so we're going to try to do our best to cover for them so apologize if it's a little bit Rocky here there exists an age-old trade-off between having good abstraction and having the absolute best possible performance one of the key benefits of kubernetes is abstraction making it easier to scale out applications using a cloud

### Excerpt da transcript

we have a few team members that could not make it uh today one of them was ill for covid one of them couldn't make make it because they're in the UK um so we're going to try to do our best to cover for them so apologize if it's a little bit Rocky here there exists an age-old trade-off between having good abstraction and having the absolute best possible performance one of the key benefits of kubernetes is abstraction making it easier to scale out applications using a cloud native approach today in our short-handed panel we'll be discussing the usage of kubernetes in Telco and Edge where workloads are highly latency and throughput sensitive um and also Jitter sensitive and have historically been scaled up using techniques to squeeze every last bit of process and network performance out of the computers the Need for Speed the need for low latency and the need for scale cause developers to adopt kubernetes to deploy workloads onto compute but bypass kubernetes networking instead connectivity to carry Edge and Telco network is done largely with uh routers expensive routers and srov uh single rot IO virtualization this allows uh Edge and Telco to be deployed as containers and pods under standard server infrastructure using kubernetes but they are not interconnected and scaled out using native kubernetes networking last year at cubec con 2022 several of our presenters not including me held a similar panel on how optimize software and new hardware accelerators dpu and ipu can be used to accelerate kubernetes networking underneath the existing abstraction of kubernetes networking what is running in the containers does not change except that they experience a much faster lower latency Network our panel today is applying this concept to Edge and Telco workloads um so this is the panel uh me and nil um my name is Ian kulage I work at Google Cloud on uh Google distributed Cloud um nabil's from Bloomberg um and uh I'll be covering the motivating use case of Telco and Nabil will be covering the value of offload uh the value of standardization and then we'll be presenting a video on neur section of course the graphic does not render okay I don't know why the graphic is not rendering but it's basically just a Nick with some virtual functions um so srov has been used for years to help containers and virtual machines uh believe that they are experiencing the use of a single network card um and also allowing them to get direct access to the PCI bus so they can um bypass uh c
