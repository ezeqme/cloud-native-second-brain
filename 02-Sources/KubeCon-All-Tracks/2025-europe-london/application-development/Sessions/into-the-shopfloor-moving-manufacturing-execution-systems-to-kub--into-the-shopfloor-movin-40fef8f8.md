---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Application Development"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Manuel Peuster", "Andrei Traian Cucuruzac", "Bosch Connected Industry"]
sched_url: https://kccnceu2025.sched.com/event/1txEg/into-the-shopfloor-moving-manufacturing-execution-systems-to-kubernetes-manuel-peuster-andrei-traian-cucuruzac-bosch-connected-industry
youtube_search_url: https://www.youtube.com/results?search_query=Into+the+Shopfloor%3A+Moving+Manufacturing+Execution+Systems+To+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Into the Shopfloor: Moving Manufacturing Execution Systems To Kubernetes - Manuel Peuster & Andrei Traian Cucuruzac, Bosch Connected Industry

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Manuel Peuster, Andrei Traian Cucuruzac, Bosch Connected Industry
- Schedule: https://kccnceu2025.sched.com/event/1txEg/into-the-shopfloor-moving-manufacturing-execution-systems-to-kubernetes-manuel-peuster-andrei-traian-cucuruzac-bosch-connected-industry
- Busca YouTube: https://www.youtube.com/results?search_query=Into+the+Shopfloor%3A+Moving+Manufacturing+Execution+Systems+To+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Into the Shopfloor: Moving Manufacturing Execution Systems To Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEg/into-the-shopfloor-moving-manufacturing-execution-systems-to-kubernetes-manuel-peuster-andrei-traian-cucuruzac-bosch-connected-industry
- YouTube search: https://www.youtube.com/results?search_query=Into+the+Shopfloor%3A+Moving+Manufacturing+Execution+Systems+To+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GgxRHpQIEfg
- YouTube title: Into the Shopfloor: Moving Manufacturing Execution Syste... Manuel Peuster & Andrei Traian Cucuruzac
- Match score: 0.832
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/into-the-shopfloor-moving-manufacturing-execution-systems-to-kubernete/GgxRHpQIEfg.txt
- Transcript chars: 31798
- Keywords: basically, module, library, development, templating, software, within, modules, actually, systems, course, everything, deployment, manufacturing, approach, individual, moving, devops

### Resumo baseado na transcript

Hello everybody, welcome to our talk about into the shop floor moving manufacturing execution systems to kubernetes. I'm a senior DevOps engineer there and you might have heard of our company Bosch. Uh we started to develop the next phase Nix IAS a cloud capable design software that made the first steps in bringing uh this flexibility, scalability and efficiency to the shop floor. Um one was designed for the onremise environment and the other one was um was an early version that that threw us into the cloud world. So we used docker compos for that deploying the microservices with anible and um uh for the for the cloud approach uh basically we used anible to render the the kubernetes manifest and deploy them in in the cloud. Uh now I will let my colleague Manuel to show you what challenges and solutions we encountered along the way.

### Excerpt da transcript

Hello everybody, welcome to our talk about into the shop floor moving manufacturing execution systems to kubernetes. My name is Manuel Pster. I am with Bosch connected industry. I'm a senior DevOps engineer there and you might have heard of our company Bosch. We are a very large manufacturer based in Germany and we are active in many different fields. We are doing mobility solutions, industrial technology, we do energy and building technology as well as customer goods. Overall, we have more than 400,000 employees worldwide. And we are having more than 400 plants that are producing our products in more than 60 different countries. And these plants typically look somehow like that here. So it's a very complex system as you could imagine running in most cases 247. And we as Bosch connected industry are a software provider within Bosch and we are focusing on industry 4.0 from zero solutions and especially we are providing a product which is a manufacturing execution system and for that let me hand over and introduce my colleague Andre who will walk you through the details on what a manufacturing execution system is and what it actually does.

Thank you Manuel. Hello everyone. I'm Andre and I work for Bosch connected the industry as a junior DevOps engineer. All right. So, uh, what is NES? Maybe let's take a look at this picture. We might find some clues. Yeah, we see some guys working here and there. Uh, we have a guy that is driving something that resembles a forklift over there. Looks cool, right? But we don't understand much from it, right? Maybe let's take a deeper look. All right. See that little screen? That is something that we call end on live. Um to the worker is able to see on that screen how many parts will be created in his shift or if any parts has any malfunction. Let's move on. Yeah. Moving to the guy that is driving the forklift. That is actually called the milk run. uh with some some help from another piece of software that we call intra logistics. These guys uh are able to see on their dashboards where the next parts are needed to be delivered. Yeah, the big mysterious glass box actually. Uh here the magic is happening and here small components become bigger parts and bigger parts become the drill you use at home or maybe the electric motor or other component in your car.

And with another uh piece of software called part traceability uh we are able to see uh the the the traces of a part from the beginning uh when it is bored and from the mom
