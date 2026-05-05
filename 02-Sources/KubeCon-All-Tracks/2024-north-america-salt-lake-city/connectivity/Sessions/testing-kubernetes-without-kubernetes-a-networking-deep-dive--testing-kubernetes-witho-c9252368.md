---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Connectivity"
themes: ["Networking", "Kubernetes Core"]
speakers: ["John Howard", "Solo.io"]
sched_url: https://kccncna2024.sched.com/event/1i7qh/testing-kubernetes-without-kubernetes-a-networking-deep-dive-john-howard-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Testing+Kubernetes+Without+Kubernetes%3A+A+Networking+Deep+Dive+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Testing Kubernetes Without Kubernetes: A Networking Deep Dive - John Howard, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: John Howard, Solo.io
- Schedule: https://kccncna2024.sched.com/event/1i7qh/testing-kubernetes-without-kubernetes-a-networking-deep-dive-john-howard-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Testing+Kubernetes+Without+Kubernetes%3A+A+Networking+Deep+Dive+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Testing Kubernetes Without Kubernetes: A Networking Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qh/testing-kubernetes-without-kubernetes-a-networking-deep-dive-john-howard-soloio
- YouTube search: https://www.youtube.com/results?search_query=Testing+Kubernetes+Without+Kubernetes%3A+A+Networking+Deep+Dive+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-Dp7fAxXuwI
- YouTube title: Testing Kubernetes Without Kubernetes: A Networking Deep Dive - John Howard, Solo.io
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/testing-kubernetes-without-kubernetes-a-networking-deep-dive/-Dp7fAxXuwI.txt
- Transcript chars: 35567
- Keywords: namespace, actually, namespaces, running, process, networking, network, thread, testing, actual, called, basically, runtime, within, device, ethernet, function, instead

### Resumo baseado na transcript

I'm a senior architect at solo.io and I'm here to talk about testing without Kubernetes. So before we get into things, I want to get a quick poll of the audience to see how many people are running tests where they actually have to deploy something on Kubernetes as part of the test. Like I've been running tests in Kubernetes and that's part of projects I've been working on for many years now, so I've learned a few tricks to speed things up and I know all the commands to run and the magic scripts that you need to touch. We often use this project called kind Kubernetes and Docker which helps keeps our cost down. But we at one point were running all of our tests on a real cloud Kubernetes cluster and we were racking up the cloud bills like crazy. So if we have all these problems, then why did almost everyone here raise their hand and say they're testing on Kubernetes?

### Excerpt da transcript

Hey everyone. I'm John Howard. I'm a senior architect at solo.io and I'm here to talk about testing without Kubernetes. So before we get into things, I want to get a quick poll of the audience to see how many people are running tests where they actually have to deploy something on Kubernetes as part of the test. All right, and how many of you guys enjoy that experience? No complaints. We've got one. They're not sure though. I I wouldn't be so sure either. So in my experience like testing on Kubernetes, we do it but it's really rough, right? It gives us a really hard time for all sorts of reasons. The biggest one for me is that it's quite slow. I'm not a very patient guy and in order to set up these tests, we have to go create a Kubernetes cluster. We've got to build some images. We've got to push some summer. We've got to create some deployment services, configuration, have those pull in the the cluster. They spin up, maybe they take a while to pass the readiness probe. All these things and by the time we actually get to our test logic, we've got like 10 minutes down the drain.

We've already finished our coffee and then the actual test maybe only takes 10 seconds, right? It's a huge waste of time. It's also going to be very hard to debug. Aside from the fact that there's now all these moving parts, it's also not so easy to just go attach a debugger to our process and just go see put breakpoints somewhere and figure out what's going wrong. It can be done. I know I'm sure there's plenty of tools out there that help us do it but it's still nowhere near as easy as a basic unit test where you can just you know, click the button in your IDE. It's also hard to onboard. Like I've been running tests in Kubernetes and that's part of projects I've been working on for many years now, so I've learned a few tricks to speed things up and I know all the commands to run and the magic scripts that you need to touch. But we often see really smart people trying to onboard the project and it takes them many hours or even days to figure out just how to run the test and that's time that they're not contributing value and they get really frustrated.

Sometimes they leave and they never come back, right? And it can be expensive and unreliable. And depends on how you run things. We often use this project called kind Kubernetes and Docker which helps keeps our cost down. But we at one point were running all of our tests on a real cloud Kubernetes cluster and we were racking up the
