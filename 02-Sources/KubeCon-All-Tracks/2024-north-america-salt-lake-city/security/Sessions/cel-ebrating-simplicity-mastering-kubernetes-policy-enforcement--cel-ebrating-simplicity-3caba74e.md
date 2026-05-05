---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Kevin Conner", "Getup Cloud", "Anish Ramasekar", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1i7lk/cel-ebrating-simplicity-mastering-kubernetes-policy-enforcement-kevin-conner-getup-cloud-anish-ramasekar-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=CEL-Ebrating+Simplicity%3A+Mastering+Kubernetes+Policy+Enforcement+CNCF+KubeCon+2024
slides: []
status: parsed
---

# CEL-Ebrating Simplicity: Mastering Kubernetes Policy Enforcement - Kevin Conner, Getup Cloud & Anish Ramasekar, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Kevin Conner, Getup Cloud, Anish Ramasekar, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1i7lk/cel-ebrating-simplicity-mastering-kubernetes-policy-enforcement-kevin-conner-getup-cloud-anish-ramasekar-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=CEL-Ebrating+Simplicity%3A+Mastering+Kubernetes+Policy+Enforcement+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre CEL-Ebrating Simplicity: Mastering Kubernetes Policy Enforcement.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lk/cel-ebrating-simplicity-mastering-kubernetes-policy-enforcement-kevin-conner-getup-cloud-anish-ramasekar-microsoft
- YouTube search: https://www.youtube.com/results?search_query=CEL-Ebrating+Simplicity%3A+Mastering+Kubernetes+Policy+Enforcement+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7NO8HXzjLAk
- YouTube title: CEL-Ebrating Simplicity: Mastering Kubernetes Policy Enforcement - Kevin Conner & Anish Ramasekar
- Match score: 0.893
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cel-ebrating-simplicity-mastering-kubernetes-policy-enforcement/7NO8HXzjLAk.txt
- Transcript chars: 32429
- Keywords: policy, validating, admission, expressions, policies, expression, binding, namespace, resource, request, actually, deploy, parameters, validation, within, parameter, resources, object

### Resumo baseado na transcript

good okay so my name is Kevin Connor I'm chief engineer with getup Cloud I'm also a co-author on the second edition of kubernetes In Action along with Marco Lua hi um Manish ramaker I'm a software engineer at Microsoft focusing on security um I'm a member of kuity SE go maintainer of Secret store CSI driver from Seattle Washington okay so here is the agenda for today uh we're going to talk briefly about cell uh then we're going to introduce you to cell playground um basically a playground

### Excerpt da transcript

good okay so my name is Kevin Connor I'm chief engineer with getup Cloud I'm also a co-author on the second edition of kubernetes In Action along with Marco Lua hi um Manish ramaker I'm a software engineer at Microsoft focusing on security um I'm a member of kuity SE go maintainer of Secret store CSI driver from Seattle Washington okay so here is the agenda for today uh we're going to talk briefly about cell uh then we're going to introduce you to cell playground um basically a playground where you can test out cell Expressions uh then we're going to give you a deep dive on validating admission policies mutating admission policies and then basically show you uh the validating admission policies and mutating admission policies in action okay so let's start with a brief overview of cell so what is cell cell is common expression language it's an efficient way to evaluate expressions especially for applications where performance is critical like kubernetes cell is non-turing complete it avoids constructs like loops and recursions making it predictable in terms of execution time this design ensures that cell can evaluate expressions safely and quickly with no risk of running indefinitely U cell evalu expressions in linear time and is optimized for Speed so it performs very well in production environments cell is built to be embedded in applications providing an easy way to integrate policy checks directly into your system without needing any additional dependencies this makes it versatile and useful across various software environments cell also allows for extensibility through its context meaning you can add custom functions or provide additional data the cell reference in Expressions cell is designed to use minimal CPU and memory which is critical in environments with limited resources this efficiency allows you to evaluate expressions even in resource constraint environments like a kubernetes cluster and on the screen here we have an example of what a cell expression might look like uh it's natural syntax and it has dot accessors with ability to have macros or fun FS that the integrator provides okay so the cell language has a straightforward syntax as we looked at in the previous slide uh cell was designed to be embeded into applications so each cell program is an expression that evaluates to a single value and then they're typically short on liners that can be easily inlined in kubernetes API objects um in addition to the cell community libraries kubernete
