---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Fabian Kammel", "James Cleverley-Prance", "ControlPlane"]
sched_url: https://kccnceu2023.sched.com/event/1M6nq/hacking-and-defending-kubernetes-clusters-well-do-it-live-fabian-kammel-james-cleverley-prance-controlplane
youtube_search_url: https://www.youtube.com/results?search_query=Hacking+and+Defending+Kubernetes+Clusters%3A+We%27ll+Do+It+LIVE%21%21%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Hacking and Defending Kubernetes Clusters: We'll Do It LIVE!!! - Fabian Kammel & James Cleverley-Prance, ControlPlane

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Fabian Kammel, James Cleverley-Prance, ControlPlane
- Schedule: https://kccnceu2023.sched.com/event/1M6nq/hacking-and-defending-kubernetes-clusters-well-do-it-live-fabian-kammel-james-cleverley-prance-controlplane
- Busca YouTube: https://www.youtube.com/results?search_query=Hacking+and+Defending+Kubernetes+Clusters%3A+We%27ll+Do+It+LIVE%21%21%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Hacking and Defending Kubernetes Clusters: We'll Do It LIVE!!!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1M6nq/hacking-and-defending-kubernetes-clusters-well-do-it-live-fabian-kammel-james-cleverley-prance-controlplane
- YouTube search: https://www.youtube.com/results?search_query=Hacking+and+Defending+Kubernetes+Clusters%3A+We%27ll+Do+It+LIVE%21%21%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=J3pS-XBdNpU
- YouTube title: Hacking & Defending Kubernetes Clusters: We'll Do It LIVE!! - Fabian Kammel & James Cleverley-Prance
- Match score: 0.801
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/hacking-and-defending-kubernetes-clusters-well-do-it-live/J3pS-XBdNpU.txt
- Transcript chars: 25334
- Keywords: attacker, cluster, container, access, threat, scenario, default, account, security, attack, available, information, permissions, control, scenarios, little, application, running

### Resumo baseado na transcript

hello everyone and welcome to hacking and defending kubernetes clusters we'll do it live you've got myself James lovely France I am a security engineer at control plane I lead our penetration testing services purple teaming uh deliver training and workshops and facilitate CTF events and scenarios such as the one we run at kubecon events like this one all right hi I'm Fabian I'm a security architect also with control plane and I'm passionate about all things Automation and security especially supply chain Security in the last year we

### Excerpt da transcript

hello everyone and welcome to hacking and defending kubernetes clusters we'll do it live you've got myself James lovely France I am a security engineer at control plane I lead our penetration testing services purple teaming uh deliver training and workshops and facilitate CTF events and scenarios such as the one we run at kubecon events like this one all right hi I'm Fabian I'm a security architect also with control plane and I'm passionate about all things Automation and security especially supply chain Security in the last year we spoke at six.com and some Community Days and meetups in around Berlin where I'm also located so what we're going to talk about today we'll do a high level overview of what threat modeling is and why it might be important to you and then we'll go through six exploit scenarios at PACE look at the uh and so in each of those individual scenarios uh we'll have a little bit of a look at the impact of the attack uh and then we will map uh through to controls that we would use to prevent against some of the techniques that we demonstrate and have a little bit of a discussion about those sort of mitigation strategies then at the end we'll summarize and have a look at what we've learned in the session all right as as James mentioned let's first Define the term threat model or the exercise of threat modeling so what is this in a threat model session you should really Define and also address the risks of your system right why would you want to do this of course we want to find security issues before someone else does hopefully before it goes into production um so to prevent this we want to do this as soon as possible so if you have a new system for example do a threat model session as soon as an architecture is available or even an architecture draft can be used as input here if you have a system that is to be extended this is usually done with the means of a user story or something similar so you can use that piece to think about like new risks being introduced into the system and how to mitigate them so who should join these threat model sessions right this is a group exercise so you should really bring everyone to the table your developers your sres who know how to run this stuff in production bring your security folks and everyone with domain knowledge or like special knowledge about the system everyone can can bring insights to the table and you find more risks together and you find more appropriate mitigations together as well really
