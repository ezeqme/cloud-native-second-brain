---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Angel De Miguel Meana", "Rafael Fernandez Lopez", "VMware"]
sched_url: https://kccnceu2023.sched.com/event/1HybK/create-istio-filters-with-any-programming-language-angel-de-miguel-meana-rafael-fernandez-lopez-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Create+Istio+Filters+with+Any+Programming+Language+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Create Istio Filters with Any Programming Language - Angel De Miguel Meana & Rafael Fernandez Lopez, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Angel De Miguel Meana, Rafael Fernandez Lopez, VMware
- Schedule: https://kccnceu2023.sched.com/event/1HybK/create-istio-filters-with-any-programming-language-angel-de-miguel-meana-rafael-fernandez-lopez-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Create+Istio+Filters+with+Any+Programming+Language+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Create Istio Filters with Any Programming Language.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HybK/create-istio-filters-with-any-programming-language-angel-de-miguel-meana-rafael-fernandez-lopez-vmware
- YouTube search: https://www.youtube.com/results?search_query=Create+Istio+Filters+with+Any+Programming+Language+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_y3f18gf4FA
- YouTube title: Create Istio Filters with Any Programming Language - Angel De Miguel Meana & Rafael Fernandez Lopez
- Match score: 0.77
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/create-istio-filters-with-any-programming-language/_y3f18gf4FA.txt
- Transcript chars: 30812
- Keywords: webassembly, filters, javascript, actually, proxies, specific, filter, envoy, languages, create, inside, machine, virtual, assembly, interpreter, configuration, configure, infrastructure

### Resumo baseado na transcript

my name is Angel and today I'm here with my teammate Raphael to talk to you about how to create Easter filters with any programming language before starting let me introduce the team we are working on we both are part of wasan labs which is a small thing inside of the VMware Office of the CTO we focus on creating and contributing uh to projects that showcase the possibilities of webassembly we also create different tools and other projects to increase the adoption of Developers for this technology that

### Excerpt da transcript

my name is Angel and today I'm here with my teammate Raphael to talk to you about how to create Easter filters with any programming language before starting let me introduce the team we are working on we both are part of wasan labs which is a small thing inside of the VMware Office of the CTO we focus on creating and contributing uh to projects that showcase the possibilities of webassembly we also create different tools and other projects to increase the adoption of Developers for this technology that we are really excited for apart from that we also create 13 experiments we will We love to do that and today we want to to show you one of the experiments that we recently did one thing that I think everyone of us that work with services and infrastructure knows that proxies are everywhere proxies are a critical piece of an infrastructure we can talk about proxies even in single node deployments where we have a reverse proxy that redirects the traffic to our services we can think of big clusters with more than 100 nodes and a lot of different proxies collaborating together to serve the traffic redirect things and provide the actual content that all users want to see there are a lot of different ones we have voy nginx traffic there are different types so today we are going to focus on Envoy and specifically about Easter installation that are based on Envoy if we look how a regular deployment looks these days we have a lot of different applications that actually share some common resources or the same box we can say it could be multiple nodes but they are part of the same infrastructure then we want to expose them outside so we create gateways and everything so users can access to them and in some cases we need more advanced connection between the different uh resources and the different services and we include proxies across all the different services so they can connect together and they can perform other Advanced actions this is not something that it's easy to manage and to deploy fortunately we have projects like istio that allows you to easily deploy all these different proxies without any hustle just put them where they should be and connect the services as we need so now let's talk a little bit more about how we can extend all those small proxies all those small dots that we have in our infrastructure when talking about extending a proxy what we are talking is about adding custom behaviors that it's tailored to some specific use cases it could be someth
