---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Unclassified"
themes: ["Cloud Native"]
speakers: ["Fabio Oliveira", "Srinivasan Parthasarathy", "IBM Research"]
sched_url: https://kccnceu2021.sched.com/event/iE2l/live-experiments-with-k8s-applications-pitfalls-and-how-to-avoid-them-fabio-oliveira-srinivasan-parthasarathy-ibm-research
youtube_search_url: https://www.youtube.com/results?search_query=Live+Experiments+with+K8s+Applications%3A+Pitfalls+and+How+to+Avoid+Them+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Live Experiments with K8s Applications: Pitfalls and How to Avoid Them - Fabio Oliveira & Srinivasan Parthasarathy, IBM Research

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Unclassified]]
- Temas: [[Cloud Native]]
- País/cidade: Virtual / Virtual
- Speakers: Fabio Oliveira, Srinivasan Parthasarathy, IBM Research
- Schedule: https://kccnceu2021.sched.com/event/iE2l/live-experiments-with-k8s-applications-pitfalls-and-how-to-avoid-them-fabio-oliveira-srinivasan-parthasarathy-ibm-research
- Busca YouTube: https://www.youtube.com/results?search_query=Live+Experiments+with+K8s+Applications%3A+Pitfalls+and+How+to+Avoid+Them+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Live Experiments with K8s Applications: Pitfalls and How to Avoid Them.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2l/live-experiments-with-k8s-applications-pitfalls-and-how-to-avoid-them-fabio-oliveira-srinivasan-parthasarathy-ibm-research
- YouTube search: https://www.youtube.com/results?search_query=Live+Experiments+with+K8s+Applications%3A+Pitfalls+and+How+to+Avoid+Them+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6lwgFzRykPY
- YouTube title: Live Experiments with K8s Applications: Pitfalls and Ho... Fabio Oliveira & Srinivasan Parthasarathy
- Match score: 0.841
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/live-experiments-with-k8s-applications-pitfalls-and-how-to-avoid-them/6lwgFzRykPY.txt
- Transcript chars: 22707
- Keywords: experiment, traffic, iterate, versions, release, metrics, version, winner, solution, business, metric, experiments, organizations, applications, experimentation, automated, canary, testing

### Resumo baseado na transcript

hello everyone thanks for joining our session today my name is fabio olivier and i'll be presenting together with srinivas and partaserati let me start by saying a few words about us we are passionate about what we call live experiments because we believe that live experiments can help organizations answer the phone question how do you know how can you know whether or not every single new code release that you make deliver that delivers value to your customers and to your business we co-founded a project called iterate

### Excerpt da transcript

hello everyone thanks for joining our session today my name is fabio olivier and i'll be presenting together with srinivas and partaserati let me start by saying a few words about us we are passionate about what we call live experiments because we believe that live experiments can help organizations answer the phone question how do you know how can you know whether or not every single new code release that you make deliver that delivers value to your customers and to your business we co-founded a project called iterate that embodies our vision for a live experimentation of kubernetes applications and how we can help businesses and we have experience creating solutions to help sres and to automate devops practices before we go into the specifics of live experimentation let's take a step back and look at current trends uh when it comes to cloud native code release practices these trends we extracted them from a recent cncf survey report that was made available publicly in november of 2020.

that survey found that the majority of organizations release code weekly or more frequently and that there is a widespread use of ci and cd tools in production but those findings do not come as a surprise that survey also revealed that there was a seven percent increase in the number of organizations that release code daily sometimes multiple times per day which is also not surprising however and paradoxically that same survey uncovered uh a trend that was surprising to us from 2018 to there was a big decrease a 21 decrease in the number of organizations that adopt fully automated release cycles so organizations seem to be raising code more frequently but automating less that is not intuitive so why why is that happening there are a few uh explanations for this phenomenon perhaps there are newcomers that are just trying out automation solutions to see what works maybe some organizations have the need to control uh a few aspects of code releases or perhaps there's a lack of trust in the tools currently used for cloud native release robots what can we do to change that so we are on a mission to change this state of affairs so here are the goals for this presentation and how it relates to the trends that we that we just saw first and foremost we want to raise awareness of facts misconceptions that we have seen in pitfalls that organizations might encounter when um adopting uh fully automated solutions for uh code releases we want to elevate the practice of release automation
