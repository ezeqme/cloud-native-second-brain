---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["Kubernetes Core"]
speakers: ["Fabrice Jammes", "Julien Peloton", "CNRS", "Etienne Fayen", "Universite Paris-Saclay"]
sched_url: https://kccnceu2024.sched.com/event/1YeOZ/fink-on-kubernetes-efficient-management-of-massive-alert-streams-for-astronomical-objects-identific-fabrice-jammes-julien-peloton-cnrs-etienne-fayen-universite-paris-saclay
youtube_search_url: https://www.youtube.com/results?search_query=Fink+on+Kubernetes%3A+Efficient+Management+of+Massive+Alert+Streams+for+Astronomical+Objects+Identific+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Fink on Kubernetes: Efficient Management of Massive Alert Streams for Astronomical Objects Identific - Fabrice Jammes & Julien Peloton, CNRS; Etienne Fayen, Universite Paris-Saclay

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Fabrice Jammes, Julien Peloton, CNRS, Etienne Fayen, Universite Paris-Saclay
- Schedule: https://kccnceu2024.sched.com/event/1YeOZ/fink-on-kubernetes-efficient-management-of-massive-alert-streams-for-astronomical-objects-identific-fabrice-jammes-julien-peloton-cnrs-etienne-fayen-universite-paris-saclay
- Busca YouTube: https://www.youtube.com/results?search_query=Fink+on+Kubernetes%3A+Efficient+Management+of+Massive+Alert+Streams+for+Astronomical+Objects+Identific+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Fink on Kubernetes: Efficient Management of Massive Alert Streams for Astronomical Objects Identific.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOZ/fink-on-kubernetes-efficient-management-of-massive-alert-streams-for-astronomical-objects-identific-fabrice-jammes-julien-peloton-cnrs-etienne-fayen-universite-paris-saclay
- YouTube search: https://www.youtube.com/results?search_query=Fink+on+Kubernetes%3A+Efficient+Management+of+Massive+Alert+Streams+for+Astronomical+Objects+Identific+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JklTII0HcKk
- YouTube title: Fink on Kubernetes: Efficient Management of Massive Alert Streams for Astronomical Objects Identific
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/fink-on-kubernetes-efficient-management-of-massive-alert-streams-for-a/JklTII0HcKk.txt
- Transcript chars: 29886
- Keywords: cluster, install, basically, question, production, provide, everything, infrastructure, platform, change, definitely, runner, script, difficult, having, inside, machine, running

### Resumo baseado na transcript

welcome everyone quite impressed with the size of the room so bear with me a bit of adrenaline um so I'm Julian julan I'm a research engineer at cnrs one of the research institute in France this is a picture of an observatory a real one so it's located in Chile it's called the robin Observatory and with fabis who is on stage will join me on stage later and here in this room I'll try to give you some idea of what we are doing uh here okay so

### Excerpt da transcript

welcome everyone quite impressed with the size of the room so bear with me a bit of adrenaline um so I'm Julian julan I'm a research engineer at cnrs one of the research institute in France this is a picture of an observatory a real one so it's located in Chile it's called the robin Observatory and with fabis who is on stage will join me on stage later and here in this room I'll try to give you some idea of what we are doing uh here okay so think think is the name of the project uh it it makes it mixes astronomy and Computing but ex what exactly are we doing so we track changes in the sky and how we do that so imagine you own The Observatory I showed you before you take a picture of the sky you come back the day after and you take a picture of the same sky at the same position you make the difference and then you wonder what have changed and you would be surprised a lot of things change at every time scale second minute hours day months and that can be obvious things like asteroids comets uh that that are passing by that can be less obvious things death of a star for example something explode in the sky and that can be very quick like in a matter of minute imagine the star just ripped off and nothing left so we have to be very quick often just to make sure that we can get the information and and understand what happen the problem is if you have uh a telescope that is very uh powerful so very deep that goes very deep uh and that can scan every little details you will get many of those events those changes that we call alert typically million per night Millions even and so you can just get them and look them by eyes that would be just impossible even if you have an army of PhD student uh you don't get enough so you need to autom to to to make automate to automate all of that and here comes think so think is a brocker so it's a software uh that is basically serving the community by ingesting the stream of alerts that are coming in real time try to classify the events because the events when when they come they are pure information in a pure sense they don't contain any scientific information it's just position a change like a delta in luminosity and a time nothing else so we try to classify that and I will give you some details how we do that we filter them because over the several Millions maybe a few only if is of interest for you and we redistribute that this is what we do basically how we do that so all our services are deployed on academic clouds large C
