---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["AI ML", "Security", "Storage Data"]
speakers: ["Natalia Reka Ivanko", "John Fastabend", "Isovalent"]
sched_url: https://kccncna2023.sched.com/event/1R2v2/paint-the-picture-detecting-suspicious-data-patterns-in-encrypted-traffic-with-ebpf-and-ktls-natalia-reka-ivanko-john-fastabend-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Paint+the+Picture%21+-+Detecting+Suspicious+Data+Patterns+in+Encrypted+Traffic+with+eBPF+and+KTLS+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Paint the Picture! - Detecting Suspicious Data Patterns in Encrypted Traffic with eBPF and KTLS - Natalia Reka Ivanko & John Fastabend, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]]
- País/cidade: United States / Chicago
- Speakers: Natalia Reka Ivanko, John Fastabend, Isovalent
- Schedule: https://kccncna2023.sched.com/event/1R2v2/paint-the-picture-detecting-suspicious-data-patterns-in-encrypted-traffic-with-ebpf-and-ktls-natalia-reka-ivanko-john-fastabend-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Paint+the+Picture%21+-+Detecting+Suspicious+Data+Patterns+in+Encrypted+Traffic+with+eBPF+and+KTLS+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Paint the Picture! - Detecting Suspicious Data Patterns in Encrypted Traffic with eBPF and KTLS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2v2/paint-the-picture-detecting-suspicious-data-patterns-in-encrypted-traffic-with-ebpf-and-ktls-natalia-reka-ivanko-john-fastabend-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Paint+the+Picture%21+-+Detecting+Suspicious+Data+Patterns+in+Encrypted+Traffic+with+eBPF+and+KTLS+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-2FykHaqvlg
- YouTube title: Paint the Picture! - Detecting Suspicious Data Patterns in E... Natalia Reka Ivanko & John Fastabend
- Match score: 0.787
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/paint-the-picture-detecting-suspicious-data-patterns-in-encrypted-traf/-2FykHaqvlg.txt
- Transcript chars: 24496
- Keywords: observability, actually, encrypted, tetragon, traffic, security, encrypt, application, visibility, option, basically, ebpf, library, kernel, socket, inside, network, binary

### Resumo baseado na transcript

all right hello thanks for coming uh we're here to talk to you today about detecting suspicious data patterns in encrypted traffic with ebpf and ktls and I just want to say I'm excited to talk to everyone about this today because I've been working on ebpf and TLS for close to 10 years now so seeing all the pieces come together is exciting um my name is John fastan I work on tetron I'm the lead there I'm also Main also a colel maintainer um and I work at

### Excerpt da transcript

all right hello thanks for coming uh we're here to talk to you today about detecting suspicious data patterns in encrypted traffic with ebpf and ktls and I just want to say I'm excited to talk to everyone about this today because I've been working on ebpf and TLS for close to 10 years now so seeing all the pieces come together is exciting um my name is John fastan I work on tetron I'm the lead there I'm also Main also a colel maintainer um and I work at is surveillant um and Natalia is with me as well and um she also is at at um is surveillant and she's the product lead um for I think everything we're going to be talking about today um so here's a quick agenda we're going to talk about tetron just to give you a just a quick um brief about what our background is like how we approach problems like our lens for looking at this and then we're going to dive into L7 observability and security and use these cases so let's get going because we have 34 minutes now so first of all what is tetron and the reason um this talk isn't about tetragon we did have a talk on Monday so go back to the conon if you really want to get a deep dive on tetragon but I think it helps to understand what we kind of problems we think about and how we how we go about addressing them so tetragon is a security observability and runtime enforcement agent it's written in BPF they really heavy focus on overhead try to keep that performance really low we do that with BPF in the kernel we move a lot of the business logic that is usually in user space we move it down into the kernel so all your filters um are are down there we keep a a state of all the execs that have happened in a system all of the sockets so we have a map from sockets to execution we have a map from DNS to sockets back to the execution and we can build kind of a map of what's going on in your platform for observability reasons first and foremost and then we follow that up with enforcement so you can say things like if um if this pod or binary even is talking to another binary that's allowed if it's doing a DNS query out to a new DNS server that's not allowed so you can build these fine grain binary level policies um and uh there were actually uh Thomas graph gave a talk Monday about this so go to the symcon if you want to know more about that um but that's really our focus is the security deep observability low overhead so that's where we're coming from both from a networking side but also from a runtime so think about file Int
