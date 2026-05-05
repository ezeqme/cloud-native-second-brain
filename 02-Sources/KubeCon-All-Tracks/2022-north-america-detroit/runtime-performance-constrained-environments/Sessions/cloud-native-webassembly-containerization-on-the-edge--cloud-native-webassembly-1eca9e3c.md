---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Runtime Performance + Constrained Environments"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Michael Yuan", "Second State"]
sched_url: https://kccncna2022.sched.com/event/182Ed/cloud-native-webassembly-containerization-on-the-edge-michael-yuan-second-state
youtube_search_url: https://www.youtube.com/results?search_query=Cloud-Native+WebAssembly%3A+Containerization+On+the+Edge+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Cloud-Native WebAssembly: Containerization On the Edge - Michael Yuan, Second State

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Runtime Performance + Constrained Environments]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Michael Yuan, Second State
- Schedule: https://kccncna2022.sched.com/event/182Ed/cloud-native-webassembly-containerization-on-the-edge-michael-yuan-second-state
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud-Native+WebAssembly%3A+Containerization+On+the+Edge+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Cloud-Native WebAssembly: Containerization On the Edge.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ed/cloud-native-webassembly-containerization-on-the-edge-michael-yuan-second-state
- YouTube search: https://www.youtube.com/results?search_query=Cloud-Native+WebAssembly%3A+Containerization+On+the+Edge+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Kg5z5A5wH0A
- YouTube title: Cloud-Native WebAssembly: Containerization On the Edge - Michael Yuan, Second State
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/cloud-native-webassembly-containerization-on-the-edge/Kg5z5A5wH0A.txt
- Transcript chars: 38168
- Keywords: container, webassembly, assembly, containers, native, support, application, javascript, docker, applications, language, runtime, started, libraries, network, database, running, however

### Resumo baseado na transcript

let's get started and uh um first of all thank you so much for coming to the last presentation of this coupon I wasn't expecting this many people you know I I've done the last talk in conferences before and they were you know it's typically was much less attended so thank you all for coming here and I appreciate that um so the title of this talk is cloud native web assembly so there are two keywords here it's Cloud native and webassembly so when we when we think

### Excerpt da transcript

let's get started and uh um first of all thank you so much for coming to the last presentation of this coupon I wasn't expecting this many people you know I I've done the last talk in conferences before and they were you know it's typically was much less attended so thank you all for coming here and I appreciate that um so the title of this talk is cloud native web assembly so there are two keywords here it's Cloud native and webassembly so when we when we think about cloud computing what do we you know I think the key notion really is there's there's really no Cloud it's just other people's computer running your program right you know so virtualization or isolation is the most important technique in cloud computing you know so it started with the virtual machine the VM where you know um it's they can virtualize the infrastructure and provide each user its own say um you know computer right and then on cloud native Revolution comes along and it makes provide tools and uh um and new design patterns to make it easier you know to based on container technology so you know so you would have a Linux container starting with stalker Linux containers and um you know so makes it easier for um to have to run my tenancy applications and share the infrastructure so that's Cloud native so what about web assembly so a little history about webassembly before we um before we really goes on so webassembly started out as a Sandbox or virtualization technology in the browser you know so in the browser people you know we have JavaScript we can run code in JavaScript however it's not satisfactory you know people wants to run codes that faster you know native code in C plus plus or in Rust so they invented a new runtime inside the browser that provides a security sandbox it's called webassembly and so webassembly started in the browser and then it moves to the world of um we now call web3 but back then we call blockchain you know that's uh so um many of you know that you certain blockchain but after you certain blockchain almost all the leading blockchain projects are using web assembly to run smart contracts which really when you think about it it has similar characteristics about application you know programs in the browser which is somewhat somewhere else the program have to run on your infrastructure right you know so it's uh you have to provide a safe sandbox faster on it and it's also the same kind of problem that cloud native wants to solve so then in 2019 you know there
