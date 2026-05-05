---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Shivangi Motwani", "Zeta", "Ayush Maheshwari", "ShareChat"]
sched_url: https://kccncna2023.sched.com/event/1R2un/deep-dive-into-writing-a-kubernetes-operator-lets-avoid-data-loss-and-down-times-shivangi-motwani-zeta-ayush-maheshwari-sharechat
youtube_search_url: https://www.youtube.com/results?search_query=Deep+Dive+Into+Writing+a+Kubernetes+Operator%3A+Let%E2%80%99s+Avoid+Data+Loss+and+Down+Times%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Deep Dive Into Writing a Kubernetes Operator: Let’s Avoid Data Loss and Down Times! - Shivangi Motwani, Zeta & Ayush Maheshwari, ShareChat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Shivangi Motwani, Zeta, Ayush Maheshwari, ShareChat
- Schedule: https://kccncna2023.sched.com/event/1R2un/deep-dive-into-writing-a-kubernetes-operator-lets-avoid-data-loss-and-down-times-shivangi-motwani-zeta-ayush-maheshwari-sharechat
- Busca YouTube: https://www.youtube.com/results?search_query=Deep+Dive+Into+Writing+a+Kubernetes+Operator%3A+Let%E2%80%99s+Avoid+Data+Loss+and+Down+Times%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Deep Dive Into Writing a Kubernetes Operator: Let’s Avoid Data Loss and Down Times!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2un/deep-dive-into-writing-a-kubernetes-operator-lets-avoid-data-loss-and-down-times-shivangi-motwani-zeta-ayush-maheshwari-sharechat
- YouTube search: https://www.youtube.com/results?search_query=Deep+Dive+Into+Writing+a+Kubernetes+Operator%3A+Let%E2%80%99s+Avoid+Data+Loss+and+Down+Times%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2NjMHLACvc0
- YouTube title: Deep Dive Into Writing a Kubernetes Operator: Let’s Avoid Dat... Shivangi Motwani & Ayush Maheshwari
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/deep-dive-into-writing-a-kubernetes-operator-lets-avoid-data-loss-and/2NjMHLACvc0.txt
- Transcript chars: 25417
- Keywords: operator, actually, having, writing, application, testing, cluster, request, around, custom, resource, issues, process, manage, version, making, started, resources

### Resumo baseado na transcript

thanks for making it to today's talk last day after lunch so thanks um I uh in this talk I would be um sharing a story with you about my experience and my teen's experience on writing cuberes operator What were the challenges that we faced and how we uh overcomed it so the content of this talk would look something like this um I'll be sharing the problem context uh where we started off with what were the um alternative Solutions apart from writing cuberes operator for us how

### Excerpt da transcript

thanks for making it to today's talk last day after lunch so thanks um I uh in this talk I would be um sharing a story with you about my experience and my teen's experience on writing cuberes operator What were the challenges that we faced and how we uh overcomed it so the content of this talk would look something like this um I'll be sharing the problem context uh where we started off with what were the um alternative Solutions apart from writing cuberes operator for us how they did not work for us and how we transitioned into writing a cuber 8s operator uh this was just the half story of finding the right kind of solution for us but the technical challenges started coming after uh we um started implementing the operator and making it productionize uh we would also go ahead uh and see like what are the good resources that are already available uh which you can look into if you want some additional uh resource uh resources or you are just starting out in the space um apart from that we will uh do the recap of what we looked uh what we will look today and any questions that you guys have uh feel free to stop me in between if you you have some questions and something is not clear so yeah let's understand what kind of application uh I and my team were working on um the application would process lots of messages in a day and it would be of multiple kinds right I cannot go into the details or architecture of the application but uh you can um understand something like uh a message processor right right and it could process the events ranging from a simple OTP message to some email content that the marketing team would use right and once these messages would be processed these would be uh send to uh different business applications so application who wants to send the marketing uh uh content right or wants to uh uh process uh the uh credit card transactional statements so such kind of applications would consume these events based on category and configuration so maybe an uh transactional statement would want to read a message uh immediately and even if the communication between the uh between my application and that business application fails they want it to be retried immediately uh for 10 times right but that might not be the case with uh notifications uh Team uh who wants to read marketing messages and all right now uh these configurations that we would manage uh in throughout the presentation I would refer to as States so there were around 15 to 20 such Fields
