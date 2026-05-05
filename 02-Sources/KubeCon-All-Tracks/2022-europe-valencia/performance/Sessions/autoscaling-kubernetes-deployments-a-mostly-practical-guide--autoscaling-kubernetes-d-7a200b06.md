---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Performance"
themes: ["GitOps Delivery", "Kubernetes Core", "SRE Reliability"]
speakers: ["Natalie Serrino", "New Relic (Pixie team)"]
sched_url: https://kccnceu2022.sched.com/event/ytmH/autoscaling-kubernetes-deployments-a-mostly-practical-guide-natalie-serrino-new-relic-pixie-team
youtube_search_url: https://www.youtube.com/results?search_query=Autoscaling+Kubernetes+Deployments%3A+A+%28Mostly%29+Practical+Guide+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Autoscaling Kubernetes Deployments: A (Mostly) Practical Guide - Natalie Serrino, New Relic (Pixie team)

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Performance]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Natalie Serrino, New Relic (Pixie team)
- Schedule: https://kccnceu2022.sched.com/event/ytmH/autoscaling-kubernetes-deployments-a-mostly-practical-guide-natalie-serrino-new-relic-pixie-team
- Busca YouTube: https://www.youtube.com/results?search_query=Autoscaling+Kubernetes+Deployments%3A+A+%28Mostly%29+Practical+Guide+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Autoscaling Kubernetes Deployments: A (Mostly) Practical Guide.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytmH/autoscaling-kubernetes-deployments-a-mostly-practical-guide-natalie-serrino-new-relic-pixie-team
- YouTube search: https://www.youtube.com/results?search_query=Autoscaling+Kubernetes+Deployments%3A+A+%28Mostly%29+Practical+Guide+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=n8t_hbchQcc
- YouTube title: Autoscaling Kubernetes Deployments: A (Mostly) Practical Guide - Natalie Serrino, New Relic
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/autoscaling-kubernetes-deployments-a-mostly-practical-guide/n8t_hbchQcc.txt
- Transcript chars: 31089
- Keywords: scaler, metric, scaling, actually, application, number, latency, cluster, horizontal, resources, metrics, resource, workload, vertical, second, replicas, autoscaler, request

### Resumo baseado na transcript

um so welcome to my talk uh auto scaling kubernetes deployments a mostly practical guide so hopefully this is the one you actually meant to go to just a little bit about me before we start i'm a software engineer at new relic i work on the pixi open source project pixi is a cncf sandbox project and it basically provides observability for your kubernetes cluster and it's super cool so please check it out i love observability and performance problems and prior to that and partially because of that scaler you can still set a resource cap with the vertical plot auto scaler so when it's adding something like cpu you'll set a cap so it doesn't just grow the cpu indefinitely you may see a container restart or your pod get rescheduled because it's adding more cpu maybe it needs to be moved to a different node to have that amount of cpu you want to use the vertical pod auto scaler in conjunction with the cluster auto scaler because otherwise you can have a situation where you're the number of pods here hit the result of this computation so it started out 72 or 74 once you add two 105 or 107 once you add 2 and then the program is going to terminate so there you go this autoscaler outputs high okay great so this is kind of the end of the prepared remarks but i just wanted to give some shout outs to the kubernetes sig instrumentation they've made it so easy to get started with defining...

### Excerpt da transcript

um so welcome to my talk uh auto scaling kubernetes deployments a mostly practical guide so hopefully this is the one you actually meant to go to just a little bit about me before we start i'm a software engineer at new relic i work on the pixi open source project pixi is a cncf sandbox project and it basically provides observability for your kubernetes cluster and it's super cool so please check it out i love observability and performance problems and prior to that and partially because of that i formally worked in the data space and what we kind of see with observability is a lot of the same problems and observability are data problems so that's kind of the uniting thread behind kind of some of the stuff i've worked on so today's talk is all about auto scaling kubernetes deployments so first we'll briefly touch on what is kubernetes auto scaling and why would you do it then we'll cover more detailed stuff like what are the different knobs that kubernetes auto scaling provides us with you have to know the right bottleneck in your application in order to make your auto scaling as performant as possible so that then we'll cover selecting the right auto scaling metric for your application and then finally i love to push the boundaries of the technology i work in and uh it turns out you can make a touring complete auto scaler for kubernetes so we'll be showing that at the end so let's get started so when you're sizing an application or kubernetes cluster how do you decide how many nodes there should be how do you decide how many pods should be in your deployment how do you know how many resources to give a pod these are not obvious questions or these are obvious questions maybe but they don't necessarily have obvious answers and the strategies that people take for them vary for example there is the methodology of doing a completely random guess and hope that it works you copy pasta from some other thing that i've already deployed on your cluster this is one of the most common ones in my experience you might be one of those people that is always thinking ahead and you're always proactively iterating you're monitoring your deployments and seeing oh shoot cpu is a little bit close to the limit but mostly in practice we reactively iterate we see oh shoot my application's down oh my gosh the pod it's using all the cpu it's given incident auto scaling is intended to help solve some of these problems and kubernetes provides really really good support for auto scalin
