---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "SDLC"
themes: ["Runtime Containers"]
speakers: ["Artur Souza", "Yaron Schneider", "Diagrid"]
sched_url: https://kccncna2023.sched.com/event/1R2rk/achieving-functional-quality-in-a-multi-cloud-runtime-artur-souza-yaron-schneider-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Achieving+Functional+Quality+in+a+Multi-Cloud+Runtime+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Achieving Functional Quality in a Multi-Cloud Runtime - Artur Souza & Yaron Schneider, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[SDLC]]
- Temas: [[Runtime Containers]]
- País/cidade: United States / Chicago
- Speakers: Artur Souza, Yaron Schneider, Diagrid
- Schedule: https://kccncna2023.sched.com/event/1R2rk/achieving-functional-quality-in-a-multi-cloud-runtime-artur-souza-yaron-schneider-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Achieving+Functional+Quality+in+a+Multi-Cloud+Runtime+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Achieving Functional Quality in a Multi-Cloud Runtime.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rk/achieving-functional-quality-in-a-multi-cloud-runtime-artur-souza-yaron-schneider-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Achieving+Functional+Quality+in+a+Multi-Cloud+Runtime+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Si1GmTcBSO0
- YouTube title: Achieving Functional Quality in a Multi-Cloud Runtime - Artur Souza & Yaron Schneider, Diagrid
- Match score: 0.826
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/achieving-functional-quality-in-a-multi-cloud-runtime/Si1GmTcBSO0.txt
- Transcript chars: 35320
- Keywords: dapper, testing, running, component, basically, actually, integration, components, scenarios, infrastructure, change, application, environment, multiple, markdown, anything, tested, notice

### Resumo baseado na transcript

hi everyone thank you for coming to our talk my name is iron Schneider I'm the CTO and co-founder of a company called diagrid and we are commercializing the Dapper open source project which I helped create uh while I was at Microsoft before diagrid and the grer with me here we have arker I'm engineering for Di and also Dapper yes we're both maintainers of dapper um I'm a steering committee member of the project Arthur was a steering committee member of the project in the past we're happy

### Excerpt da transcript

hi everyone thank you for coming to our talk my name is iron Schneider I'm the CTO and co-founder of a company called diagrid and we are commercializing the Dapper open source project which I helped create uh while I was at Microsoft before diagrid and the grer with me here we have arker I'm engineering for Di and also Dapper yes we're both maintainers of dapper um I'm a steering committee member of the project Arthur was a steering committee member of the project in the past we're happy to be here and help you talk about how we do quality control and testing um in what we call a multicloud runtime so what is a multicloud runtime Dapper is an example of one but it might just be any sort of application that is deployed to a multicloud environment needs to talk to uh multiples of you know Services Cloud providers libraries they interact with the underlying Cloud infrastructure it's essentially anything that can run in a cloud environment needs to interact with either multiple services within that cloud environment or across Cloud environments and so this comes with lots of challenges because you need to start writing you know different lay in your application to interact with that infrastructure to secure it to make it reliable and there's lots of you know examples from that let's take kubernetes for example kinetes is obviously a multicloud runtime because well it interacts with the cloud infrastructure kinetes has a cloud provider uh layer that interacts with things like Network compute and storage from the cloud provider uh upon which you run Dapper is a really good example um because it does over 150 different connecting connections to all of these cloud services and uh if we really look at Dapper and we're going to talk about how we're doing testing in dapper today but I assure you you can take all of the lessons here to your applications uh whether they're using Dapper or not um Dapper is a set of apis for developers to encapsulate distributed systems challenges instead of you needing to write the same old Border plate code that needs to interact with a database or pubs or a configuration store or a Secrets management store Dapper gives you these best practices encapsulated in a set of apis that you can use to run on top of any cloud or Edge infrastructure it can run as a single binary on your machine on a VM um or on kinetes with a control plane and you can really use it from any type of program language um and this is essentially what Dapper does you
