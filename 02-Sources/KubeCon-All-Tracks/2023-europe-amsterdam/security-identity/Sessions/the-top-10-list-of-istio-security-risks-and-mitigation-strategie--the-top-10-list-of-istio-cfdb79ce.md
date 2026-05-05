---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security", "Networking"]
speakers: ["José Carlos Chávez", "Tetrate"]
sched_url: https://kccnceu2023.sched.com/event/1HyPQ/the-top-10-list-of-istio-security-risks-and-mitigation-strategies-jose-carlos-chavez-tetrate
youtube_search_url: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+The+Top+10+List+of+Istio+Security+Risks+and+Mitigation+Strategies+CNCF+KubeCon+2023
slides: []
status: parsed
---

# 🦝 The Top 10 List of Istio Security Risks and Mitigation Strategies - José Carlos Chávez, Tetrate

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]], [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: José Carlos Chávez, Tetrate
- Schedule: https://kccnceu2023.sched.com/event/1HyPQ/the-top-10-list-of-istio-security-risks-and-mitigation-strategies-jose-carlos-chavez-tetrate
- Busca YouTube: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+The+Top+10+List+of+Istio+Security+Risks+and+Mitigation+Strategies+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre 🦝 The Top 10 List of Istio Security Risks and Mitigation Strategies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyPQ/the-top-10-list-of-istio-security-risks-and-mitigation-strategies-jose-carlos-chavez-tetrate
- YouTube search: https://www.youtube.com/results?search_query=%F0%9F%A6%9D+The+Top+10+List+of+Istio+Security+Risks+and+Mitigation+Strategies+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aCCm9VowNSs
- YouTube title: 🦝 The Top 10 List of Istio Security Risks and Mitigation Strategies - José Carlos Chávez, Tetrate
- Match score: 0.913
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-top-10-list-of-istio-security-risks-and-mitigation-strategies/aCCm9VowNSs.txt
- Transcript chars: 29928
- Keywords: security, istio, traffic, policies, attack, mitigation, basically, cannot, mesh, authorization, understand, attacker, permissions, secure, exactly, application, firewall, logs

### Resumo baseado na transcript

I'm so happy to be here at kubicon it's it's uh it's a talk after almost three years of not giving any talk or any participating in any conference so it's like a new start for me in a way so I'm so so happy still nervous um today I'm gonna present the top 10 istio security risks and mitigation strategies um you might have heard of the WASP button for webs and this is uh this is an idea that I came up because I I found this need

### Excerpt da transcript

I'm so happy to be here at kubicon it's it's uh it's a talk after almost three years of not giving any talk or any participating in any conference so it's like a new start for me in a way so I'm so so happy still nervous um today I'm gonna present the top 10 istio security risks and mitigation strategies um you might have heard of the WASP button for webs and this is uh this is an idea that I came up because I I found this need in the cloud native space to have something specific to Cloud native because Cloud native architecture has like specific problems with a specific environments so yeah before I start let me introduce myself um I'm Jose Carlos Chavez I am originally from Peru but I'm based in Barcelona I am an open source Enthusiast I participate in some open source projects I like that I am also an owasp core co-leader for the project called coraza which is a web application firewall and for for the zero trust times and I'm also shifting core maintainer if you heard of distributed tracing and I'm there as well and I'm a loving father as you might think um before I continue I want to just spend a couple of minutes um talking about how all this started and because originally my idea was to to build a list of awareness for um the cloud native or for istio landscape in terms of security risks but then in the process um the security tag for cncf got some attention on this and interest on this so it started as a list for Easter but in the end we are going to make a top 10 list for the cloud native um ecosystem like including kubernetes is the World Service mesh in general so yeah it's it's growing so without further words let me start um we will first talk about what our security risk of course to to understand what we are talking about um risk are something that is hard to define or at least hard to like make concrete right you want to evaluate livelihood versus impact right something that is unlikely to happen but has a huge impact then it's a bidding risk something that is likely to happen but the impact is low then okay it's like a not too important risks so what we measure usually is how easy is for an attacker to carry out an attack in our in our system right is it easy is it just triggering a call is it a doing a DDOS attack um what are the skills needed right it's not the same like I brought it in the script and then I start launching and go routines that will send HTTP requests it's completely different as if I have to get into a server and then f
