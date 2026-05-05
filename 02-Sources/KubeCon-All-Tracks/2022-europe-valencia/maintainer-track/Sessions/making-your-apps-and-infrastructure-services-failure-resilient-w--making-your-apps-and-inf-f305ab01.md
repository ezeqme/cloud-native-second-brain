---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Yaron Schneider", "Diagrid", "Henry Spang", "Microsoft"]
sched_url: https://kccnceu2022.sched.com/event/ytuk/making-your-apps-and-infrastructure-services-failure-resilient-with-dapr-yaron-schneider-diagrid-henry-spang-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Making+Your+Apps+and+Infrastructure+Services+Failure-Resilient+with+Dapr+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Making Your Apps and Infrastructure Services Failure-Resilient with Dapr - Yaron Schneider, Diagrid & Henry Spang, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Yaron Schneider, Diagrid, Henry Spang, Microsoft
- Schedule: https://kccnceu2022.sched.com/event/ytuk/making-your-apps-and-infrastructure-services-failure-resilient-with-dapr-yaron-schneider-diagrid-henry-spang-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Making+Your+Apps+and+Infrastructure+Services+Failure-Resilient+with+Dapr+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Making Your Apps and Infrastructure Services Failure-Resilient with Dapr.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytuk/making-your-apps-and-infrastructure-services-failure-resilient-with-dapr-yaron-schneider-diagrid-henry-spang-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Making+Your+Apps+and+Infrastructure+Services+Failure-Resilient+with+Dapr+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Jw05zFpsPms
- YouTube title: Making Your Apps and Infrastructure Services Failure-Resilient with... Yaron Schneider & Henry Spang
- Match score: 0.918
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/making-your-apps-and-infrastructure-services-failure-resilient-with-da/Jw05zFpsPms.txt
- Transcript chars: 28752
- Keywords: circuit, breaker, dapper, application, policy, actually, policies, retries, resiliency, breakers, timeout, component, traffic, maximum, seconds, allows, request, components

### Resumo baseado na transcript

hello everyone and welcome to the dapper maintainers track session my name is eron schneider i'm a co-founder and cto of dagrid and my name is hal spang and i'm a senior engineer at microsoft okay i'm going to be sharing the screen so how please let me know when you can see it what's good okay so today we're going to talk about dapper and how it can help make your application infrastructure services more resilient and fault tolerant but before we deep dive into that let's talk about

### Excerpt da transcript

hello everyone and welcome to the dapper maintainers track session my name is eron schneider i'm a co-founder and cto of dagrid and my name is hal spang and i'm a senior engineer at microsoft okay i'm going to be sharing the screen so how please let me know when you can see it what's good okay so today we're going to talk about dapper and how it can help make your application infrastructure services more resilient and fault tolerant but before we deep dive into that let's talk about what's dapper dapper is essentially a set of apis for application developers to help them write their applications faster and more reliable so instead of focusing on things like state management and pub sub inventory and architectures and triggering their code based on events coming in from different systems and fetching secrets or configuration uh dapper gives them these building blocks for them to just consume these apis from so that they're free to focus on their code on their company's ip and their business logic dapper runs on any infrastructure it runs particularly well on kubernetes which is the recommended production platform for it but it'll also just run on virtual machines dapper has a sidecar architecture in which you have your application here and then the dapper sidecar and the application will just call dapper via http or jrpc so literally any programming language that understands each peer jerkbc can be used to talk to debber and so the application will call dapper um over these protocols and here are some examples of how these look like so for example here the application will call localhost and it's going to tell dapper hey dapper please invoke the card application for me on the method new order and this is an example of state so the application is basically telling dapper hey dapper please fetch the item 67 state for me from a key value store that i configure you work with this is an example of the upper pub sub so publish subscribe and this is an example of how an application might fetch a secret from the upper from a component called key vault so what are these components for state publish and secrets dapper at its very heart has the concept of components which are how developers talk to these different apis or ac rather the actual implementation behind those apis so for example if a developer talks to the adapter state api an operator or developer can basically configure dapper based in the environment they're running in to talk to different databases so f
