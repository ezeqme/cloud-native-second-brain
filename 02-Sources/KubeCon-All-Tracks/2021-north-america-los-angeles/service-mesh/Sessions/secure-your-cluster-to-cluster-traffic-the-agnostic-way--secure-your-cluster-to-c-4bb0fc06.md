---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Service Mesh"
themes: ["Security", "Networking", "Kubernetes Core"]
speakers: ["Pauline Lallinec", "Dave Kerr", "Workday"]
sched_url: https://kccncna2021.sched.com/event/lV4Z/secure-your-cluster-to-cluster-traffic-the-agnostic-way-pauline-lallinec-dave-kerr-workday
youtube_search_url: https://www.youtube.com/results?search_query=Secure+your+cluster-to-cluster+traffic%2C+the+agnostic+way+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Secure your cluster-to-cluster traffic, the agnostic way - Pauline Lallinec & Dave Kerr, Workday

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Pauline Lallinec, Dave Kerr, Workday
- Schedule: https://kccncna2021.sched.com/event/lV4Z/secure-your-cluster-to-cluster-traffic-the-agnostic-way-pauline-lallinec-dave-kerr-workday
- Busca YouTube: https://www.youtube.com/results?search_query=Secure+your+cluster-to-cluster+traffic%2C+the+agnostic+way+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Secure your cluster-to-cluster traffic, the agnostic way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV4Z/secure-your-cluster-to-cluster-traffic-the-agnostic-way-pauline-lallinec-dave-kerr-workday
- YouTube search: https://www.youtube.com/results?search_query=Secure+your+cluster-to-cluster+traffic%2C+the+agnostic+way+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nyiiH0t9ZWA
- YouTube title: Secure your cluster-to-cluster traffic, the agnostic way - Pauline Lallinec & Dave Kerr, Workday
- Match score: 0.839
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/secure-your-cluster-to-cluster-traffic-the-agnostic-way/nyiiH0t9ZWA.txt
- Transcript chars: 21114
- Keywords: cluster, center, private, communication, console, gateway, istio, traffic, mesh, workday, public, ingress, platform, running, envoy, secure, solution, agnostic

### Resumo baseado na transcript

hi everyone this is pauline and dave talking from kubecon about securing your cluster to cluster traffic the agnostic way dave and i work for workday which is a provider of human resources and financial system a couple of years ago workday decided to expand its offering by deploying workday on the public cloud and for this we built a platform based on kubernetes which my colleague dave is part of this team that is building kubernetes platform for workday thanks pauline hey folks i'm dave care i'm a software

### Excerpt da transcript

hi everyone this is pauline and dave talking from kubecon about securing your cluster to cluster traffic the agnostic way dave and i work for workday which is a provider of human resources and financial system a couple of years ago workday decided to expand its offering by deploying workday on the public cloud and for this we built a platform based on kubernetes which my colleague dave is part of this team that is building kubernetes platform for workday thanks pauline hey folks i'm dave care i'm a software engineer devops on the silhoue public cloud team here at workday the sale team is focused around building uh workday's kubernetes based cloud platform and you can usually find me doing things in the gaming tabletop and ctf space if you want to reach out or just talk you can find me at davecare95 on twitter and i'm pauline i'm an i'm an engineer in the public cloud infrastructure team after i spent a number of years working in the same team as dave um when there is no pandemic you can find me in a karaoke room and you can reach out to me on twitter at filalin so what to expect from this presentation well we will give you a use case for a provider agnostic cluster to cluster communication we'll give you an overview of a solution to secure your cluster to cluster communication across providers we will give you a story about what they incrementally implemented that's all that solution will give you an overview of the custom kubernetes resources and operators developed in order to implement that solution and at the end of the slide deck you will find leaks in order to go further by yourself technologies discussed in this talk include kubernetes of course but also helm and voi console aws and istio but first let's see why we need cluster to cluster communication with my colleague dave thanks pauline so closer to cluster communication why do we need it well let's look at a sample service its name is ox it's a service living in cluster one in data center one and sometimes it wants to send messages to his family and friends in cluster 2 in dc2 in the old days ox would use the public-facing load balancer to reach its family and friends but as we know securing public gateway ingress is hard and the teams had to maintain complex configurations for these cross cluster communications this was not sustainable for the platform and engineer platform and infrastructure engineering folks who needed to maintain these complex configurations for any new providers and new reg
