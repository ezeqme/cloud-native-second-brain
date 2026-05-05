---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Customizing + Extending Kubernetes"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Jesse Sanford", "Greg Haynes", "Autodesk"]
sched_url: https://kccnceu2023.sched.com/event/1HyXP/building-a-platform-engineering-fabric-with-the-kube-api-at-autodesk-jesse-sanford-greg-haynes-autodesk
youtube_search_url: https://www.youtube.com/results?search_query=Building+a+Platform+Engineering+Fabric+with+the+Kube+API+at+Autodesk+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Building a Platform Engineering Fabric with the Kube API at Autodesk - Jesse Sanford & Greg Haynes, Autodesk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jesse Sanford, Greg Haynes, Autodesk
- Schedule: https://kccnceu2023.sched.com/event/1HyXP/building-a-platform-engineering-fabric-with-the-kube-api-at-autodesk-jesse-sanford-greg-haynes-autodesk
- Busca YouTube: https://www.youtube.com/results?search_query=Building+a+Platform+Engineering+Fabric+with+the+Kube+API+at+Autodesk+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Building a Platform Engineering Fabric with the Kube API at Autodesk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyXP/building-a-platform-engineering-fabric-with-the-kube-api-at-autodesk-jesse-sanford-greg-haynes-autodesk
- YouTube search: https://www.youtube.com/results?search_query=Building+a+Platform+Engineering+Fabric+with+the+Kube+API+at+Autodesk+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tPNmY1Q1GoY
- YouTube title: Building a Platform Engineering Fabric with the Kube API at Autodesk - Jesse Sanford & Greg Haynes
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/building-a-platform-engineering-fabric-with-the-kube-api-at-autodesk/tPNmY1Q1GoY.txt
- Transcript chars: 40043
- Keywords: platform, resources, resource, implementation, actually, account, capabilities, pattern, crossplane, simple, developer, thanks, application, tooling, software, cluster, controllers, provider

### Resumo baseado na transcript

testing welcome everybody glad all of you are joining us here um Welcome to our talk on building a platform engineering fabric with the kubernetes API at Autodesk so over the past couple years we've been on a journey to transition our developer platform away from a set of organically grown tightly coupled tools with extensive configuration and libraries into declarative API first platform with kubernetes API at its core this is an area with lots of lots of Interest across the industry so our hope here is to convey

### Excerpt da transcript

testing welcome everybody glad all of you are joining us here um Welcome to our talk on building a platform engineering fabric with the kubernetes API at Autodesk so over the past couple years we've been on a journey to transition our developer platform away from a set of organically grown tightly coupled tools with extensive configuration and libraries into declarative API first platform with kubernetes API at its core this is an area with lots of lots of Interest across the industry so our hope here is to convey some of the challenges some of the wins and our general experiences during this journey in order to help others be successful at a similar Journey before getting in our talk let us briefly introduce ourselves U Jesse would you like to sure yeah no problem hey everybody you got you found us here we're at the end of the hallway I'm Jesse I uh I'm a senior principal software engineer here at Autodesk um and uh I focus on the juncture of our our platform engineering uh and software supply chain security initiatives and when I'm not in front of a computer I uh I like to sale and Backcountry ski and pretty much do anything outdoors thanks Jesse um so I'm Greg Haynes I'm a software architect and I'm also the open source lead at Autodesk um I focus primarily on internal developer platform software and my background before that is has been primarily in uh open source cloud platform development so spent about 10 years doing that before coming to Autodesk and now I'm excited to get back to it so today we're going to start off with an overview of where our developer platform was at the beginning of this journey and how we got there next I'll talk about our Northstar or what motivations led us to this major effort and then we'll cover some of the Alternatives considered as part of planning out how we'd accomplish this afterward we'll cover a couple specific technical challenges we encountered and how we solve them and to wrap up we'll hopefully impart some big picture wisdom with you and some lessons learned now let's begin the story of our developer platform so this is a very high level View and from this angle I expect it should be pretty familiar to all of you this is an early rudimentary version of our developer platform at the time is primarily focused on Simple app delivery at the bottom we have our user who primarily interacts with two Services GitHub for Source control and Jenkins for cicd the user supplies some application configuration via git which
