---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Giuseppe Avolio", "CERN"]
sched_url: https://kccncna2024.sched.com/event/1i7oV/orchestrating-quasi-real-time-data-processing-in-the-computing-farm-of-the-atlas-experiment-at-cern-giuseppe-avolio-cern
youtube_search_url: https://www.youtube.com/results?search_query=Orchestrating+Quasi-Real+Time+Data+Processing+in+the+Computing+Farm+of+the+ATLAS+Experiment+at+CERN+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Orchestrating Quasi-Real Time Data Processing in the Computing Farm of the ATLAS Experiment at CERN - Giuseppe Avolio, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Giuseppe Avolio, CERN
- Schedule: https://kccncna2024.sched.com/event/1i7oV/orchestrating-quasi-real-time-data-processing-in-the-computing-farm-of-the-atlas-experiment-at-cern-giuseppe-avolio-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Orchestrating+Quasi-Real+Time+Data+Processing+in+the+Computing+Farm+of+the+ATLAS+Experiment+at+CERN+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Orchestrating Quasi-Real Time Data Processing in the Computing Farm of the ATLAS Experiment at CERN.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oV/orchestrating-quasi-real-time-data-processing-in-the-computing-farm-of-the-atlas-experiment-at-cern-giuseppe-avolio-cern
- YouTube search: https://www.youtube.com/results?search_query=Orchestrating+Quasi-Real+Time+Data+Processing+in+the+Computing+Farm+of+the+ATLAS+Experiment+at+CERN+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vUB3NzqMAzo
- YouTube title: Orchestrating Quasi-Real Time Data Processing in the Computing Farm of the ATLAS Experi... G. Avolio
- Match score: 0.993
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/orchestrating-quasi-real-time-data-processing-in-the-computing-farm-of/vUB3NzqMAzo.txt
- Transcript chars: 37107
- Keywords: actually, number, startup, scheduling, increase, controller, cluster, manager, little, hardware, second, deployment, topological, filtering, simple, working, custom, configuration

### Resumo baseado na transcript

okay good afternoon everybody thanks for being here my name is jpe I work for for I work for CERN and in particular for the data Cris of Atlas which is one of the big experiments at CERN so let's start with the with the talk now um I'm I would like to to to tell you a story that is the story of our kubernetes journey in the that acquisition system of the atel experiment at CERN and I have divided this journey into three parts the departure the

### Excerpt da transcript

okay good afternoon everybody thanks for being here my name is jpe I work for for I work for CERN and in particular for the data Cris of Atlas which is one of the big experiments at CERN so let's start with the with the talk now um I'm I would like to to to tell you a story that is the story of our kubernetes journey in the that acquisition system of the atel experiment at CERN and I have divided this journey into three parts the departure the adventure and the reward but before going deep into that I would like to spend a few words about Atlas and large Adon collider which is the accelerator providing the physics that we like and additionally let me also give some motivations and the challenges that we are going to face introducing kubernetes in our in our system so let's start with Atlas and LHC and and this is atlas so this is a picture a real picture in scale of Atlas it's actually a big detector as you can see and at is one of the main of the four main particle detectors are the large Adon collider and when I say huge I say I say that because atas is 44 M long and 25 M high so really really really a little bit and you see it has this Barrel shape with two end caps and consider that that collisions are actually happening at the heart of Atlas so atas is really built around one of the places where the collisions are happening but what is the goal of attles so obviously the goal of attles is to collect data from the proton collisions but what does that really mean that Tas has to collect this data I will try to explain here in a in a in a kind of few word so collisions at LHC are happening at a rate of 40 MHz so this means that every 25 NCS there there are protons colliding into the accelerator as I said before the protons are colliding actually at the in the middle of Atlas really at the Earth of Atlas and the product of proton collisions are several other particles so you have a huge amount of particles that are traversing the atlas detector all the active parts of the atas detector and all the electric signals then are digitized and we have data out of collisions and this is what we call an event okay so this is the event is the representation of the collisions for for atas so we can say I will mention this word several times event so atas the input rate for the events of atas is 40 Megs matching the the Collision rate of the of the LHC and what is the final goal of atas as I said before we want to collect this data this physics event and we want to s
