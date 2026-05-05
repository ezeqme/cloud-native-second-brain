---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Observability"
themes: ["Observability"]
speakers: ["Michael Friedrich", "GitLab"]
sched_url: https://kccnceu2022.sched.com/event/yttd/from-monitoring-to-observability-left-shift-your-slos-with-chaos-michael-friedrich-gitlab
youtube_search_url: https://www.youtube.com/results?search_query=From+Monitoring+to+Observability%3A+Left+Shift+your+SLOs+with+Chaos+CNCF+KubeCon+2022
slides: []
status: parsed
---

# From Monitoring to Observability: Left Shift your SLOs with Chaos - Michael Friedrich, GitLab

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Spain / Valencia
- Speakers: Michael Friedrich, GitLab
- Schedule: https://kccnceu2022.sched.com/event/yttd/from-monitoring-to-observability-left-shift-your-slos-with-chaos-michael-friedrich-gitlab
- Busca YouTube: https://www.youtube.com/results?search_query=From+Monitoring+to+Observability%3A+Left+Shift+your+SLOs+with+Chaos+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre From Monitoring to Observability: Left Shift your SLOs with Chaos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yttd/from-monitoring-to-observability-left-shift-your-slos-with-chaos-michael-friedrich-gitlab
- YouTube search: https://www.youtube.com/results?search_query=From+Monitoring+to+Observability%3A+Left+Shift+your+SLOs+with+Chaos+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BkREMg8adaI
- YouTube title: From Monitoring to Observability: Left Shift your SLOs with Chaos - Michael Friedrich, GitLab
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/from-monitoring-to-observability-left-shift-your-slos-with-chaos/BkREMg8adaI.txt
- Transcript chars: 26502
- Keywords: application, monitoring, observability, certain, metrics, environment, memory, actually, specific, defining, everyone, developer, slo, everything, production, engineering, quality, cluster

### Resumo baseado na transcript

hi everyone nice to finally finally meet you in person um now i'm a little nervous um but it's really i'm really happy to be here and to talk about a little bit about from monitoring to observability left shift your slos with chaos today i'm michael i'm a senior developer evangelist at gitlab on the internet you can find me as dns mihi which is dns michi it's the lovely form of michael in german and i figured later on it doesn't really work in english but please connect

### Excerpt da transcript

hi everyone nice to finally finally meet you in person um now i'm a little nervous um but it's really i'm really happy to be here and to talk about a little bit about from monitoring to observability left shift your slos with chaos today i'm michael i'm a senior developer evangelist at gitlab on the internet you can find me as dns mihi which is dns michi it's the lovely form of michael in german and i figured later on it doesn't really work in english but please connect if you want to and now let's dive into and start with like an sr retail let's build some lego as well a while ago or like 10 years ago we had certain things like black box monitoring state changes measuring slo sla reporting over time at a certain point metrics have been added trending service level objective have been defined and we moved into certain things like white box monitoring and one of the things which inspired me in my past life as an open source monitoring maintainer myself the promisius metrics endpoint was added to docker and it made it much more easy and convenient to look inside the application from there like we defined service level agreements objectives indicators there was much to learn and much to move on like saying hey i won't have an availability of 99.5 percent the objective is much higher and we also need to define an indicator and the error budgets actually which we want to um look at and see whether the slo is actually violated and there are many terms to also consider and figure out like the golden signals which help you immediately identify specific things which are going wrong for example in your kubernetes cluster or in your environment something like latency traffic errors and situation at a certain point you needed to instrument the code like making a code change to really export the metrics you wanted to see the term or site reliability engineer sre was invented and maybe it solved everything maybe not but in the end it was really a nice way to move forward and go into the metrics direction as a developer on the other side something goes wrong you make a mistake there is a bug and one of the stories i want to tell today is we had sort of a monitoring system with a central server satellites a rest api json rpc and it was not that fast and we thought of well let's just add more threads to it problem was then the cpu was locked and maybe we should do something else the application was written in c plus we looked at go at the time and thought well let's use go
