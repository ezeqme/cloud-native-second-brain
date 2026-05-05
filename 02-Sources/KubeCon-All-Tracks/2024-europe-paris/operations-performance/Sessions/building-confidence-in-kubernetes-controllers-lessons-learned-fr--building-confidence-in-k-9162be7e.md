---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Matteo Ruina", "Datadog", "Philippe Scorsolini", "Upbound"]
sched_url: https://kccnceu2024.sched.com/event/1YeNQ/building-confidence-in-kubernetes-controllers-lessons-learned-from-using-e2e-framework-matteo-ruina-datadog-philippe-scorsolini-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Building+Confidence+in+Kubernetes+Controllers%3A+Lessons+Learned+from+Using+E2e-Framework+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Building Confidence in Kubernetes Controllers: Lessons Learned from Using E2e-Framework - Matteo Ruina, Datadog & Philippe Scorsolini, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Matteo Ruina, Datadog, Philippe Scorsolini, Upbound
- Schedule: https://kccnceu2024.sched.com/event/1YeNQ/building-confidence-in-kubernetes-controllers-lessons-learned-from-using-e2e-framework-matteo-ruina-datadog-philippe-scorsolini-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Confidence+in+Kubernetes+Controllers%3A+Lessons+Learned+from+Using+E2e-Framework+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Building Confidence in Kubernetes Controllers: Lessons Learned from Using E2e-Framework.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNQ/building-confidence-in-kubernetes-controllers-lessons-learned-from-using-e2e-framework-matteo-ruina-datadog-philippe-scorsolini-upbound
- YouTube search: https://www.youtube.com/results?search_query=Building+Confidence+in+Kubernetes+Controllers%3A+Lessons+Learned+from+Using+E2e-Framework+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Y0R1NAb16Ds
- YouTube title: Building Confidence in Kubernetes Controllers: Lessons Learned from Using E2e-Framework
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/building-confidence-in-kubernetes-controllers-lessons-learned-from-usi/Y0R1NAb16Ds.txt
- Transcript chars: 29879
- Keywords: framework, testing, cluster, actually, environment, running, everything, parallel, clusters, multiple, feature, controllers, resources, controller, crossplane, already, moment, assessment

### Resumo baseado na transcript

hello everyone can you hear me yes so let's get started and thank you for joining us today to talk about one of your favorite topics n2n testing and today we are going to talk about how you can use the n2n framework to build confidence in your kubernetes controllers and clusters my name is mat Rua I'm a senior software engineer at data dog a cloud observability company and I work in the control playe team where we manage the control plane for our users today I'm presenting with

### Excerpt da transcript

hello everyone can you hear me yes so let's get started and thank you for joining us today to talk about one of your favorite topics n2n testing and today we are going to talk about how you can use the n2n framework to build confidence in your kubernetes controllers and clusters my name is mat Rua I'm a senior software engineer at data dog a cloud observability company and I work in the control playe team where we manage the control plane for our users today I'm presenting with Philip I'm Philip scorsolini I work at upbound I'm a crossplay maintainer cool so the agenda for today is to give you an overview about what is the Ann framework and why we have it and then to give you an overview about how we do n2n testing at data dog and cross plane so the first step is to talk about the N framework it's a go framework to do end to end test of components running in kubernetes clusters and why do we have that you can say if I go inside the kubernetes repository there is already an extensive set of example and code to do end to endend tests the problem with the framework is that the sty CL hold with kubernetes itself is designed to test the kubernetes and to ensure a consistent and reliable behavior of the kubernetes codebase it is not designed to be used outside as external Library plus is based on Ginko Gino is a testing framework with foro that has its own DLS and uh it's something that uh is similar to a behavior driven development framework so it has its own set of instruction and its own way to declare the test that is quite different from what you're use when you're writing go tests and so now we have the ENT framework that is an official uh Sig project with a goal to provide a documented approach for endtoend testing an official tool that you can use uh as close as possible to use uh the go test package that you use every day with components to help you to build your test Suite helper functions to get you started when interacting with kubernetes clusters and especially avoiding all the dependencies on the kubernetes code base itself let's have a look about how the n2n framework works so at the heart of the framework there is the environment object it has a config that is used to store your test Suite configuration you can customize the configuration with your own CLI flags and then there is a context that you can use to pass signaling and data uh across each phase of the tests you can use functions to customize different stages of the environment including
