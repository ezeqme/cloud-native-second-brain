---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Performance"
themes: ["Observability", "Kubernetes Core", "SRE Reliability"]
speakers: ["Eden Federman", "Verizon"]
sched_url: https://kccncna2021.sched.com/event/lV1o/effortless-profiling-on-kubernetes-eden-federman-verizon
youtube_search_url: https://www.youtube.com/results?search_query=Effortless+Profiling+on+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Effortless Profiling on Kubernetes - Eden Federman, Verizon

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Performance]]
- Temas: [[Observability]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Los Angeles
- Speakers: Eden Federman, Verizon
- Schedule: https://kccncna2021.sched.com/event/lV1o/effortless-profiling-on-kubernetes-eden-federman-verizon
- Busca YouTube: https://www.youtube.com/results?search_query=Effortless+Profiling+on+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Effortless Profiling on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1o/effortless-profiling-on-kubernetes-eden-federman-verizon
- YouTube search: https://www.youtube.com/results?search_query=Effortless+Profiling+on+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VPN-q2rjhxc
- YouTube title: Effortless Profiling on Kubernetes - Eden Federman, Verizon
- Match score: 0.836
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/effortless-profiling-on-kubernetes/VPN-q2rjhxc.txt
- Transcript chars: 14167
- Keywords: profiling, profiler, profile, application, container, running, basically, process, created, applications, python, command, plugin, recommendation, invoke, having, performance, called

### Resumo baseado na transcript

so hey everybody thank you for coming to my talk and staying so late so today we're going to talk about effortless profiling on kubernetes a little bit about myself so my name is Eden I'm currently an engineer at Yahoo I've been coding for almost 15 years now H I'm really into everything observability and profiling I think that uh finding performance issues in production is my hobby and uh I created one of the tools that I'm going to show you here today called Cube C flame so uh keep plugin this flame plugin actually saves us from learning H which is the best profiler to use what is the specific API details and copying over the file having to restart our application having to have a shell on our container image all

### Excerpt da transcript

so hey everybody thank you for coming to my talk and staying so late so today we're going to talk about effortless profiling on kubernetes a little bit about myself so my name is Eden I'm currently an engineer at Yahoo I've been coding for almost 15 years now H I'm really into everything observability and profiling I think that uh finding performance issues in production is my hobby and uh I created one of the tools that I'm going to show you here today called Cube C flame so uh today we first going to start by some a little bit of introduction to what is profiling and how how do you analyze a profile H what's the best way to visualize a profile uh secondly we're going to talk about some of the challenges uh in general in profiling and secondly in specifically when profiling in Rees and lastly we're going to do some demo I'm going to try to profile multiple applications and uh do it first manually and then H by using Cube CTL flame so profiling is the act of analyzing the performance of applications in order to improve Poly Performance section of code and simple worlds is basically per profiling is the process you do when you have some slow run running application and you want to understand why this application runs so slowly uh one of the most popular ways to visualize a profile to present a profile is by generating something that is called Flame graph uh flame graphs look something like that it's uh multiple stock traces stocked on top of each other uh basically the y- axis is the stock def is basically the stack itself the x-axis is the sample population basically the Y the flame is H the longer a method call took uh the color is usually used in order to differentiate between different type of uh of method cods for example here H green can be Java code red can be C code and orang can be some I don't know k space code and the order is usually not that important uh H flame graphs are usually ordered alphabetically so I try to to think about why profiling is so hard and I think it comes down to two main reasons uh the F the first is overhead uh simply the act of profiling an application makes the application run slower H this is the main reason that most people try to avoid profiling in production because we don't want to hurt our production applications uh secondly is that if I have some application that is not ready to be profiled yet it's not profil I need to to modify the code in multiple ways in order to H be able to profile the application uh for exa
